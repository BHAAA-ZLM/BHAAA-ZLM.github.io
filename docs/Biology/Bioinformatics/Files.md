---

author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 30min
publish_date: 2022.7.20

---

<span style="font-family: Courier">Here, I learnt about all the different files that may come up during a NGS analysis. All the knowledge comes from:

<span style="font-family: Courier">General:

- <span style="font-family: Courier"> <https://learn.gencore.bio.nyu.edu> A very 
useful website teaching about NGS analysis.

<span style="font-family: Courier">FASTA & FASTQ:

- <span style="font-family: Courier"> <https://support.illumina.com/bulletins/2016/04/fastq-files-explained.html>
- <span style="font-family: Courier"> <http://www.biotrainee.com/thread-2703-1-2.html>

## <span style="font-family: Courier">FASTQ and FASTA

<span style="font-family: Courier">The first section is about FASTQ and FASTA files.

### <span style="font-family: Courier">FASTQ

<span style="font-family: Courier">
FASTQ files contains four lines including:

1. <span style="font-family: Courier">The sequence Identifier with information about the sequencing run and the cluster.
1. <span style="font-family: Courier">The sequence read.
1. <span style="font-family: Courier">A separator, which is simply a plus (+) sign, but sometimes might also be a (-) sign.
1. <span style="font-family: Courier">The quality scores. Using ASCII characters to represent the numerical quality of the scores.

<img src="https://supportassets.illumina.com/content/dam/illumina-support/images/bulletins/11/fastq_files_explained_image.png" width=600 title="sample fastq file" alt="sample fastq file">

#### <span style="font-family: Courier">Quality Scores

<span style="font-family: Courier">
[Quality scores](https://learn.gencore.bio.nyu.edu/ngs-file-formats/quality-scores/) are a way to assign confidence to a particular base within a read. The code is related to the ASCII table and each letter is related to a different Q score.

<span style="font-family: Courier">
The quality score Q is related to the probability of incorrect corresponding base call.

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-1.36.09-PM-1024x713.png" width=600 title="Quality value Q" alt="Quality value Q">

<span style="font-family: Courier">
By matching the ASCII table characters to their Q code under certain protocals, we can easily (?) know the quality of the specific gene.

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-1.34.33-PM-1024x656.png" title="ASCII to Q to P" alt="ASCII to Q to P">