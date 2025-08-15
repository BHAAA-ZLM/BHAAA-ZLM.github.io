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

In mathematical terms, we want to maximize the **between-class variance** while minimizing the **within-class variance**.  Which surprisingly, are the same thing. Because mathematically, the total variance is the sum of these two variances.

If $\sigma_t$ is the total variation, $\sigma_b$ and $\sigma_w$ are the variances between groups and within groups, then:

$$\sigma_t^2 = \sigma_b^2 + \sigma_w^2$$

$$\sigma_b^2 = w_0(\mu_0 - \mu)^2+w_1(\mu_1 - \mu)^2 = w_0 w_1 (\mu_1 - \mu_0)^2$$

Where $w_0, w_1$ are separate weights of these classes.

$$w_i = \sum^{k_i}p_i(x)$$

We then find the threshold $t$ which maximizes $\sigma_b$.


```python
import numpy as np


def otsu_intraclass_variance(image, threshold):
    """
    Otsu's intra-class variance.
    If all pixels are above or below the threshold, this will throw a warning that can safely be ignored.
    """
    return np.nansum(
        [
            np.mean(cls) * np.var(image, where=cls)
            #   weight   ·  intra-class variance
            for cls in [image >= threshold, image < threshold]
        ]
    )
    # NaNs only arise if the class is empty, in which case the contribution should be zero, which `nansum` accomplishes.


# Random image for demonstration:
image = np.random.randint(2, 253, size=(50, 50))

otsu_threshold = min(
    range(np.min(image) + 1, np.max(image)),
    key=lambda th: otsu_intraclass_variance(image, th),
)
```

##### K-means Clustering
We can first separte the pixels according to the mean of all pixels, $\mu$. Then, we set the threshold to the middle point of the mean of the two clusters.

$$t = \frac{\mu_1 + \mu_2}{2}$$

Repeat this process multiple times until $t$ converges to a certain value.

### Change Detection and Background Extraction.

Videos can be seen as a sequence of images $\mathbf{I}(i,j,t)$.

For the human eye, a frame rate of 25Hz is considered smooth.

#### Detection of Change

We can define the **temporal difference** of the images, $\mathbf{D}(i,j,t)$ as:

$$\mathbf{D}(i,j,t) = |\mathbf{I}(i,j,t) - \mathbf{I}(i,j,t-1)|$$

A difference is considered interesting if the difference surpasses a certain threshold. The resulting difference of interest, $\mathbf{D}'$ is:

$$\mathbf{D}'(i,j,t) = \begin{cases}
    1 & \text{if } \mathbf{D}(i,j,t) > \tau \\
    0 & \text{if } \mathbf{D}(i,j,t) \leq \tau
\end{cases}$$

#### Background Extraction
The adaptive background $\mathbf{B}(i,j,t)$ is a kind of mean that can ignore the moving things and preserve the inanimate backgrounds.

$$\mathbf{B}(t) = \frac{1}{N}\sum^t_{i=t-N}\mathbf{I}(i, j, t)$$

Another way of definition can also be:

$$\mathbf{B}(i, j, t + 1) = \alpha \mathbf{I}(i, j, t) + (1 - \alpha)\mathbf{B}(i, j, t)$$

<figure>
    <img src="../AI_B/video_background.png" alt="Background Extraction Example" width="600" caption="Background extraction example.">
    <figcaption>Background extraction example. (top) Original image. (middle) Calculated background. (bottom) Original - Background & mapped.</figcaption>
</figure>

As we can see from the example. A very long truck came into the parking lot in image 5. After parking in image 6, the truck is no longer moving, and gradually blends into the background.

