---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 15min
publish_date: 2024.06.20
---
This is my note & plan markdown for my bioinformatics project about RNA velocity anlaysis. The project is about reproducing some of the results, and I think this markdown is quite helpful for further analysis. So I put it here in my blog, in case I might need it in the future. All the other codes are stored in the GitHub repository for [this project](https://github.com/BHAAA-ZLM/RNA-velocity_Review).
## To Do List 
- [x] Perform velocyto analysis on the already single Bam files.

        - [x] Find out what happened to the python error output.
        - [ ] Check the mask GTF file to see what problems is it causing.
        - [x] Inspect the GTF file to see if it might be the cause of all the problems.

- [x] Perform velocyto analysis on the squashed and then seperated Bam files.
- [ ] Try `cellranger` pipeline for other datasets.
- [x] Prepare files required for velocyto analysis.
- [x] Turn the squashed Bam into multiple Bam files.
- [x] Figure out a way to run `velocyto` somewhere.

## Starting from GEO files

### Environment Setup
```bash
# A new conda environment on taiyi
conda create -n pre python=3.8

# install required packages
conda install numpy scipy cython numba matplotlib scikit-learn h5py click
pip install velocyto
```

### Chromaffin Cells Analysis  
In the directory `/scratch/2024-05-04/bio-zhanglm/bioinfo/chromaffin`.

#### Acquiring Data from GEO 
```bash
#!/bin/sh                          
#BSUB -J N_F                        ##job name
#BSUB -q ser                     ##queue name
#BSUB -n 10                        ##number of total cores     
#BSUB -R "span[ptile=40]"          ##40 cores per node
#BSUB -W 12:00                     ##walltime in hh:mm 
#BSUB -R "select[hname!='r13n18']" ##exclusive r13n18
#BSUB -e log/err.log                   ##error log
#BSUB -o log/H.log                     ##output log

cd /scratch/2024-05-04/bio-zhanglm/bioinfo/chromaffin

geofetch -i GSE99933

mkdir fastq 
ls | while read line
do
	echo $line
	fastq-dump --outdir fastq $line
done
```

#### Making mm10 index for STAR alignment
The mm10 reference directory is `/data/bio-zhanglm/genome/mm10`.
STAR was setup in the `(base)` environment.
```bash
cd /data/bio-zhanglm/genome/mm10

wget https://ftp.ensembl.org/pub/release-111/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna_sm.toplevel.fa.gz
wget https://ftp.ensembl.org/pub/release-111/gtf/mus_musculus/Mus_musculus.GRCm39.111.gtf.gz

# 'dna_sm' - soft-masked genomic DNA. 
# All repeats and low complexity regions have been replaced 
# with lowercased versions of their nucleic base

gunzip Mus_musculus.GRCm39.111.gtf.gz
gunzip Mus_musculus.GRCm39.dna_sm.toplevel.fa.gz

STAR \
        --runThreadN 25 \
        --runMode genomeGenerate \
        --genomeDir /data/bio-zhanglm/genome/mm10 \
        --genomeFastaFiles Mus_musculus.GRCm39.dna_sm.toplevel.fa \
        --sjdbGTFfile Mus_musculus.GRCm39.111.gtf
```

Out put:
```bash
STAR --runThreadN 25 --runMode genomeGenerate --genomeDir /data/bio-zhanglm/genome/mm10 --genomeFastaFiles Mus_musculus.GRCm39.dna_sm.toplevel.fa --sjdbGTFfile Mus_musculus.GRCm39.111.gtf
        STAR version: 2.7.10b   compiled: 2022-11-01T09:53:26-04:00 :/home/dobin/data/STAR/STARcode/STAR.master/source
May 08 15:43:29 ..... started STAR run
May 08 15:43:29 ... starting to generate Genome files
May 08 15:44:14 ..... processing annotations GTF
May 08 15:44:35 ... starting to sort Suffix Array. This may take a long time...
May 08 15:44:47 ... sorting Suffix Array chunks and saving them to disk...
May 08 15:50:58 ... loading chunks from disk, packing SA...
May 08 15:52:04 ... finished generating suffix array
May 08 15:52:04 ... generating Suffix Array index
May 08 15:56:09 ... completed Suffix Array index
May 08 15:56:09 ..... inserting junctions into the genome indices
May 08 15:59:04 ... writing Genome to disk ...
May 08 15:59:04 ... writing Suffix Array to disk ...
May 08 15:59:21 ... writing SAindex to disk
May 08 15:59:24 ..... finished successfully
```

### STAR alignment

#### Aligning Together and Splitting
First we construct a tab delimited file matching the sequence to the cell barcode (in our case GEO session number).
```bash
ls fastq/*.fastq | cut -f 2 -d '/' | cut -f 1 -d '.' | while read line 
do 
        # STAR requires 3 columns, second should be "-" in single-end sequencing.
        echo -e "fastq/${line}.fastq\t-\t${line}" 
done > manifest.tsv
```
Then we align the sequences to the genome using the `--readFilesManifest` option in STAR. Also we specified the sequencing method with `--soloType SmartSeq`.
```bash
# Submitted as ll_star_02.txt
STAR --runThreadN 25 \
        --genomeDir /data/bio-zhanglm/genome/mm10 \
        --readFilesManifest manifest.tsv \
        --outFileNamePrefix ./mapping/split/chromaffin. \
        --outSAMtype BAM SortedByCoordinate \
        --quantMode GeneCounts \
        --soloType SmartSeq \
        --soloUMIdedup Exact NoDedup \
        --outSAMattributes NH HI AS nM RG
```


STARsolo's github page said that: 
> Cell-id can be any string without spaces. Cell-id will be added as ReadGroup tag (RG:Z:) for each read in the SAM/BAM output. If Cell-id starts with ID:, it can contain several fields separated by tab, and all the fields will be copied verbatim into SAM @RG header line.

Thus we might try to split the BAM file into multiple BAM files based on the cell barcode with `samtools split`, which by default separate with the `@RG` header. 

```bash
# at /scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin/mapping/split/split_out
samtools split -f %#_%*.%. ../chromaffin.Aligned.sortedByCoord.out.bam
```

In order for the Bam file output by STAR to have the `@RG` tag, we need to add one line of command when doing the alignmnet. The last line `--outSAMattributes NH HI AS nM RG` is required for the each read in the Bam file to contain the @RG tag.

It worked and the overall time for the jobs are:
- Alignment: 30 minutes.
- Splitting: 30 minutes.

The output files are stored in `/scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin/mapping/split/split_out`.

#### Aligning One-by-one 
This probably will work just fine, but it will take a long time. With this method, you can't use the soloType command since we are not using `starsolo`, but only the regular `STAR`.
```bash 
# Submitted as ll_star_01.txt
ls fastq/*.fastq | cut -f 2 -d '/' | cut -f 1 -d '.' | while read line 
do 
        STAR --runThreadN 25 \ 
                --genomeDir /data/bio-zhanglm/genome/mm10 \
                --readFilesIn fastq/${line}.fastq \
                --outFileNamePrefix mapping/${line} \ 
                --outSAMtype BAM SortedByCoordinate \
                --quantMode GeneCounts \
done
```
The job process took around 6 hours.

### Velocyto Analysis 
We first performed the velocyto analysis on the one-by-one aligned BAM files. 

#### Preperation 
Before we start to do the analysis, `velocyto` analysis for the SmartSeq2 data requires two additional files. 
1. The gene annotation file in GTF format `Mus_musculus.GRCm39.111.gtf`.
2. The repeat masker file `mm10_rmsk.gtf`, .
All could be found in `/data/bio-zhanglm/genome/mm10/` directory.

#### Analysis 
##### One-by-one output BAMs
```bash
mask=/data/bio-zhanglm/genome/mm10/mm10_rmsk.gtf
annotation=/data/bio-zhanglm/genome/mm10/Mus_musculus.GRCm39.111.gtf

velocyto run-smartseq2 -o velocyto -m $mask -e chromaffin mapping/*.bam $annotation 
```
Which sadly resulted in the error: 
```
Traceback (most recent call last):
  File "/work/bio-zhanglm/conda/envs/pre/bin/velocyto", line 8, in <module>
    sys.exit(cli())
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/velocyto/commands/run_smartseq2.py", line 70, in run_smartseq2
    return _run(bamfile=bamfiles, gtffile=gtffile, bcfile=None, outputfolder=outputfolder,
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/velocyto/commands/_run.py", line 196, in _run
    mask_ivls_by_chromstrand = exincounter.read_repeats(repmask)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/velocyto/counter.py", line 347, in read_repeats
    gtf_lines = sorted(gtf_lines, key=sorting_key)
  File "/work/bio-zhanglm/conda/envs/pre/lib/python3.8/site-packages/velocyto/counter.py", line 345, in sorting_key
    return (x[0], x[6] == "+", int(x[3]), entry)  # The last element of the touple corresponds to the `last resort comparison`
IndexError: list index out of range
```
##### Squashed BAMs
```bash
cd /scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin

mask=/data/bio-zhanglm/genome/mm10/mm10_rmsk.gtf
annotation=/data/bio-zhanglm/genome/mm10/Mus_musculus.GRCm39.111.gtf
bam=/scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin/mapping/split/split_out


velocyto run-smartseq2 -o velocyto -m $mask -e chromaffin ${bam}/*.bam $annotation
```
Which outputs the same error as above.

## Hippocampus 

Since the SmartSeq2 chromaffin data didn't work, we wanted to try the 10x Genomics data of hippocampus to see if we can reproduce their results.

SmartSeq2 might not be that popular, so there aren't many solutions in the GitHub issue page, but I found a lot of people asking and answering 10x related questions.

In the directory `/scratch/2024-05-11/bio-zhanglm/bioinfo/hippocampus`.

However, this dataset seems to be too large, I've been downloading it via the command `geofetch -i GSE104323` for over 3 days now, and it seems to be still downloading. I give up.

## Starting from Aligned Bam files 

We found some pre-aligned Bam files by P.Kharchenko's lab deposited at `http://pklab.med.harvard.edu/velocyto/notebooks/R/chromaffin2.nb.html` which is great news. We can now compare the difference between our aligned Bam files and theirs.

### Downloading new Bam files
We just download and extract it with the following commands:
```bash
wget http://pklab.med.harvard.edu/velocyto/chromaffin/bams.tar
tar xvf bams.tar
```
Resulting in the following files:
```
e12.5.bams/
|-- A1
|   `-- A1_unique.bam
|-- A10
|   `-- A10_unique.bam
|-- A11
|   `-- A11_unique.bam
|-- A12
|   `-- A12_unique.bam
|-- A13
|   `-- A13_unique.bam
.
.
.
```

## Analysis of Velocyto

### Obtaining the `.loom` Files
We then try to run velocyto on this public dataset to see if it works. This time, we followed the instructions from [Kharchenko's Lab](http://pklab.med.harvard.edu/velocyto/notebooks/R/chromaffin2.nb.html) and removed the mask field `-m` from the command.
```bash
velocyto run-smartseq2 -o velocyto ${bam}/*/*.bam $annotation
```
Suprisingly, it worked! The output files are stored as `/scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin/public_bam/velocyto/onefilepercell_A10_unique_and_others_1N5XB.loom`. 

Thus, we removed the `-m` field from the command for our own Bam files, and it worked as well. Seems that there is a problem with the mask data, which is reasonable since the Bam files have similar structure. The codes are shown beneath.
```bash
cd /scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin

mask=/data/bio-zhanglm/genome/mm10/mm10_rmsk.gtf # something wrong
annotation=/data/bio-zhanglm/genome/mm10/Mus_musculus.GRCm39.111.gtf
bam=/scratch/2024-05-11/bio-zhanglm/bioinfo/chromaffin/mapping/split/split_out

velocyto run-smartseq2 -o velocyto -e chromaffin ${bam}/*.bam $annotation
```
The output from our own Bam files are stored as `.../bioinfo/chromaffin/velocyto/chromaffin_split.loom`.

The `.loom` files are binary, so we don't know what's the structure like. But we know that it contains information linking UMI to splicing information. This can be accessed with the `velocyto` package.

### Analysis with R and Python

#### R
First, we need to install the required packages from the github [`velocyto.R` Repository](https://github.com/velocyto-team/velocyto.R?tab=readme-ov-file) by using the following command:
```R
devtools::install_github("velocyto-team/velocyto.R")
```
R output the following error:
```R
ERROR: dependency ‘pcaMethods’ is not available for package ‘velocyto.R’
* removing ‘/Library/Frameworks/R.framework/Versions/4.3-arm64/Resources/library/velocyto.R’
Warning message:
In i.p(...) :
  installation of package ‘/var/folders/ck/9dvycsw50dz1r928cgvks0tr0000gn/T//RtmpqeuAwC/file22d973751c84/velocyto.R_0.6.tar.gz’ had non-zero exit status
```

#### Huge Problem
`velocyto` don't support arm64 architecture, and sadly I'm using a m1 pro chip. This will not work at all.

### Analysis with scVelo
When researching the follow-up works of velocyto, I found a new analysis pipeline named scVelo. Which is the counterpart of velocyto in scanpy. It assumed different splicing rates for different genes, so the model is slightly different from the original velocyto model. The analysis pipeline and results can be found in the github repository for this project.