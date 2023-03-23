---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 10min 
publish_date: 2023.03.24
---

<img src='../coot_install/6_arg.png' width=600>

<span style="font-family: Courier"> There are two types of ways to install *Coot* on MacOS. One is to simply install the CCP4 package, which have coot bundled inside it. The other method is installing it through homebrew. I will start with the one I found the most useful.

## <span style="font-family: Courier"> Installing Through CCP4 package
<span style="font-family: Courier"> The [Collaborative Computational Project Number 4](https://www.ccp4.ac.uk/?page_id=180) was a very old project indeed. But it contains a lot of useful toos for macromolecule crystollography, including *Coot*. We just need to go to the website of CCP4 and click download.

<img src='../coot_install/ccp4.png' width=600>

<span style="font-family: Courier"> However, remember to pay attention to the **ATTENTION** part in front of the Download Now! You need to have XQuartz installed before everything can work. 

<span style="font-family: Courier"> So if you can't get any of the CCP4 applications to work, don't worry and calm down, just install [XQuartz](https://www.xquartz.org/releases/index.html) and everything will be fine.

## <span style="font-family: Courier"> Installing Through Homebrew
<span style="font-family: Courier"> If you are not feeling very comfortable and don't want to take the more easier path, you can also install it through Homebrew. Take a very good look at this [github repo](https://github.com/pemsley/coot/issues/33), and you will find that your path is very clear.

```bash
wget https://raw.githubusercontent.com/YoshitakaMo/homebrew-bio/coot/Formula/coot.rb
brew install ./coot.rb --verbose --HEAD
```
<span style="font-family: Courier"> These two commands are needed to install *Coot*. However, only these two commands are not enough. You need to ensure that you have the right edition of gtk+3 because *Coot* does not support the latter versions very well. Follow this [issue](https://github.com/pemsley/coot/issues/33#issuecomment-1374409909) and download an older version of gtk+3. But I need to warn you, although the new *Coot* looks cool, it doesn't work very well and have a lot of bugs.

## <span style="font-family: Courier"> Have Fun with *Coot*!