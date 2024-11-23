---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 10min
publish_date: 2024.11.20
---

## The Property of the Image
The microscope transferred the information of the wave after it passed through the specimen to the final image, where every point $g(\mathbf{r})$ in the final image is influenced by all the waves after the specimen $f(\mathbf{r})$. Supposing the coordinates can be shared (or have a linear relationship). The final image can be described as:

$$ g(\mathbf{r}) = \int f(\mathbf{r}') h(\mathbf{r} - \mathbf{r}') d\mathbf{r}' = f(\mathbf{r}) \otimes h(\mathbf{r}) $$

Where $h(\mathbf{r})$ is the function describing how a point is spread into a disk, and is called the point-spread function.

## The Influence of the Specimen

Obtaining $f(\mathbf{r})$ is the first step to understanding the contrast transfer function. A general and very easy model might be:

$$ f(\mathbf{r}) = A(\mathbf{r}) \exp(-i\phi(\mathbf{r})) $$

Where $A(\mathbf{r})$ is the amplitude and $\phi(\mathbf{r})$ is the phase of the wave. In our high resolution transmission electron microscope, the amplitude of the wave can be seen as un uniform, i.e. $A(\mathbf{r}) = 1$. Now, how do we obtain $\phi(\mathbf{r})$?

### The Interaction of the Wave with the Specimen

For a very thin specimen, the projected potential $V_t(\mathbf{r})$ can be described as:

$$ V_t(\mathbf{r}) = \int_0^t V(\mathbf{r}, z) dz $$

The wavelength of the electron can be discribed as:

$$ \lambda = \frac{h}{p} = \frac{h}{\sqrt{2m_e E}} $$

If the electron is passing through the sepcimen, its wavelength will be influenced by the projected potential.

$$ \lambda ' = \frac{h}{\sqrt{2m_e (E + V(\mathbf{r},z))}} $$

The change in phase, can be described by:

