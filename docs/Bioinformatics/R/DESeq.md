---

author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 1hour
publish_date: 2022.8.3

---


<span style="font-family: Courier"> DESeq2 is a very special R package made for performing differential expression analysis on your sequence, especially when you are tring to define differences between multiple biological conditions (e.g. treated, untreated).
 
<span style="font-family: Courier">  Most of my overall knowledge comes from surfing the internet, and I found:

- <span style="font-family: Courier"> A [wonderful girl](https://www.youtube.com/watch?v=OzNzO8qwwp0&t=226s) teaching DESeq2. Her channel is so rich in knowledge, everyone, subscribe now!!!

- <span style="font-family: Courier"> The original [manual](http://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html#countmat) for DESeq2.

- <span style="font-family: Courier"> Another DESeq2 [tutorial](https://lashlock.github.io/compbio/R_presentation.html) made very thoroughly and clear, I love it!

- <span style="font-family: Courier"> The DESeq2 [tutorial](https://genviz.org/module-04-expression/0004/02/01/DifferentialExpression/) made by Griffith lab of Washington University. Which is surprisingly detailed when it comes to plotting.

## <span style="font-family: Courier"> Getting Ready for DESeq2

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

### <span style="font-family: Courier"> Finally, the DESeq analysis

<span style="font-family: Courier"> The actual analysis part is really easy to understand, and doesn't require a lot of code of brain.

```R
# perform the differential expression analysis
dds <- DESeq(dds)
res <- results(dds)
```

<span style="font-family: Courier"> Just type these words and everything will be done in the background thanks to our lovely DESeq2 developers. The deeper truth behind all the analysis is much more complex, and I don't think I fully understand it. I will leave a link here to the [lovely Indian girl's video](https://www.youtube.com/watch?v=0b24mpzM_5M), and I might make another whole chapter just talking about how it works. But for us who are just using it and only cares about the final output data, these two lines of code is enough.

## <span style="font-family: Courier"> Plot Your Data

<span style="font-family: Courier"> After we obtained our data from DESeq, we need to know how to show everyone else in a clear and fasionable way, what is happening in our experiments. That's where our beautiful plots come. A wide variaty of plots can be used to express our data, and it's best if we know how to draw each one of them, and more importantly, the essence behind every plot.

<span style="font-family: Courier"> The knowledge of the plotting part mainly comes from the Griffith lab website, which is [here](https://genviz.org/module-04-expression/0004/02/01/DifferentialExpression/). There might be some websites helpful for individual plotting, I will list each of the websites in their own part.

### <span style="font-family: Courier"> The MA plot

<span style="font-family: Courier"> [MAplots](https://en.wikipedia.org/wiki/MA_plot) are plots that can display the difference of measurements between two sets of data.

<span style="font-family: Courier"> DESeq2 have it's own MAplotting function. Which is simply:
```R
plotMA(res, ylim = c(-3,3))
```

<img src="./plotMA.png" width=600 tab="MAplot from DESeq2" title="MAplot from DESeq2">

<span style="font-family: Courier"> But this MA plot only have two colours, and is rather lame. With ggplot's function geom_point, we could make a similar MA plot.

```R
library(ggplot2)
deseq2ResDF <- as.data.frame(res) ## convert the result file into a data frame
deseq2ResDF$significant <- ifelse(deseq2ResDF$padj < .1, "Significant", NA) ## a new column for significance

ggplot(deseq2ResDF, aes(baseMean, log2FoldChange, colour = padj)) + 
  geom_point(size=0.5) + scale_y_continuous(limits=c(-3, 3)) + 
  scale_x_log10() + geom_hline(yintercept = 0, colour="darkorchid4", size=1, linetype="longdash") + 
  labs(x="mean of normalized counts", y="log fold change") + 
  theme_bw() + geom_density_2d(colour="black", size=0.25) +
  scale_colour_gradient( high = "#f8ff2b", low = "#ff2b2b", space = "Lab", na.value = "grey50", guide = "colourbar", aesthetics = "colour")
```

<img src="./ggplotMA2.png" width=600 tab="MAplot from ggplot" title="MAplot from ggplot">

<span style="font-family: Courier">  By adding a series of constraints, we can make the geom_point look just like our MAplot. But first, we need to input our DESeq Data as a dataframe, and than add a new column called significant to the end of the dataframe. Remember to add `scale_x_log10` or else it will display the original counts, which are massive.

### <span style="font-family: Courier"> Heatmap

<span style="font-family: Courier"> Heatmaps are often used to show the difference between two groups of data, for example the experiment and the control. We can use the data we got from DESeq to plot a wonderful heatmap.

<img src="./ComplexHeatMap.png" width=600 tab="a complex heatmap" title="a complex heatmap">

<span style="font-family: Courier"> A fantastic heatmap tutorial can be found [here](https://www.youtube.com/watch?v=ht1r34-ifVI&list=PLi1VnGoeDGjvHvl83QySD2oAQYFHPRYso&index=8). 

```R
library(DESeq2)
library(ComplexHeatmap)
library(RColorBrewer)
library(circlize)
```

<span style="font-family: Courier"> Four libraries are used to draw this kind of heatmap. 

```R
dds_sig <- subset(deseq2ResDF, significant == "Significant")
dds_sig <- dds_sig[(dds_sig$baseMean > 50) & (abs(dds_sig$log2FoldChange) > 2),]
dds_sig <- dds_sig[order(dds_sig$log2FoldChange, decreasing = T),]  
```

<span style="font-family: Courier"> We first make a subset of our result matrix based on the significance (which comes from the padj number, usually padj <.1 can be considered significant). Then we filter this data by deleting the rows that have very small baseMean number (which means it's probably background noise), and choose those genes that have the largest foldchange (which are the most significant genes). Then we order our data so that the genes that have the largest change are at the first and last rows of the matrix.

```R
rlog_out <- rlog(dds, blind = F)
mat <- assay(rlog_out)[rownames(dds_sig),rownames(coldata)]
colnames(mat) <- rownames(coldata)
base_mean <- rowMeans(mat)
```

<span style="font-family: Courier"> Then we perform the rlog function on the DESeq Dataset to calculate the [Z-score](https://en.wikipedia.org/wiki/Standard_score) for the genes. Because the rlog_out is another dataset, we transform it into another matrix and set the column and row name of the matrix.

```R
mat_scaled <- t(apply(mat, 1, scale))
colnames(mat_scaled) <- colnames(mat)
```

<span style="font-family: Courier">  Then we [scale](https://en.wikipedia.org/wiki/Scaling_(geometry)) the matrix, which I guess is similar to the SVD decomposition, to get their influence factors on the difference. In our case, the scaling is more like normalizing the data of each row of mat, thus setting a global standard to express the difference between each group. Then set the names of our new matrix, and then we are done. 

```R
rows_keep <- c(seq(1:25), seq((nrow(mat_scaled) - 25), nrow(mat_scaled)))

l2_val <- as.matrix(dds_sig[rows_keep,]$log2FoldChange)
colnames(l2_val) <- "logFC"

mean_val <- as.matrix(dds_sig[rows_keep,]$baseMean)
colnames(mean_val) <- "AveExpr"
```

<span style="font-family: Courier"> Then we chose the 50 genes that have the largest and smallest foldchange to plot. We also want to plot their log2FoldChange value and baseMean value, so we extract them from the original sorted data (not from the normalized matrix).

```R
col_logFC <- colorRamp2(c(min(l2_val),0,max(l2_val)),c("blue","white","red"))
col_AveExpr <- colorRamp2(c(quantile(mean_val)[1], quantile(mean_val)[4]), c("white","red"))
```

<span style="font-family: Courier"> We set the colour for our log(FoldChange) and baseMean sub-heatmap so that it matches our main matrix.

```R
h1 <- Heatmap(mat_scaled[rows_keep,], cluster_columns = T, cluster_rows = F,
              column_labels = colnames(mat_scaled), name = "Z-score")

ha <- HeatmapAnnotation(summary = anno_summary(gp = gpar(fill = 2), height = unit(2, "cm")))
h2 <- Heatmap(l2_val, row_labels = rownames(dds_sig[rows_keep,]),
              cluster_rows = F, name = "LogFC", top_annotation = ha,
              col = col_logFC, 
              cell_fun = function(j, i, x, y, w, h, col){
                grid.text(round(l2_val[ i, j], 2), x, y)
              })

h3 <- ComplexHeatmap::Heatmap(mean_val, row_labels = rownames(dds_sig[rows_keep,]),
              cluster_rows = F, name = "AveExpr", 
              col = col_AveExpr, 
              cell_fun = function(j,i,x,y,w,h,col){
                grid.text(round(mean_val[ i, j], 2), x, y)
              })

h <- h1 + h2 + h3
h
```

<span style="font-family: Courier"> Then we finally plot the heatmap. `h1` is the main heatmap which demonstrates the expression difference of each gene in different group. `h2` and `ha` are bound together, `h2` shows the fold change of each individual gene, and `ha` is a small heatmap annotation showing the range of log(foldChange). At last `h3` is the baseMean value heatmap. We then combine all three graphs together, and get our final complex heatmap.