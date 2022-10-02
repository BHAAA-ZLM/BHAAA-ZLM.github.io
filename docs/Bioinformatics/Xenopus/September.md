---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 30min 
publish_date: 2022.09.28
---

## <span style="font-family: Courier"> Motif analysis
<span style="font-family: Courier"> September 23rd, got my first ever project from Prof.Chen Wei. The first important step should be motif analysis. (my actual work-list is [here](https://bottlenose-stilton-cc3.notion.site/Co-occurrence-for-Luming-108a4aac2b2844bcb0b40961d8bffa6f))

<span style="font-family: Courier"> To summarize, finding the linkage between two TF proteins which regulates gene expression is what we should do. By finding the linkage between the motifs of proteins in the promoter zone of the gene, we can hypothesis that some of the proteins have interactions with each other.

### <span style="font-family: Courier"> Pipelines

#### <span style="font-family: Courier"> Preparing raw materials
<span style="font-family: Courier"> Several raw materials are needed for this analysis. Including:
- <span style="font-family: Courier"> The motif files of the TF proteins we are interested in.
- <span style="font-family: Courier"> Classify the ATAC-seq peaks and filter the non-promoter ones.
- <span style="font-family: Courier"> Getting the sequence for the filtered peaks.

<span style="font-family: Courier"> The motif files of the TF proteins are fairly easy to obtain. Go to [JASPR database](https://jaspar.genereg.net) and download the motifs you need. You can download multiple motifs in one text file by adding them to the cart.

<span style="font-family: Courier"> Classifying the ATAC-seq files need some Linux skills (which sadly I don't have) and we also need [Homer](http://homer.ucsd.edu/homer/). First, we have to classify our own unique genome. Because we are using frogs, which are not very common, Homer requires us to build our own reference genome, which can be easily done following the guidelines [here](http://homer.ucsd.edu/homer/introduction/update.html). This procedure requires the FASTA file for the genome and the gtf file for the genome annotation.

```bash
loadGenome.pl -name XenTr10 -fasta Xentr10.repeatMasked.fasta -gtf Xentr10.0.gene.chr.gtf -org xenopus
```

<span style="font-family: Courier"> After loading our own genome into Homer, we can classify the peaks we get from our normal ATAC-seq pipeline.

```bash
annotatePeaks.pl st9-2_peaks.narrowPeak XenTr10 > st9-2-annotated.txt
```

<img src="http://homer.ucsd.edu/homer/ngs/annotation.example.png" width=600>

<span style="font-family: Courier"> Within the text file, there are peaks that are classified as intron, intergenic, promoter etc. We need to filter out the ones containing promoters. So this is where the powerful [awk](https://www.geeksforgeeks.org/awk-command-unixlinux-examples/) comes.
```bash
awk '/promoter/ {print}'  st9-2-annotated.txt > st9-2-promoter.txt
```
<span style="font-family: Courier"> This simple command can filter out all the lines containing promoter into a new file. We also need to convert the new text file into bed format by cutting out some of the important lines (you can use awk for this as well).
```bash
cut -f 2,3,4,16 XXX.txt >XXX.bed
```
<span style="font-family: Courier"> Thus we can get a bed format file that contains only the promoter peaks from the ATAC-seq peaks.

<span style="font-family: Courier"> At last, we get our filtered peaks and map them back to the genome, thus obtaining their sequence. Using **[bedtools](https://bedtools.readthedocs.io/en/latest/content/tools/getfasta.html)** we can finish these steps very quickly. 
```bash
bedtools getfasta -fi Xentr10.repeatMasked.fasta -bed xxx.bed -fo output.fa -name
```

#### <span style="font-family: Courier"> Finding the motifs
<span style="font-family: Courier"> After we got our wanted sequence of all the promoters of the ATAC-seq peaks, we would like to see where are the motifs of the two TF proteins located, if at all, in these promoter sequences. Do they really activate the gene expression? Or that they are not bound to these sites. We use [fimo](https://meme-suite.org/meme/doc/fimo.html) from [meme](https://meme-suite.org/meme/) to match the motifs with our sequence.
```bash
fimo --o dir/fimo OTX1.meme st9-2-promoter-gene.fa
```
<span style="font-family: Courier"> Thus you get all the matches of the motif and your sequence.