---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 30min 
publish_date: 2022.09.28
---

## <span style="font-family: Courier">  ATAC-Seq pipeline
<span style="font-family: Courier">  In the introduction (which I didn't write at 28 of Sep), we introduced the basic workflow of ATAC-Seq. In this note, I will introduce each step carefully with codes.

### <span style="font-family: Courier">  Pre-analysis: Quality Control & Alignment

#### <span style="font-family: Courier">  fastp

<span style="font-family: Courier"> We also introduced fastp in RNA-Seq, it's just a fast and all in one quality check machine. It can simultaneously check the quality and trim the reads.

```
fastp -a CTGTCTCTTATA --detect_adapter_for_pe -w 12 --length_required 20 -q 30 -i $fq1 -I $fq2 -o trim/${sampled}_1.fq.gz -0 trim/${sampleid}_2.fq.gz -h trim/${sampleid}_fastp.html
```

- <span style="font-family: Courier">   **-a, --adapter_sequence**      
         the adapter for read1. For SE data, if not specified, the adapter will be auto-detected. For PE data, this is used if R1/R2 are found not overlapped. (string [=auto])

- <span style="font-family: Courier"> **--detect_adapter_for_pe** 
    Turns on the auto detection of adapters for pair end sequencing data. (Automatically turned on for single end data)

- <span style="font-family: Courier"> **--length_required**
    Reads shorter than length_required will be discarded, default is 15.

<span style="font-family: Courier">  For more commands, type `fastp -help` in terminal or look [here](../RNA-seq/Tools.md).

<span style="font-family: Courier">  Ex. **For loops in shell**
```
    for ((i=0; i<=10; i++)); do          
        echo "/$i"; 
    done
```

#### <span style="font-family: Courier"> Bowtie2

<span style="font-family: Courier"> Bowtie2 is another sequence alignment tool. Similar to HISAT2 (in fact they are developed by the same bunch of people, interesting).

```
bowtie2 -x ~/reference/bowtie2/xenTro10 -1 trim/${sampleid}_1.fq.gz -2 trim/${sampleid}_2.fq.gz -p 12 -X 2000 | samtools view -bS - -@ 12 > mapping/${sampleid}.bam
```

<span style="font-family: Courier">  Sometimes we need to filter low quality alignments, or alignments with problems (marked in the FLAG part of SAM files). In TianChi's pipeline, he used a python program to filter these reads, but I think tools in samtools can fulfill the needs. Nevertheless, here's the code.
```bash
/home/bio-ligp/miniconda3/envs/py2/bin/python ~/bin/filter_bam.py -i mapping/${sampleid}.bam -o mapping/${sampleid}.filt.bam
```

#### <span style="font-family: Courier"> Sambamba
<span style="font-family: Courier"> A samtools like program to process sam and bam files. But sambamba can process sam and bam files quicker, which is very interesting.

```
sambamba sort --sort-picard -m 8G --tmpdir=tmp -t 12 mapping/${sampleid}.filt.bam -o mapping/${sampleid}.sort.bam

sambamba markdup -r -t 12 --tmpdir=tmp mapping/${sampleid}.sort.bam mapping/${sampleid}.dup.bam
```
<span style="font-family: Courier">  Sambamba sort:
: <span style="font-family: Courier"> **--sort-picard sort** by query name like in picard
    **-m** approximate total memory limit for all threads (by default 2GB)
    **--tmpdir=TMPDIR** directory for storing intermediate files; default is system directory for temporary files
    **-t** number of threads
    **-o** output file

<span style="font-family: Courier">  Sambamba markdup:
: <span style="font-family: Courier"> **-r** remove duplicates instead of just marking them
    **-t** number of threads to use
    **--tmpdir=TMPDIR** directory for storing intermediate files; default is system directory for temporary files

<span style="font-family: Courier"> We also need to sort the bam file again with samtools. Because the sambamba sorting sort the bam file according to picard.

```bash
samtools sort -@ 12 mapping/$sampleid.dup.bam > mapping/$sampleid.dup.sort.bam
```

### <span style="font-family: Courier">  Post-alginment: Quality Control

#### <span style="font-family: Courier"> get_tlen
<span style="font-family: Courier">  Getting the fragment length.
```bash
python ~/bin/get_tlen.py -i mapping/$sampleid.dup.sort.bam > mapping/$sampleid.dup.sort.bam.tlen.txt
```

#### <span style="font-family: Courier"> ATACseqQC
<span style="font-family: Courier">  An R package that can perform ATACseqQC. Requires the bam file.

### <span style="font-family: Courier"> Peak Calling

#### <span style="font-family: Courier"> MACS2

<span style="font-family: Courier">  MACS2 can differentiate the statistically significant peaks of reads from others and generate a peak file.
```bash
macs2 callpeak -t mapping/$sampleid.dup.sort.bam -g 1.435e9 --keep-dup all --outdir peaks -n $sampleid -q 0.05 --slocal 10000 --nomodel --nolambda -B --SPMR
```
<span style="font-family: Courier">  **-t** ChIP-seq treatment file. If multiple files are given as '-t A B C', then they will all be read and pooled together. REQUIRED.

<span style="font-family: Courier"> **-g** The effective genome size. It can be 1.0e+9 or 1000000000, or shortcuts:'hs' for human (2.7e9), 'mm' for mouse (1.87e9), 'ce' for C. elegans (9e7) and 'dm' for fruitfly (1.2e8), Default:hs

<span style="font-family: Courier"> **--keep-dup** It controls the behavior towards duplicate tags at the exact same location -- the same coordination and the samestrand. The 'auto' option makes MACS calculate the maximum tags at the exact same location based on binomaldistribution using 1e-5 as pvalue cutoff; and the 'all' option keeps every tags. If an integer is given, at mostthis number of tags will be kept at the same location. Note, if you've used samtools or picard to flag reads as'PCR/Optical duplicate' in bit 1024, MACS2 will still read them although the reads may be decided by MACS2 asduplicate later. If you plan to rely on samtools/picard/any other tool to filter duplicates, please remove thoseduplicate reads and save a new alignment file then ask MACS2 to keep all by '--keep-dup all'. The default is tokeep one tag at the same location. Default: 1

<span style="font-family: Courier"> **--outdir** If specified all output files will be written to that directory. Default: the current working directory

<span style="font-family: Courier"> **-n NAME** Experiment name, which will be used to generate output file names. DEFAULT: "NA" 

<span style="font-family: Courier"> **-q** Minimum FDR (q-value) cutoff for peak detection. DEFAULT: 0.05. -q, and -p are mutually exclusive.

<span style="font-family: Courier"> **--slocal**The small nearby region in basepairs to calculate dynamic lambda. This is used to capture the bias near the peak summit region. Invalid if there is no control data. If you set this to 0, MACS will skip slocal lambda calculation. *Note* that MACS will always perform a d-size local lambda calculation while the control data is available. The final local bias would be the maximum of the lambda value from d, slocal, and llocal size windows. While control is not available, d and slocal lambda won't be considered. DEFAULT: 1000

<span style="font-family: Courier"> **--nomodel** Whether or not to build the shifting model. If True, MACS will not build model. by default it means shifting size = 100, try to set extsize to change it. It's highly recommended that while you have many datasets to process and you plan to compare different conditions, aka differential calling, use both 'nomodel' and 'extsize' to make signal files from different datasets comparable. DEFAULT: False

<span style="font-family: Courier"> **--nolambda**If True, MACS will use fixed background lambda as local lambda for every peak region. Normally, MACS calculates a dynamic local lambda to reflect the local bias due to the potential chromatin accessibility.

<span style="font-family: Courier"> **-B** Whether or not to save extended fragment pileup, and local lambda tracks (two files) at every bp into a bedGraph file. DEFAULT: False

<span style="font-family: Courier"> **--SPMR** If True, MACS will SAVE signal per million reads for fragment pileup profiles. It won't interfere with computing pvalue/qvalue during peak calling, since internally MACS2 keeps using the raw pileup and scaling factors between larger and smaller dataset to calculate statistics measurements. If you plan to use the signal output in bedGraph to call peaks using bdgcmp and bdgpeakcall, you shouldn't use this option because you will end up with different results. However, this option is recommended for displaying normalized pileup tracks across many datasets. Require -B to be set. Default: False

#### <span style="font-family: Courier">  bamCoverage

<span style="font-family: Courier"> Convert bam reads into bigwig files. Which are made to calculate the "score" of each gene. That is to say, how many reads are mapped with a certain gene of the genome. Of course, because the thing is going into the igv, the bam files need to be indexed.

```bash
samtools index -@ 12 mapping/$sampleid.dup.sort.bam
bamCoverage -b mapping/$sampleid.dup.sort.bam -p 12 --normalizeUsing CPM --binSize 5 -o bigwig/$sampleid.ATAC.bw
```
> <span style="font-family: Courier">  binSize is actually a very important parameter that will influence plotting later. It means that five nucleotide reads are combined to calculate one score, rather than computing it one by one, which is time and storage consuming. See [here](https://deeptools.readthedocs.io/en/develop/content/tools/bamCoverage.html) for more info.

### <span style="font-family: Courier"> Plotting the Heatmap

<span style="font-family: Courier"> After getting the bigwig file, we can draw heatmaps using the [**computeMatrix**](https://deeptools.readthedocs.io/en/develop/content/tools/computeMatrix.html?highlight=computeMatrix#reference-point) tool and [**plotHeatmap**](https://deeptools.readthedocs.io/en/develop/content/tools/plotHeatmap.html?highlight=plotHeatmap) tool from deeptools.

#### <span style="font-family: Courier"> computeMatrix

<span style="font-family: Courier"> ComputeMatrix tool compares different peaks with the bigwig file to get where the location of the peaks.

<span style="font-family: Courier">  **Reference Point**
<span style="font-family: Courier"> Because of my spupidity, I actually stuck the summit bed file (with sequence length 1) into computeMatrix, and sadly the other method of scale-region didn't work. So we switched to reference point (because in principle, a summit can also used to draw a heatmap). It did finish calculating the matrix, but I don't think the result is correct since instead of using the middle of the peak sequence, we only used the summit as the middle, which is not the case in every peak.
<span style="font-family: Courier"> **However, after careful consideration, this is actually what we need to use during ATAC-seq**
<span style="font-family: Courier"> Yeah, I'm back on the right track. We actually need to use the summits bed file and reference point to draw our ATAC-Seq heatmap. What we cared is the amount of reads in proximity to our peak (i.e. our summit), so using the summit as the middle point is completely right.

```bash
computeMatrix reference-point -S /data/bio-zhanglm/xenopus/09_Bigwig/st9-ATAC-${i}.bw \
        -R /data/bio-zhanglm/xenopus/08_Peak/st9-${i}_summits.bed \
        -o /data/bio-zhanglm/xenopus/10_Graph/st9-${i}-matrix.gz -a 1500 -b 1500;
```

#### <span style="font-family: Courier"> plotHeatmap
<span style="font-family: Courier"> With the data you got from computeMatrix, you can plot a heatmap showing the amount of reads on either end of your peak.
```bash
plotHeatmap -m /data/bio-zhanglm/xenopus/10_Graph/st9-2-matrix.gz -o /data/bio-zhanglm/xenopus/10_Graph/st9-ATAC-Heatmap-2.png
```
<span style="font-family: Courier"> Compared to earlier steps, this step is really as easy as hell.