---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 40min
publish_date: 2022.07.22
---

<span style="font-family: Courier"> 
In this Article, you can learn about the tools in RNA-Seq. The articles come from these websites:

<span style="font-family: Courier"> 
General (with huge thanks to Wen Yi):

- <span style="font-family: Courier"> <https://github.com/Blairewen/Arabidopsis-Pollen> Remember to star her repository too if you visit Wen Yi's repo.

<span style="font-family: Courier"> 
FASTQC

- <span style="font-family: Courier"> <https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/>

---

## <span style="font-family: Courier"> FastQC

<span style="font-family: Courier"> 
FastQC is for the quality control of the raw data from sequencing. It's best to check that the data are good before you do anything further.

<span style="font-family: Courier"> 
You can use the user interface friendly FastQC java swing application. But when you are processing multiple files, you can use the terminal command `fastqc` in such a way that you cna process multiple files at the same time.

```
 fastqc [-o output dir] [--(no)extract] [-f fastq|bam|sam] [-c contaminant file] seqfile1 .. seqfileN
```

<span style="font-family: Courier"> Remember to switch your shell to bash when you execute this command. I don't actually know the alternative command for zsh, but there must be some kind of command.

## <span style="font-family: Courier"> MultiQC

<span style="font-family: Courier"> However, sometimes we have a lot of test data, and we don't actually have the time to check the HTML output of the FastQC for each and every file. Thus, we can use MultiQC.

```
multiqc /raw_data_dir
```

<span style="font-family: Courier"> Will auto generate a 4 in 1 html report.

## <span style="font-family: Courier"> Trimmomatic

