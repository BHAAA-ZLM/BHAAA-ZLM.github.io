---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 30min 
publish_date: 2022.09.28
---

## Probability Rules

For a wave function $\Psi(x,t)$, we can solve it with the __Schrodinger Equation__:

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial t^2} + V \Psi $$

Where $V$ is the potential energy of the system. $\hbar$ is the reduced Planck constant, $\hbar = \frac{h}{2\pi} = 1.054572\times 10^{-34} \text{J s}$.

The wave function $\Psi$ is a complex function, and the probability of finding a particle at $x$ is $|\Psi(x,t)|^2$. The probability of finding a particle in the range $[a,b]$ is: 

$$ P(a \leq x \leq b) = \int_a^b |\Psi(x,t)|^2 dx $$

After a measurement, the wave function instantly collapses to the measured state. With time, the wave function evolves back to a widely distributed state. The wave function can be solved with the Schrodinger Equation.

---
An example for calculating with the probability density. (I'm not very smart about physics, so this example in my mind, is so smart and witty.)

Suppose I drop a rock off a cliff of height $h$. As it falls, I snap a million photographs, at random intervals. On each picture I measure the distance the rock has fallen. _Question_: What is the average of all the distances? i.e. what is the time average of the distance traveled?

Solution:

$$ x(t) = \frac{1}{2}gt^2 $$

The velocity is $$ v(t) = \frac{dx}{dt} = gt $$ and the total flight times is 

$$T = \sqrt{\frac{2h}{g}}$$

The probability of the camera flashing is $ dt / T$ (if the camera flashes for a short period of time $dt$). Thus the length traveled in this photograph is:

$$ \frac{dt}{T} = {dt}\cdot \sqrt{\frac{g}{2h}} = \frac{dx}{gt}\cdot \sqrt{\frac{g}{2h}} = \frac{1}{2\sqrt{hx}} dx $$ 

So the probability density is 

$$ \rho(x) = \frac{1}{2\sqrt{hx}} $$

The average distance is 

$$ \langle x \rangle = \int_0^h x \rho(x) dx = \int_0^h x\frac{1}{2\sqrt{hx}} dx = \frac{1}{2 \sqrt{h}} (\frac{2}{3} x^{3/2}) \Big|_0^h = \frac{h}{3} $$

---

Because the wave function have a relationship with probability, the wave function must be normalized. The normalization condition is:

$$ \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1 $$

The normalization condition with a constant (complex constant) $A$ is conserved . That is to say, the Schrodinger Equation has the remarkable property that it automatically preserves the normalization of the wave function. That is to say, probability is independent of time. Which can be proved.

---

$$\frac{d}{dt} \int_{-\infty}^{\infty} | \Psi(x,t) |^2 dx = \int_{-\infty}^{\infty} \frac{\partial }{\partial t} | \Psi(x,t) |^2 dx$$

Because the integral is independent of $t$, we can move the derivative inside the integral. And we can use the Schrodinger Equation to replace the derivative. Before that, by the product rule:

$$\frac{\partial}{\partial t} | \Psi |^2 = \frac{\partial}{\partial t}(\Psi^* \Psi) = \frac{\partial }{\partial t} \Psi^* \Psi + \Psi^* \frac{\partial }{\partial t} \Psi$$

Thus with the Schrodinger Equation:

$$ \frac{\partial}{\partial t} | \Psi |^2 = \frac{i \hbar}{2m} (\Psi^* \frac{\partial^2 \Psi}{\partial x^2}  + \frac{\partial^2 \Psi^* }{\partial x^2} \Psi) = \frac{\partial }{\partial x} \Big[\frac{i \hbar}{2m} \Big( \Psi^* \frac{\partial \Psi}{\partial x} - \frac{\partial \Psi^*}{\partial x} \Psi \Big) \Big]$$

So the integral:

$$\frac{d}{dt} \int_{-\infty}^{\infty} | \Psi(x,t) |^2 dx $$

$$ = \int_{-\infty}^{\infty} \frac{\partial }{\partial x} \Big[\frac{i \hbar}{2m} \Big( \Psi^* \frac{\partial \Psi}{\partial x} - \frac{\partial \Psi^*}{\partial x} \Psi \Big) \Big] dx $$

$$ = \frac{i \hbar}{2m} \Big( \Psi^* \frac{\partial \Psi}{\partial x} - \frac{\partial \Psi^*}{\partial x} \Psi \Big) \Big|_{-\infty}^{\infty} = 0 $$

Because the wave function must be zero at $-\infty$ and $\infty$. Thus the probability is independent of time. QED

Interestingly, problem 1.17 in the book gave an example of a particle that is not stable, and have a half life. In that case, the probability function $P(t)$ becomes dependent on time. We can describe this by adding an imaginary part to $V$.

$$ V = V_0 - i \frac{\hbar}{2\tau} $$

Where $\tau$ is the half life of the particle. The imaginary part of $V$ is called the __decay term__. 

---

In the quantum mechanic's world, particles don't follow the normal laws of mechanics, but interestingly there is the __Ehrenfest's theorem__. Which states that the expectation values obey the classical laws.

$$ \langle x \rangle = \int_{-\infty}^{\infty} x | \Psi (x,t) |^2 dx $$

$$ \langle p \rangle = m \frac{d \langle x \rangle}{dt} = \int_{-\infty}^{\infty} \Psi^* \Big( -i \hbar \frac{\partial \Psi}{\partial x} \Big) dx $$

Here we also introduces another new operator, for any quantity related to $x$ and $p$, $Q(x,p)$, the expectation of this quantity is:

$$ \langle Q \rangle = \int_{-\infty}^{\infty} \Psi^* Q(x, -i \hbar \frac{\partial}{\partial x}) \Psi dx $$

For a given particle, it is impossible to know it's position and momentum at the same time. This is called the __Heisenberg Uncertainty Principle__. The uncertainty principle is a direct consequence of the wave nature of matter. The uncertainty principle is:

$$ \sigma_x \sigma_p \geq \frac{\hbar}{2} $$

Where $\sigma_x$ is the standard deviation of $x$, and $\sigma_p$ is the standard deviation of $p$.