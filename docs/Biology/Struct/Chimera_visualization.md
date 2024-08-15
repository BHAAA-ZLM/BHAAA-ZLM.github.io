---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 2min 
publish_date: Continuous update
---

In this blog, I will describe some of the useful (and beautiful) visualization made with [ChimeraX](https://www.rbvi.ucsf.edu/chimerax/) I have found during the years of reading (and surfing the internet).

A useful [guide](https://rbvi.github.io/chimerax-recipes/) was made by the ChimeraX creators, and I tried to apply them to our protein of interest.

## Loopy Alpha Helix
I was listening to a talk by Prof. James H. Hurley in August at SUSTech, and I can't stop noticing how nice his resulting structures are. So I did some research and looked at his structures in this paper about the [lysosomal mTORC1–TFEB–Rag–Ragulator megacomplex](https://www.nature.com/articles/s41586-022-05652-7) published in nature, and mimicked his style. 

![Loopy Alpha Helix Original](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-022-05652-7/MediaObjects/41586_2022_5652_Fig2_HTML.png?as=webp)

```python
# Setting window size can make visualization easier
windowsize 800 800 

open 7UX2
hide atoms 
show cartoons
color bychain

# Adjust lighting of the protein
lighting soft msMapSize 64

# Adjust the style of the protein to loopy helices
cartoon style protein modeHelix default arrows false xsection oval width 1 thickness 1
# Make helices slightly thicker
cartoon style strand modeHelix default arrows true xsection rectangle width 2 thickness 1
# Draw strands with rectangle arrows
cartoon style helix modeHelix default arrows false xsection oval width 1.6 thickness 1.2

# Visualization seems better with silhouette
graphics silhouettes width 3

save rag_ragulator.jpg pixelSize 0.05 quality 100
```

![My Output](chimera/rag_ragulator.jpg)

I prefer the thicker silhouette when viewing the whole protein. But I think it would be better if we can change the colour of the different chains. I will try to do that in the future.