<span style="font-family: Courier"> Installing trimmomatic is a very tricky thing to do on a M1 chip mac. I followed this [instruction](https://datacarpentry.org/genomics-workshop/setup.html#macos-2) to get it finally done.

<span style="font-family: Courier"> <http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf>

## <span style="font-family: Courier"> fastp

<span style="font-family: Courier"> Basically fastp is just a all in one quality check machine. It can perform quality check and trim the data at the same time.

```
fastp -i Spm_R1.fastq.gz -I Spm_R2.fastq.gz -o Spm_R1.fastp.fastq.gz -O Spm_R2.fastp.fastq.gz -w 8 -q 20 –u 20 -j Spm.fastp.json -h Spm.fastp.html
```

<span style="font-family: Courier"> Here is the code for fastp.

- <span style="font-family: Courier"> -i, --in1 is the input file name of read1
- <span style="font-family: Courier"> -I, --in2 is the input file name of read2
- <span style="font-family: Courier"> -o, --out1 is the output file name of read1
- <span style="font-family: Courier"> -O, --out2 is the output file name of read2

<span style="font-family: Courier"> There are some other commands regarding whether to discard one of the pair end read or not, which can bee found by typing `fastp -help`.

- <span style="font-family: Courier"> -w, --thread means the thread number, default thread # is 2
- <span style="font-family: Courier"> -q, --qualified_quality_phred the quality phred value that a base is qualified. Default is 15, meaning that >=Q15 is qualified.
- <span style="font-family: Courier"> -u, --unqualified_percent_limit how many percents of bases are allowed to be unqualified (0~100). Default 40 means 40%.
- <span style="font-family: Courier"> -g force polyG tail trimmingmby default trimming is automatically enabled for Illumina data.

<span style="font-family: Courier"> And their are the commands that controls the outputs.

- <span style="font-family: Courier"> -j, --json the json format report file name (string [=fastp.json])
- <span style="font-family: Courier"> -h, --html the html format report file name (string [=fastp.html])

> <span style="font-family: Courier"> To download files from the server, use the scp command which works like this:

> <span style="font-family: Courier"> `scp username@sth.sth.sth.sth:/file/path/on/server.html /Local/path/to/store/file`

> <span style="font-family: Courier"> Remember not to add any extra space between.

## <span style="font-family: Courier"> HISAT2

<span style="font-family: Courier"> The HISAT2 official website can be found [here](http://daehwankimlab.github.io/hisat2/manual/). It is a fast and sensitive alignment program for mapping next-generation sequencing reads.

```
hisat2 -p 8 -x tair10_index --summary-file Spm.summary --dta-cufflinks -1 Spm_R1.fastp.cutadapt.fastq.gz -2 Spm_R2.fastp.cutadapt.fastq.gz -S output.sam
```

<span style="font-family: Courier"> The basic usage of HISAT2 is:
```
hisat2 [options]* -x <ht2-idx> {-1 <m1> -2 <m2> | -U <r> | --sra-acc <SRA accession number>} [-S <sam>]

  <ht2-idx>  Index filename prefix (minus trailing .X.ht2).
  <m1>       Files with #1 mates, paired with files in <m2>.
             Could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
  <m2>       Files with #2 mates, paired with files in <m1>.
             Could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
  <r>        Files with unpaired reads.
             Could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
  <SRA accession number>        Comma-separated list of SRA accession numbers, e.g. --sra-acc SRR353653,SRR353654.
  <sam>      File for SAM output (default: stdout)

  <m1>, <m2>, <r> can be comma-separated lists (no whitespace) and can be
  specified many times.  E.g. '-U file1.fq,file2.fq -U file3.fq'.
```

<span style="font-family: Courier"> The interesting commands for HISAT2 are the following:

- <span style="font-family: Courier"> -p, --threads (int) means the number of threads you launch. Default is 1.
- <span style="font-family: Courier"> --summary-file print the alignment summary to this file.
- <span style="font-family: Courier"> --dta-cufflinks reprots alignments tailored specifically for [cufflinks](http://cole-trapnell-lab.github.io/cufflinks/).

## <span style="font-family: Courier"> samtools

<span style="font-family: Courier"> Samtools is a tool to handle sam, bam and cram files.

```
samtools view -ShuF 4 -q 30 -f 2 -@ 2 file.name.sam | samtools sort -@ 2 -o output/file.bam 

samtools view [options] <in.bam>|<in.sam>|<in.cram> [region ...]
```

<span style="font-family: Courier"> `samtools view `is for viewing the bam/sam/cram file in bam/sam/cram type.

- <span style="font-family: Courier"> -S Ignored (the input format is auto-detected).
- <span style="font-family: Courier"> -h,--with-header Include header in the SAM output.
- <span style="font-family: Courier"> -u,--uncompressed Uncompressed BAM output (and default to --bam).
- <span style="font-family: Courier"> -F FLAG Have none of the [FLAGs](https://www.samformat.info/sam-format-flag).
- <span style="font-family: Courier"> -q int Have mapping quality >= int.
- <span style="font-family: Courier"> -f FLAG Have all of the flags present.
- <span style="font-family: Courier"> -@ int The number of threads. 

<span style="font-family: Courier"> `samtools sort` is sorting the data by your need.

-<span style="font-family: Courier"> -u Set the compression level to 0 (uncompressed).

<span style="font-family: Courier"> When you want to see your gene inside for insatance igv, you will also need to index your bam files.

## <span style="font-family: Courier"> featureCounts
<span style="font-family: Courier"> FeatureCounts is a tool to quantify the counts on genes based on the bam file. A link to a desctiption of featureCounts is [here](https://rnnh.github.io/bioinfo-notebook/docs/featureCounts.html).
```
featureCounts [options] -a <annotation_file> -o <output_file> input_file1 [input_file2] ... 
```

<span style="font-family: Courier"> After using featureCounts, you can use your command line tools:
```
cut -f1,7,...
```
<span style="font-family: Courier"> To cut the columns you need.


## <span style="font-family: Courier"> bedtools

```
genomeCoverageBed -ibam Spm.sorted.bam -bg -split > Spm.bdg
```
- <span style="font-family: Courier"> -ibam input bam files for coverage. Use `stdin` or `-` for a Unix pipe.

## <span style="font-family: Courier"> cuffdiff

<span style="font-family: Courier">  Cuffdiff is a program included in cufflinks. You can use this program to find significant changes in transcript expression. Use `cuffdiff -h` to look for the manual.

> <span style="font-family: Courier"> When cuffdiff give you all 0 counts, there might be something wierd with your sam file. The name of the chromosome might be named wrong. Instead of naming them 'chrN' they are just named with 'N'.

## <span style="font-family: Courier"> At Last ... DEseq2

<span style="font-family: Courier"> I think DEseq2 might need a seperate article.

## <span style="font-family: Courier"> Others

<span style="font-family: Courier"> To communicate with the server using `scp` command, see [here](https://stackoverflow.com/questions/16886179/scp-or-sftp-copy-multiple-files-with-single-command) for more info.
