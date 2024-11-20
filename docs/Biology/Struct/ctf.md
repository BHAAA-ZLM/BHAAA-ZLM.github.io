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

### The Contrast Transfer Function

Thus we obtained the contrast transfer function $\sin(\chi(\mathbf{r}))$. Where $\chi(\mathbf{r})$ can be described in polar coordinates with: 

$$ r = |\mathbf{r}|, \theta = a \tan(k_x, k_y) $$

$$ \chi(r, \theta) = - \frac{1}{2}\lambda (\Delta z + \frac{z_a}{2} \sin2(\phi - \phi_0))r^2 + \frac{1}{4}\lambda^3 C_s k^4 $$

Where $\Delta z$ is the defocus, $z_a$ is the astigmatis, $C_s$ is the spherical abberation. The function basically discribes a image formed due to the abberation in the instrument.

The final image will be a combination of the contrast transfer function and the specimen transfer function. As we can see from the function, with higher spacial frequency, the contrast transfer function will oscillate more frequently, together with the (not discussed here) envelope function, this makes it hard to obtain infromation at high resolution.