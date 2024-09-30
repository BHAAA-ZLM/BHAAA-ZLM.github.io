---
title: FLy by Night Physics Notes
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: ??min
publish_date: Updating...
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

### Crossing the River

With this example, we can learn the significance of guessing the functions with the limit conditions. Usually in physics, the conditions are $0$ or $1$. By $0$, we are meaning the usual $0$ and the usual limit $1/\infty$.

<div style="text-align: center;">
    <svg width="300" height="200">
        <line x1="0" y1="50" x2="300" y2="50" style="stroke:black;stroke-width:2;"/>
        <line x1="0" y1="150" x2="300" y2="150" style="stroke:black;stroke-width:2;"/>
        <!-- Drawing the O dot -->
        <circle cx="50" cy="150" r="3" style="fill:black;" />
        <text x="55" y="170" font-family="Times New Roman" font-size="20" fill="black">O</text>
        <!-- Drawing the C dot -->
        <circle cx="50" cy="50" r="3" style="fill:black;" />
        <text x="55" y="45" font-family="Times New Roman" font-size="20" fill="black">C</text>
        <!-- Draw dashed line -->
        <line x1="50" y1="150" x2="50" y2="50" style="stroke:black;stroke-width:1;stroke-dasharray:5,5;"/>
        <text x="25" y="105" font-family="Times New Roman" font-size="20" fill="black">w</text>
        <!-- Draw crossing river at point P -->
        <line x1="50" y1="150" x2="170" y2="50" style="stroke:black;stroke-width:1.5;"/>
        <circle cx="170" cy="50" r="2" style="fill:black;" />
        <text x="175" y="45" font-family="Times New Roman" font-size="20" fill="black">P</text>
        <!-- Draw the arrow for velocity -->
        <defs>
        <marker id="arrowhead" markerWidth="5" markerHeight="4" 
                refX="0" refY="2" orient="auto">
        <polygon points="0 0, 5 2, 0 4" style="fill:black;" />
        </marker>
        </defs>
        <line x1="200" y1="30" x2="230" y2="30" 
                style="stroke:black; stroke-width:1.4;" 
                marker-end="url(#arrowhead)" />
        <text x="245" y="37" font-family="Times New Roman" font-size="20" fill="black">F</text>
        <text x="115" y="40" font-family="Times New Roman" font-size="20" fill="black">x</text>
        <text x="200" y="107" font-family="Times New Roman" font-size="20" fill="black">the River</text>
    </svg>
</div>

(Spent 1 hours drawing this with SVG, so complicated haha)

A person wants to cross the river starting from $O$ to reach $F$, crossing the river at point $P$. She is moving with speed $v_l$ on land and $v_w$ in the water. Since we are talking about a human, we assume: 

$$ \gamma \equiv \frac{v_l}{v_w} > 1 $$

So where should $P$ be for here to reach $F$ ASAP?

#### The Fly by Night Method
With some dimensional analysis, we can say that $x$ should be something like this:

$$ x = w f(\gamma) $$

With $\gamma \rightarrow 1$, the person (lets say Beque), should walk and swim at the same speed. Which make it no difference to swim or walk directly to the finish. So $x \rightarrow \infty$ as $\gamma \rightarrow 1$.

With $\gamma \rightarrow \infty$, Beque should walk as fast as possible. She should spend the shortest amount of time swimming. So $x \rightarrow 0$ as $\gamma \rightarrow \infty$.

With these two limits, we can guess that $f(\gamma) = \frac{1}{\gamma (\gamma - 1)}$ or $\frac{1}{\gamma^2 - 1}$. Also, we restricted $\gamma > 1$, the usual thing to do is to limit it with imaginary parts. So I find both $f(\gamma) = \frac{1}{\sqrt{\gamma (\gamma - 1)}}$ and $f(\gamma) = \frac{1}{\sqrt{\gamma^2 - 1}}$ reasonable.

#### The Proper Analysis
First, the distance from $C$ to $F$ is not important. So the time from $P$ to $F$, is 

$$ \frac{L_{cf} - x}{v_l} = \frac{L_{cf}}{v_l} - \frac{x}{v_l} = T - \frac{x}{v_l} $$

The time from $O$ to $F$ is irrelevant in the choice of $x$, and will disappear after differentiation. So the time from $O$ to $P$ is:

$$ t = T - \frac{x}{v_l} + \frac{L_{po}}{v_w} = T - \frac{x}{v_l} + \frac{\sqrt{w^2 + x^2}}{v_w} $$

Taking the derivative of $t$ with respect to $x$ and set it to $0$:

$$ \frac{d t}{d x} = - \frac{1}{v_l} + \frac{x}{v_w \sqrt{x^2 + w^2}} = 0 $$

Solve for $x$ and we get:

$$ x = \frac{w}{\sqrt{\gamma^2 - 1}} $$

This fits our guess perfectly! How Amazing!