This moving avarage is not only useful in background extraction, but also useful in other momentum-related methods such as [ADAM](https://arxiv.org/abs/1412.6980).

Other background extraction methods fits Normal distributions to the pixel intensities. Which can fit the mean and variation as time progresses. Allowing some variations in the pixel intensities.


### Colours

In nature, colour comes from interactions between the electromagnetic waves and our cones in the retinal. Our eyes can only see the electromagnetic waves with wavelengths between 400-700nm.

#### RGB Colour Space
One of the ways to measure colour (in order to match our perception methods with the eye), is the RGB colour space. Where each colour is represented as a mixture of certain amounts of red, green and blue.

<figure>
    <img src="../AI_B/lenna_rgb.png">
    <figcaption>Lenna image with the three different channels.</figcaption>
</figure>

You can covert the RGB colour space to grey-scale by taking the average of the three channels, or with a specific formula:

$$\mathbf{I}_{grey} = 0.299 \cdot \mathbf{I}_{red} + 0.587 \cdot \mathbf{I}_{green} + 0.114 \cdot \mathbf{I}_{blue}$$

Which produces (in my opinion) similar results.

Apart from the RGB colour space, there are other colour spaces such as HSV (Hue, Saturation, Value). 

#### Comparing Coloured Images
To compare two coloured images, instead of drawing separate histograms for each channel, we can index the pixels with a single value, $v$, which is a combination of the three channels:
$$v = \mathbf{I}_{red} + 256 \cdot \mathbf{I}_{green} + 256^2 \cdot \mathbf{I}_{blue}$$

Then, we can use the value histogram to calculate the distances between two images.

### Sampling and Fourier Transform

The sin wave can be described as a function of time:

$$y(t) = A \sin(2 \pi f t + \phi)$$

Where $A$ is the amplitude, $f$ is the frequency, and $\phi$ is the phase.

In the real life, you can only measure (or sample) some fraction of the real data. The sampling rate is the number of samples per second, $f_s$. 

The Nyquist-Shannon sampling theorem states that to reconstruct a signal without aliasing, the sampling rate must be at least twice the highest frequency in the signal. Otherwise the high frequency components of the signal will be lost.

The Fourier Transform is a mathematical operation that transforms a signal from the time domain to the frequency domain. It decomposes a function into its constituent frequencies in a linear manner.

The continuouse Fourier Transform in 2D space is defined as:

$$\mathcal{F}(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mathbf{I}(x,y) e^{-2\pi i (u x + v y)} dx dy$$

Recall the Euler's formula $e^{ix} = \cos(x) + i \sin(x)$. Where the $u, v$ are the corresponding frequencies in the $x$ and $y$ directions.

The process can be inversed by the Inverse Fourier Transform:

$$\mathcal{F}^{-1}(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mathcal{F}(u, v) e^{2\pi i (u x + v y)} du dv$$

For a "sampled" image, the Discrete Fourier Transform (DFT) is defined as:

$$\mathcal{F}(u, v) = \sum_{i=0}^{M-1} \sum_{j=0}^{N-1} \mathbf{I}(i,j) e^{-2\pi i (u i / M + v j / N)}$$

Where $M$ and $N$ are the dimensions of the image. It also, of course, can be inversed by the Inverse Discrete Fourier Transform (IDFT):

$$\mathcal{F}^{-1}(i, j) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} \mathcal{F}(u, v) e^{2\pi i (u i / M + v j / N)}$$

After Fourier Transform, the resulting $\mathcal{F}(u,v)$ is a complex number. The magnitude and phase can be calculated as follows:

$$\text{magnitude} = \sqrt{\text{real}^2 + \text{imaginary}^2}$$

$$\text{phase} = \tan^{-1}(\frac{\text{imaginary}}{\text{real}})$$

Also, we shift the zero-frequency component to the center of the spectrum for better visualization.

### Convolution and Filtering
Convolution is a mathematical operation that combines two functions to produce a third function. It can be imagined as a sliding window operation, where one function is flipped and slid over the other function, and the overlapping values are multiplied and summed to produce the output.

In a continuous 1D space, the convolution of two functions $f(t)$ and $g(t)$ is defined as:

$$ (f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) d\tau $$

In a discrete 2D space, the convolution of an image $\mathbf{I}(i,j)$ with a kernel $\mathbf{K}(m,n)$ is defined as:

$$ (\mathbf{I} * \mathbf{K})(i, j) = \sum_{m=-k}^{k} \sum_{n=-k}^{k} \mathbf{I}(i - m, j - n) \mathbf{K}(m, n) $$

Where $k$ is the radius of the kernel.

An interesting property of convolution is that when combined with the Fourier Transform, it becomes a multiplication operation in the frequency domain:

$$\mathcal{F}(f * g) = \mathcal{F}(f) \cdot \mathcal{F}(g)$$

This can be proved mathematically:

$$\mathcal{F}(f * g)(u) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\tau) g(t - \tau) d\tau e^{-i2\pi(ft)} dt$$

Suppose: $w = t - \tau$, then $dt = dw$ and the limits of integration change accordingly.

$$\mathcal{F}(f * g)(u) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\tau) g(w) d\tau e^{-i2\pi(f(w + \tau))} dw$$

$$\mathcal{F}(f * g)(u) = \int_{-\infty}^{\infty} f(\tau) e^{-i2\pi(f\tau)} d\tau \int_{-\infty}^{\infty}  g(w)e^{-i2\pi(fw)} dw$$

Which is the multiplication of the Fourier Transforms of $f$ and $g$.

Convolution is usually used for filtering images. For example, a Gaussian filter can be used to blur an image and reduce noise.

<figure>
    <img src="../AI_B/lenna_blurred.png" alt="Gaussian Blur Example" width="600" caption="Gaussian blur example.">
    <figcaption>Gaussian blur example. (left) Original image. (right) Blurred image with kernel.</figcaption>
</figure>

We could of course infer from the Fourier Transform property, that the Gaussian filter in the frequency domain is a Gaussian function, which is a low-pass filter. It removes high-frequency components from the image, resulting in a smoother image.

It can also be used for pattern detection. A kernel with 1 in the middle row and -1 in the surrounding can be used to detect edges in an image. In fourier space, consider only keeping the information at a specific frequency.

<figure>
    <img src="../AI_B/lenna_convolution_hline.png" alt="Edge Detection Example" width="600" caption="Edge detection example.">
    <figcaption>Edge detection example. (left) Original image. (right) Edges detected with kernel.</figcaption>
</figure>

Two types of noise can be added to an image: Gaussian noise and Salt-and-Pepper noise. Gaussian noise is a random noise that follows a Gaussian distribution, while Salt-and-Pepper noise is a random noise that adds white and black pixels to the image.

The Gaussian filter can be used to reduce Gaussian noise.

### Scaling Space and Edge

 