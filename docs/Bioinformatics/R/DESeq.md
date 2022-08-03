---

author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 30min
publish_date: 2022.8.3

---


<span style="font-family: Courier"> DESeq2 is a very special R package made for performing differential expression analysis on your sequence, especially when you are tring to define differences between multiple biological conditions (e.g. treated, untreated).
 
<span style="font-family: Courier">  Most of my overall knowledge comes from surfing the internet, and I found:

- <span style="font-family: Courier"> A [wonderful girl](https://www.youtube.com/watch?v=OzNzO8qwwp0&t=226s) teaching DESeq2. Her channel is so rich in knowledge, everyone, subscribe now!!!

- <span style="font-family: Courier"> The original [manual](http://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html#countmat) for DESeq2.

- <span style="font-family: Courier"> Another DESeq2 [tutorial](https://lashlock.github.io/compbio/R_presentation.html) made very thoroughly and clear, I love it!

- <span style="font-family: Courier"> The DESeq2 [tutorial](https://genviz.org/module-04-expression/0004/02/01/DifferentialExpression/) made by Griffith lab of Washington University. Which is surprisingly detailed when it comes to plotting.

## <span style="font-family: Courier"> The Basic Workflow of DESeq2

<span style="font-family: Courier">  In our RNA-seq workflow, we used cuffdiff to get a general differential expression result, from it, you can easily see which genes are expressed more, which are suppressed, in other words, which genes have a significant count difference from the other genes.

<span style="font-family: Courier"> But when we come to the real biological experiments and analysis, we usually want to know more about our gene and about our test subjects. We might even want to draw fancy pictures to convey our ideas. That's when our rather old tool cuffdiff doesn't shine. 

<span style="font-family: Courier"> DESeq2 basically work nearly the same as cuffdiff (although the algorithms might be a bit different), but the final result we are looking for are bascially the same. The log2(foldchanges) and p_values and all those things. So how does it work?

### <span style="font-family: Courier"> Getting the Matrix

<span style="font-family: Courier"> First we need the count matrix from our data. We need an old friend from our RNA-seq workflow - featureCounts. 

```
featureCounts [options] -a <annotation_file> -o <output_file> input_file1 [input_file2] ... 
```

<span style="font-family: Courier"> By typing this command into the terminal, feature counts will automatically map all the counts to the genes in your annotation file. Thus providing you with a matrix of counts for specific genes. We only need the counts for each matrix, so we can cut the matrix in the command line or in R. We might also want to remove some data with very low counts, since they are not very significant, and we can do that also in the command line or in R.

### <span style="font-family: Courier"> Input the Matrix into R

<span style="font-family: Courier"> The next step is to get your matrix into R and prepare it for DESeq2. The code I used was this, and I found it pretty elegant.

```R
# input data 
input_data <- read.table("deseq2_input.txt",header = T, row.names = 1)


# preperation 
input_data <- as.matrix(input_data)
condition <- factor(c(rep("ctrl",4), rep("DDX6KO",4)))
coldata <- data.frame(row.names = colnames(input_data),condition)
```

<span style="font-family: Courier"> First we input the data into the variable input_data by the R function read.table(). You can always get help in R by just typing `?functionName()` in the R console. So in the read.table() function, we set the first row as our header with `header = T`. `row.names = 1` indicates that the first column of each row gives the name of the first row.

<span style="font-family: Courier"> Then, we prepare the raw data so that it fits the requirements of DESeq2. Apart from the original data matrix from your sequencing results, DESeq2 also requires another matrix containing informations on the columns of our data (in other words, the names and types of your contol and experiment groups). So the `as.matrix` turns the data into a matrix fit for calculation. `condition` stores a factor of two (it can be more than two). `coldata <- data.frame()` gives DESeq2 the column data it needs.

### <span style="font-family: Courier"> Construct the DESeq Dataset

<span style="font-family: Courier"> Then we use our data to construct a DESeq Dataset from our matrix (in this case, `input_data`).

```R
library(DESeq2)
# construct a deseq input data matrix
dds <- DESeqDataSetFromMatrix(countData = input_data, colData = coldata, design = ~condition)

dim(dds)
dim(dds[rowSums(counts(dds)) > 5,])
dds <- dds[rowSums(counts(dds)) > 5,]
```
<span style="font-family: Courier"> We first need to import the DESeq2 library (package) (of course). 

<span style="font-family: Courier"> Then, we use the function `DESeqDataSetFromMatrix()` from DESeq2 package to input our raw data. `colData` is the matrix we made earlier containing the data for row names and types and all those stuff. `design = ~condtion` means that the data is designed by the factor `condition` in the `colData` variable. In designed, I mean that the DESeq process will perform the differential expression analysis based on the different conditions of the experiments. The conditions are also set manually. You can add another column in the `colData` matrix called `time`, and set the design to `design = ~condition + time`, DESeq will restrain the effects of condition and focus on the time factor. For more information, see [this blog](https://www.biostars.org/p/278684/) on BioStars.

<span style="font-family: Courier">  We can check the dimensions of dds using `dim(dds)`. We could remove the results when the gene's counts are less than 5 in total, by reassigning the value of dds to `dds[rowSums(counts(dds)) > 5,]`. Thus we got our DESeq Dataset, named `dds`, and we can happily perform differential expression analysis on it!~