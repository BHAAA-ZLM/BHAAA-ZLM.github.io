---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 3min
publish_date: 2024.10.09
---

Once upon a time, I needed to write a presentation with a lot of equations. It just sickens me to type all these equations with powerpoint. So I decided to take a look at the methods utilizing $\LaTeX$ to write presentation slides. As a proud SUSTech student (at the time), I Googled 'SUSTech Latex Template', and an interesting GitHub repo came up. `latex-template` collects all sorts of templates made by SUSTech students, and there is was, the same template used by my advisor! That's where I ran into [Marp](https://marp.app). Marp is an open-source markdown based ecosystem to write presentations. It could be achieved by adding a simple extension to VScode. A demo of the presentation I made can be found [here](./Marp/presentation_trimmed.pdf).

## Initialize Settings
The first thing to do with MARP setting (in my opinion), is to turn on the `Marp: Enable HTML`. Which allows a more 'free' way of positioning my textbox and images. 

I don't think this setting is turned on at first, so everything ChatGPT taught me when I first wanted to change the presentation style didn't work. After 30 minutes of frustration, I decided to ditch GPT, and soon found out I need to turn on this setting. After turning on, everything works.

## Some Tricks in Writing the Presentation

### Adding a Header
With `css` headers in front of the entire presentation, we are able to add a small header to the top of the slide.
```css
<style>
    header {
    color: #000000;
    font-size: 1.5em;
    font-weight: 700;
    position: absolute;
        top: 30px;
        left: 40px;
    }
    section::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 120px;               /* Height of the grey rectangle */
    background-color: #d3d3d3;   /* Light grey color */
    z-index: -1;                 /* Ensure it stays behind text */
    }
    section {
      background-image: none;
      padding-top: 130px;        /* Default position for format */
      padding-left: 40px;
      padding-right: 40px;
    }
</style>
```
In the section, we should also change the padding values. Otherwise sometimes, the body of the slide will cover the rectangle, making everything look ugly.

And in the markdown file:
```markdown
--- 
<!-- _header: Test -->
```

The header will appear at the top of the file. In this case, 'Test' upon a large grey rectangle spanning the whole slide.

### Adding a Figure at Desired Position
```markdown
<div style="position: absolute; top: 130px; left: 750px;">
  <img src="figures/splash_cell.png" alt="Description" width="500" />
</div>
<div style="position: absolute; top: 550px; left: 760px;">
  <img src="figures/oasis_pnas.png" alt="Description" width="500" />
</div>
```
With HTML syntax, we can locate the pictures at a wanted position inside the slide at ease.

### Adding a Small Table
```markdown
<style>
  .algorithm-caption {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 10px;
  }
</style>

<div style="border: 1.5px solid black; width: 550px;"></div>

<div class="algorithm-caption">Algorithm:</div>

<div style="border: 1px solid black; width: 550px;"></div>

1. Randomize $\vec{c}$.
2. Set $\vec{f} = \mathrm{sign}(\tilde X \vec c)$.
3. $\vec{f} = \{ \frac{1 + \vec{f}}{2}, \frac{1- \vec f}{2} \}$
3. $\vec{f} = \mathrm{arg max}_{\vec{f}}(\vec{f}^\top \tilde{X} \vec{c})$
4. $\vec{c} \propto \tilde X^\top \vec{f}$. (With constraint $||\vec{c}|| \leq 1$)
5. Repeat 2-4 until $S$ doesn't change.
5. Output: $\vec{f}$, $\vec{c}$.

<div style="border: 1.5px solid black; width: 550px;"></div>
```
I didn't came up with a very good way to write a table, so I just use a very brutal way to just draw 2 thick lines and 1 thin one between the texts.

## Ways of Formating Text

I was writing the monthly report for my thesis and suddenly felt it would be very cool to have a small separate style box for the plans in the report. So I had a little chat with ChatGPT and came up with this style:

```css

<style>
  .plan-box {
    padding: 15px;
    font-size: 24px;
    margin: 20px 0;
  }
  .plan-box .content{
    background-color: #80808030;
    background-size: 10%;
    background-position: center;
    border-radius: 10px;
    padding: 30px 0px 3px 0px;
    margin: -40px 0 0 0;
  }
  .plan-box heading {
    margin: -15px -15px -15px -15px;
    padding: 10px;
    color: white;
    background-color: #000000;
    border-radius: 5px 5px 5px 5px;
    position: relative;
    top: -15px;
    left: -15px;
    font-weight: 1000;
    font-size: 30px
  }
</style>
```

Which can make something like this:

<img src="../Marp/plan_style.png">

Which is quite satisfying! Keep tweeking with the margin and padding values so that the two different-coloured background texts are beautifully stacked onto each other!