$$ d\phi = 2\pi \frac{dz}{\lambda '} - 2\pi \frac{dz}{\lambda} $$

$$ d\phi = 2\pi \frac{dz}{\lambda} \left( \sqrt{\frac{E + V(\mathbf{r},z)}{E}} - 1 \right) $$

$$ d\phi = 2\pi \frac{dz}{\lambda} \left( \left( 1 + \frac{V(\mathbf{r},z)}{E} \right)^{\frac{1}{2}} - 1 \right) $$ 

Since $\frac{V(\mathbf{r},z)}{E} \to 0$, by using [Binomial approximation](https://en.wikipedia.org/wiki/Binomial_approximation), we can obtain:

$$ d\phi = 2\pi \frac{dz}{\lambda} \frac{1}{2} \frac{V(\mathbf{r},z)}{E} $$

$$ d\phi =  \frac{ \pi }{\lambda E} V(\mathbf{r},z) dz $$

Set the interaction constant $\sigma = \frac{ \pi }{\lambda E}$, we can obtain:

$$ \phi(\mathbf{r}) = \sigma \int_0^t V(\mathbf{r},z) dz $$

$$ \phi(\mathbf{r}) = \sigma V_t(\mathbf{r}) $$

The absorption can be taken into account by adding a function $\mu(\mathbf{r})$, now the specimen transfer function can be described as:

$$ f(\mathbf{r}) = \exp(-i\sigma V_t(\mathbf{r})-\mu(\mathbf{r})) $$

The absorption is usually very small, this is called a phase-object approximation.

If the specimen is extremely thin, i.e. $V_t(\mathbf{r}) \ll 1$, the phase object approximation can be simplified with Taylor expansion:

$$ f(\mathbf{r}) = 1 -i\sigma V_t(\mathbf{r}) $$

### Wave Function at the Image

The wave function seen by the image is now given by:

$$ \psi(\mathbf{r}) = (1 - i \sigma V_t(\mathbf{r})) \otimes h(\mathbf{r}) $$

If we represent the function $h(\mathbf{r})$ as $\cos(\chi(\mathbf{r})) + i \sin(\chi(\mathbf{r}))$, then $\psi(\mathbf{r})$ can be described as:

$$ \psi(\mathbf{r}) = 1 \otimes h(\mathbf{r}) - i \sigma V_t(\mathbf{r}) \otimes \cos(\chi(\mathbf{r})) + \sigma V_t(\mathbf{r}) \otimes \sin(\chi(\mathbf{r})) $$

Because of (I think) the conservation of energy, $1 \otimes h(\mathbf{r}) = 1$. The final intensity of the image can be described as:

$$ I = \psi \psi^* = 1 + 2\sigma V_t(\mathbf{r}) \otimes \sin(\chi(\mathbf{r})) $$

The final image is influenced by two terms. The specimen influencing on wave transfer $\sigma V_t(\mathbf{r})$ and the phase shift caused by the abberation in the instrument $\sin(\chi(\mathbf{r}))$.

## The Contrast Transfer Function

Thus we obtained the contrast transfer function $\sin(\chi(\mathbf{r}))$. Where $\chi(\mathbf{r})$ can be described in polar coordinates with: 

$$ r = |\mathbf{r}|, \theta = a \tan(k_x, k_y) $$

$$ \chi(r, \theta) = - \frac{1}{2}\lambda (\Delta z + \frac{z_a}{2} \sin2(\phi - \phi_0))r^2 + \frac{1}{4}\lambda^3 C_s k^4 $$

Where $\Delta z$ is the defocus, $z_a$ is the astigmatis, $C_s$ is the spherical abberation. The function basically discribes a image formed due to the abberation in the instrument.

The final image will be a combination of the contrast transfer function and the specimen transfer function. As we can see from the function, with higher spacial frequency, the contrast transfer function will oscillate more frequently, together with the (not discussed here) envelope function, this makes it hard to obtain infromation at high resolution.

## Properties of the Contrast Transfer Function

Just looking at the Maths isn't very intuitive. So I wrote some Python codes to demonstrate the properties of the Contrast Transfer Function. Codes for this small video can be found on another [GitHub Repository](https://github.com/BHAAA-ZLM/Learning_All_Sorts/blob/master/transmission_EM/fft_image.py) of mine.

<video width=500 height=500 controls>
  <source src="../ctf/ctf.mov" type="video/quicktime">
</video>

As we can see from the video, by changing the defocuse value $z$, the image have different details. This feels like passing the Fourier Transform of the image through a high-pass and low-pass filter at the same time. Some details are unfortunately lost forever after.

### Coding the Snippet

The code for this animation is not actually very hard. Instead of using matplotlib, I could have used better plotting tools like [MANIM](https://github.com/3b1b/manim). I'll probably try later if I have time.

The code is made up of three parts, the contrast transfer function definition, the Fourier Transform of the image and filtering, and plotting the image with a slider.

#### Contrast Transfer Function Code
```Python
def ctf_function(z, x):
    """
    Computes the CTF for a given defocus value z and spatial frequency x.

    Args:
        z (float): Defocus value (angstrom).
        x (float): Spatial frequency (angstrom^-1).

    Returns:
        float: The CTF value for the given defocus and spatial frequency.
    """
    return np.sin(-np.pi * z * x**2 + (np.pi / 2) * x**4)
```

Which is basically the _Standard Characteristics_ with generalized variables for defocus, spatial frequency and (not used here) source size. Which are:

$$
\Delta \hat{z} = \frac{\Delta z}{[C_s \lambda]^\frac{1}{2}} ,\text{ } \hat{k} = [C_s \lambda]^\frac{1}{4}k, \text{  } \hat{q_0} = [C_s \lambda^3]^\frac{1}{4} q_0
$$ 

And the contrast transfer function is generalized for all transmission electron microscopes:

$$ CTF(\hat{k}, \Delta \hat{z}) = \sin[- \pi \Delta \hat{z} \hat{k}^2 + \frac{\pi}{2} \hat{k}^4]$$

#### Fourier Transform and Filtering

```Python
import numpy as np

def ctf_transform(image, z = 1):
    # Fourier Transform
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Generate the CTF filtered image
    rows, cols = image.shape
    x = np.linspace(-2, 2, cols)
    y = np.linspace(-2, 2, rows)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)
    ctf = ctf_function(z, r)
    filtered_transform = f_transform_shifted * ctf 

    # Inverse Fourier Transform
    filtered_transform_shifted = np.fft.ifftshift(filtered_transform)
    filtered_image = np.fft.ifft2(filtered_transform_shifted)
    filtered_image = np.abs(filtered_image)
    return ctf, filtered_transform, filtered_image
```

Then we filter the image (after Fourier Transform and shifting) with the contrast transfer function. 

#### Plotting

```Python
# Create the plot
fig, ax = plt.subplots(1, 4, figsize=(12, 6))
plt.subplots_adjust(left=0.1, bottom=0.25)  # Adjust for sliders

# Original image
ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original Image")
ax[0].axis('off')

# 2D CTF plot
ctf_im = ax[1].imshow(output[0], cmap='gray')
ax[1].set_title("Contrast Transfer Function (2D)")
ax[1].set_xlabel("Spatial Frequency (1/angstrom)")
ax[1].axis('off')

# Filtered image
filtered_im = ax[2].imshow(np.log(np.abs(output[1]) + 1), cmap='gray')
ax[2].set_title("Image After CTF Filtering")
ax[2].axis('off')

# Output image
out_im = ax[3].imshow(1 + output[2], cmap='gray', vmin=0, vmax=output[2].max() + 1)
ax[3].set_title("Filtered Image")
ax[3].axis('off')

# Add sliders
ax_z = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_z = Slider(ax_z, 'z', -2, 2, valinit=1)

# Update function for sliders
def update(val):
    z = slider_z.val
    output = ctf_transform(image, z)
    ctf_im.set_data(output[0])
    filtered_im.set_data(np.log(np.abs(output[1]) + 1))
    out_im.set_data(1 + output[2])
    fig.canvas.draw_idle()

slider_z.on_changed(update)
plt.show()
```

Finally we plot all the values. With the final image, I added a `1 + ` to mimic the effect of the transmission electrons on the final image. Remember to set the minimum and maximum value for the colour bar, otherwise matplotlib will set the smallest value to black and largest to white and you won't be able to get an image with grey background.

Just for fun, I added a slider (with the help of AI) to show the change in the final output as the defocus value changes.

## References
[1] Frank, J. (2006). Three-Dimensional Electron Microscopy of Macromolecular Assemblies: Visualization of Biological Molecules in Their Native State. _Oxford University Press._

[2] Williams, D. B., & Carter, C. B. (2008). Transmission electron microscopy: A textbook for materials science (2nd ed). _Springer_.

[3] Caltech. Part 3: The Contrast Transfer Function - G. Jensen. [_Youtube_](https://www.youtube.com/watch?v=mPynoF2j6zc).