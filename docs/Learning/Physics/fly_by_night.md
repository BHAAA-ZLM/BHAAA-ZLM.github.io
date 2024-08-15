---
title: FLy by Night Physics Notes
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: ??min
publish_date: 2024.?
---

## Dimensional Analysis

### Pendulum Period

#### Simple Dimensional Analysis
Time $T$ have the dimension of time $[T] = T$. If we want ot express time in terms of length $l$ and acceleration $a$, with $[l] = L$ and $[a] = L/T^2$. Thus the period must be: 

$$ T \sim \sqrt{l/a} $$

The exact equation should be $T = 2 \pi \sqrt{l/a}$. The $2 \pi$ can be determined by experiment. 

Or if we consider angular speed and with energy conservation equation, we can get the direct equation for $\omega$ and $T$:

$$ E = \frac{1}{2} m \dot{\theta}^2 + m g l (1 - \cos \theta) \simeq \frac{1}{2} m \dot \theta^2 + \frac{1}{2} m g l \theta^2 $$

The $\simeq$ was obtained from the small angle approximation (with taylor series). Plug in $\theta = \theta_0 \cos{\omega t}$, we get:

$$ E = \frac{1}{2} m \omega^2 \theta_0^2 \sin^2{\omega t} + \frac{1}{2} m g l \theta_0^2 \cos^2{\omega t} $$

In order for $E$ to be a constant, $m \omega^2 \theta_0^2 = m g l \theta_0^2$. Thus $\omega = \sqrt{g/l}$, and $T = 2 \pi / \omega = 2 \pi \sqrt{l/g}$.