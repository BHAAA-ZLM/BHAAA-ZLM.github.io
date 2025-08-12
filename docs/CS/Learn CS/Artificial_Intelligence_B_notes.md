---
title: Notes from Artificial Intelligence B
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 
publish_date: 13.08.2025
---

The following notes are from SUSTech course "Artificial Intelligence B" taught in Fall 2023 by [Prof. Jianguo Zhang](https://faculty.sustech.edu.cn/?tagid=zhangjg&iscss=1&snapid=1&orderby=date&go=2&lang=en).

## Computer Vision

In the first half of the semester, we focused on computer vision.

### Describing Images

#### Pixels

Digital images are just samples version of a scene. Mathematically, it is described as a matrix of pixels, $\mathbf{I}$, in which the numerical value of each pixel represents the intensity of light signals.

For typical grey-scale images: 1 pixel = 1 byte = 8 bits, which can represent 256 different values (0-255). Where 0 is black and 255 is white.

<figure>
    <img src="../AI_B/grayscale_row.png" alt="Grayscale Image Row" width="600" caption="A row of pixels sampled from a grayscale image.">
    <figcaption>A row of pixels sampled from a grayscale image.</figcaption>
</figure>

A pixel can thus be described as $\mathbf{I}_{i j} = x$, where $i$ and $j$ are the coordinates of the pixel and $x$ is the intensity.

To invert an image, simply take:

$$\mathbf{I}' = 255 - \mathbf{I}$$

With **Contrast Scaling**, we can adjust the range $\mathbf{I}_{ij} \in [L, H]$ of current pixel values to a new range.

$$
\mathbf{C}_{ij} =  \begin{cases}
   L' &\text{if } \mathbf{I}_{ij} \leq L \\
   H' &\text{if } \mathbf{I}_{ij} \geq H \\
    \frac{H' - L'}{H - L}(\mathbf{I}_{ij} - L) + L' &\text{otherwise}
\end{cases}
$$

The output image $\mathbf{C}$ will have pixel values in the range $[L', H']$.

#### Intensity Histograms

We can show the value of the image as a histogram. Where the x-axis corresponds to the intensity of the pixel and the y-axis corresponds to the count.

<figure>
    <img src="../AI_B/histogram.png" alt="Histogram of Pixel Intensities" width="600" caption="Histogram of pixel intensities in a grayscale image.">
    <figcaption>Histogram of pixel intensities for a randomly generated image and Lenna.</figcaption>
</figure>

Quantization is important when we are comparing 

With the **normalized** histogram $h(x)$, we can calculate a lot of qualities of the image. For example, the mean $\mu$, variance $\sigma^2$, and entropy $H(h)$ of the histogram can be calculated as follows:

$$
\mu = \sum_{x=L}^{H} x \cdot h(x)
$$

$$
\sigma^2 = \sum_{x=L}^{H} (x - \mu)^2 \cdot h(x)
$$

$$
H(h) = -\sum_{x=L}^{H} h(x) \log_2 h(x)
$$

Higher entropy means more information is contained in the image. The distribution with highest entropy is the uniform distribution.

If we have two images, we can then calculate the cross-entropy between the two histograms $h_1(x)$ and $h_2(x)$ of the images as follows:

$$CE = -\sum_{x=L}^{H} h_1(x) \log_2 h_2(x)$$

#### Thresholding

Thresholds can be used to distinguish pixels within the image. The image after thresholding with value $t$, $\mathbf{T}$ can be calculated as follows:

$$\mathbf{T}_{ij} = \begin{cases} 
    L & \text{if } \mathbf{I}_{ij} < t \\
    H & \text{if } \mathbf{I}_{ij} \geq t
\end{cases}$$

This essentially is separating the pixels into two groups. For example, if we cutoff at 128 for the Lenna image, we get:

<figure>
    <img src="../AI_B/thresholding.png" alt="Thresholding Example" width="600" caption="Thresholding the Lenna image at 128.">
    <figcaption>Thresholding the Lenna image at 128.</figcaption>
</figure>

It might be obvious that the histogram will be a lot of help when we are trying to find an optimal threshold to separate two objects.

##### Otsu's Method

How to determine the thresholds for separation is a common problem in computer vision. Otsu's method is a popular algorithm to find the optimal threshold for separating two classes in an image.

Intuitively if we think about it, when separating the pixels into two classes, we want the classes to be as different as possible, within one class, the pixels should be as similar as possible.

In mathematical terms, we want to maximize the **between-class variance** while minimizing the **within-class variance**.  Which surprisingly, are the same thing.

