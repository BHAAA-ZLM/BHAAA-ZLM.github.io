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
- <span style="font-family: Courier"> <https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp>

<span style="font-family: Courier">SAM/BAM/CRAM:

- <span style="font-family: Courier"> <https://samtools.github.io/hts-specs/SAMv1.pdf>

<span style="font-family: Courier">GFF/GTF:

- <span style="font-family: Courier"> <https://useast.ensembl.org/info/website/upload/gff.html>
- <span style="font-family: Courier"> <https://en.wikipedia.org/wiki/Gene_transfer_format>


<span style="font-family: Courier"> Unix

- <span style="font-family: Courier"> <http://korflab.ucdavis.edu/Unix_and_Perl/current.html>


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

### <span style="font-family: Courier">FASTA

<span style="font-family: Courier">FASTA format is a basic format for repoting a sequence whether it's a nucleic acid or amino acid. Made up by two parts:

- <span style="font-family: Courier">A sequence header which starts with a '>' and contaisn the sequence description.
- <span style="font-family: Courier">The sequence itself (containing no space within).

        >P01013 GENE X PROTEIN (OVALBUMIN-RELATED)
		QIKDLLVSSSTDLDTTLVLVNAIYFKGMWKTAFNAEDTREMPFHVTKQESKPVQMMCMNNSFNVATLPAE
		KMKILELPFASGDLSMLVLLPDEVSDLERIEKTINFEKLTEWTNPNTMEKRRVKVYLPQMKIEEKYNLTS
		VLMALGMTDLFIPSANLTGISSAESLKISQAVHGAFMELSEDGIEMAGSTGVIEDIKHSPESEQFRADHP
		FLFLIKHNPTNTIVYFGRYWSP




## <span style="font-family: Courier">SAM/BAM/CRAM Format

### <span style="font-family: Courier">**SAM**

<span style="font-family: Courier">The Sequence Alignment/Map (SAM) format is the most basic and most human readable format of the three. It consists of a header, and a row for every read in your dataset, and 11 tab-delimited fields describing that read.

#### <span style="font-family: Courier">**SAM Header**

<span style="font-family: Courier">The SAM header varies in size, but header lines start with '@', while alignment lines do not. You can customize the header when you generate the SAM file, add the information you decided to add. The full list of header fields are found below. '*' means that this tag is required; e.g., every `@SQ` header line must contain `SN` and `LN` fields.

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-4.47.54-PM.png" width=600 title="SAM header fields" alt="SAM header fields">

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-4.51.29-PM.png" width=600 title="SAM header fields" alt="SAM header fields">

#### <span style="font-family: Courier">**Fields Descriptions**

<span style="font-family: Courier">Every row contains 11 mandatory fields, which are: 

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-4.35.57-PM.png" width=600 title="Fields Descriptions" alt="Fields Descriptions">

<span style="font-family: Courier">
**Bitwise Flag** is a lookup code to explain certain features about the particular read (exact same concept as Linux permission codes!). It tells you whether the read aligned, is marked a PCR duplicate, if it’s mate aligned, etc. and any combination of the available tags, seen below:

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-4.42.16-PM.png" width=600 title="Bitwise Flag" alt="Bitwise Flag">

<span style="font-family: Courier">Sometimes it might be a bit hard to explain the integers of the Bitwise Flag, you can go on [Picard](https://broadinstitute.github.io/picard/explain-flags.html) to get a quick analysis.

<span style="font-family: Courier">
**Map Q** (Mapping Quality) reveals how well the read are aligned to the reference. Different algorithm might lead to different scores, but generally, the greater the number, the better the alignment.

<span style="font-family: Courier">
**CIGAR String** is a special string that can tell you the alignment information of the whole sequence.

<img src="../CIGAR_String.png" width=600 title="CIGAR" alt="CIGAR">

<img src="https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/Screen-Shot-2018-01-07-at-5.02.26-PM.png" title="CIGAR example" alt="CIGAR example" width=600>


### <span style="font-family: Courier">**BAM**

<span style="font-family: Courier">
BAM format has literally the same content as the SAM file, except it's in **B**inary format. Thus it's not legible to human but is smaller and faster to read for a computer.

<span style="font-family: Courier">
Tools like [Samtools](http://www.htslib.org), [Picard Tools](http://broadinstitute.github.io/picard/) and [IGV](http://software.broadinstitute.org/software/igv/) are required to make sence of BAM files.

### <span style="font-family: Courier">**CRAM**

<span style="font-family: Courier">
This is a relatively new format that is very similar to BAM as it also retains the same information as SAM and is compressed, but it is much smarter in the way that it stores the information. It’s very interesting and up and coming but is a bit beyond my level and not so relative to RNA-seq. To learn more about it, you can read [this](https://samtools.github.io/hts-specs/CRAMv3.pdf).

## <span style="font-family: Courier">VCF Format

<span style="font-family: Courier">
Variant calling format is a tab-delimited text file (different from Virtual Card Format), it is used to describe single nucleotide variants (SNVs) as well as insertions, deletions and other sequence variations. It is limited to only show the variations not the genetic features.

- <span style="font-family: Courier">Chromosome Name
- <span style="font-family: Courier">Chromosome Position
- <span style="font-family: Courier">ID

    > <span style="font-family: Courier">This is generally used to reference an annotated variant in dbSNP or other curate variant database.

- <span style="font-family: Courier">Reference base(s)
- <span style="font-family: Courier">Alternate base(s)
- <span style="font-family: Courier">Variant quality

    > <span style="font-family: Courier"> [Phred-scaled quality](https://gatk.broadinstitute.org/hc/en-us/articles/360035531872-Phred-scaled-quality-scores) for the alternate base. Usually, a >20 score is acceptable.

- <span style="font-family: Courier">Filter

    > <span style="font-family: Courier">Whether or not this has passed all filters – generally a QC measure in variant calling algorithms

- <span style="font-family: Courier">Additional Information

    > <span style="font-family: Courier">This is for additional information, generally describing the nature of the position/variants with respect to other data.

<span style="font-family: Courier">
For example vcf files, look at your own files during the class BIOS201, Genome, why are we different.

## <span style="font-family: Courier">GFF and GTF

<span style="font-family: Courier">
Gene transfer format (GTF) and General feaure format (GFF) are kinds of file format used to hold information about gene structure.

<span style="font-family: Courier"> <https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md>

## <span style="font-family: Courier">BED

<span style="font-family: Courier"> The formal bed format description can be found [here](https://genome.ucsc.edu/FAQ/FAQformat.html#format1).

<span style="font-family: Courier"> In shorter words, BED files allows an easy way to define the things you want to show in your track annotation (like a reference genome).

## <span style="font-family: Courier"> Bed Graph

<span style="font-family: Courier"> The detailed discription for bed graph is [here](http://genome.ucsc.edu/goldenPath/help/bedgraph.html), I think this file can be used to store the reads for each small sets of nucleotide on your chromosome after your sequencing.

## <span style="font-family: Courier"> BigWig

<span style="font-family: Courier"> The BigWig files indicates the reads on a certain position. You can view it with igv, but also other applications and can turn it into a very beautiful graph. Requires further inquiry. The official BigWig file explaination can be found [here](http://genome.ucsc.edu/goldenPath/help/bigWig.html).