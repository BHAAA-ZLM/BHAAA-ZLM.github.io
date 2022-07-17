---
tags:
    - Java
    - Games
---
<span style="font-family: Courier">

# <span style="font-family: Courier"> My First Project - ChessKing

<img src="https://raw.githubusercontent.com/LittleEtx/ChessKing/main/pre/Gameshot.png" width = 600 alt="ChessKing Ad">

<span style="font-family: Courier">
[ChessKing](https://github.com/LittleEtx/ChessKing) was a Java project for the SUSTech course CS102A in 2022 Spring. Created by me and LittleEtx(Li Tian) with great passion.

---

## <span style="font-family: Courier">The Beginning

<span style="font-family: Courier">
For people studying in ShenZhen, the spring of 2022 was very unique, especially when you were not living in ShenZhen during that time. Unluckly, me and LittleEtx were all living in GuangZhou. Because of the pandemic, we all had to stay in our home and take online classes everyday. Which was not very good, but I still found it had some advantages.

<span style="font-family: Courier">
Especially when you are learning Computer Science. For me, computer science is a completely new subject and I was both excited and scared to learn CS102A. The Java class was known as the "Freshmen Killer" (together with Linear Algebra), and lots of students found it super hard and said it's learning process is "torture". Java classes will have a unique project every year and it's usually some kind of games. For exemple, the Java project for 2021 autumn is [Reversi](https://en.wikipedia.org/wiki/Reversi) 

<span style="font-family: Courier">
Luckly for me, my room mate LittleEtx is a total geek, and learning Java to him is like drinking water. So I chose the same class with him and stuck with him for the whole semester. Also, I found a fantastic book called ***Head First Java***, which helped me a lot. Since I don't need to "go" to school, I spent most of my free time reading this book and learning Java.

<span style="font-family: Courier">
After a few weeks, my Java programming skills grew and I found myself happily learning more Java than I expected.

## <span style="font-family: Courier">The Project

<span style="font-family: Courier">
After the midterm exam week, our teacher finally announced the project this semester, which is Chess. The Chess includes a lot of rules and requirements for us to fulfill, so we started to prepare for the project on April 12th. When we created our first git.

### <span style="font-family: Courier">**Git**

<span style="font-family: Courier">
[Git](https://git-scm.com) was a new thing to both of us, because we never used version control before. It was LittleEtx's idea to use Git and he built a repository on GitHub. It was a bit confusing to use (at least for me) at first because of all the pull, commit, and push actions. But luckily it's year 2022 and we have [GitHub desktop](https://desktop.github.com) and [IntelliJ IDEA](https://www.jetbrains.com/idea/), which made things a lot moer easier than using the terminal for all the actions. I'm proud to say that I am quite used to using version controls now (BTW this [blog](https://github.com/BHAAA-ZLM/BHAAA-ZLM.github.io) is also under git's version control).

### <span style="font-family: Courier">**FXGL**

<span style="font-family: Courier">
The next thing was finding a good engine for our game. We have no idea about ui design with Java, and we need a ui for our game. So we search on the internet and found [JavaFX](https://openjfx.io) an open source ui tool for Java. We searched on bilibili and found a set of videos teaching us how to write games using an engine called [FXGL](http://almasb.github.io/FXGLGames/). FXGL is a very interesting and powerful game engine based on JavaFX. It allows us to design different scenes and stages for the game and can add entities in a very smart and efficient way. It requires some learning but we are happy to do it, I even made my own basic tank game as I'm learning!

### <span style="font-family: Courier">**UI Design**
<span style="font-family: Courier">
In the whole project, our work is pretty seperated. LittleEtx is responsable for designing the basic logic of the game, and I am responsable for all the UI, in other words, all the things you can see in the game. Including the buttons (and their interactions), chess, backgrounds and so on.

#### <span style="font-family: Courier">**CSS**

<span style="font-family: Courier">
I need a way to customize all the buttons and HBoxes and VBoxes and so on. So I Googled and found CSS, the language used to style HTML document, but is also supported by JavaFX. I spent a lot of time learning how to change the style of the buttons and adding different images and colours to the backgrounds, and at the end of the project, I am very proud to say that 2.9% of the whole project's language is CSS, and is all written by me! 
 
<img src="./CSSimage.png" width = 500 alt="the CSS ratio">

#### <span style="font-family: Courier">**Themes for the Game**

<span style="font-family: Courier">
The one function I spent most time on was the place where you can chose your theme. You can choose your own avatar, background picture, chess board colours and the skin for your chess. Which will be automatically stored with your player account.

<img src="./ChooseSkin.png" width=500 alt="the choose skin window">

<span style="font-family: Courier">
Avatars are chosen from some of our favourite art works, including games and animations. So are some of the background music. If you want to learn more about our hobbies, you can read the [README.md](https://github.com/LittleEtx/ChessKing/blob/main/README.md) for the repository, where we introduced our likings with love and care.

#### <span style="font-family: Courier">**A DIY Chess Skin**

<span style="font-family: Courier">
Later the teachers and teaching assistants of the course provided us with a demo (written in swing), which contains a very common chess skin. At first, we think it's very convinient, so we just used the pictures inside the demo (and that's what most of the students do). But later, we think the original chess skin is not catchy and can't fulfill our wish that this is a complete and stylish game of our own. So I drew a set of skin for our chess, using my favourite pixel style. It turned out to be very similar to Dead Cells, but I'm a huge fan of the game so it's fine.

<img src="./pixel.png" width=500 alt="the pixel skin">

### <span style="font-family: Courier">**The MVC Model**

<span style="font-family: Courier">
When we finished making the whole game, we found out that we actually were making something that fitted the MVC model, which in simple words, is the seperation of the things the user can control from the basic logic of the game. As I learnt more about MVVM (the Apple swift structure for an app), I started to notice that there are still some things we could improve to achieve a better structure, but I'm still very pleased that we made some sign of a MVC model game.

## <span style="font-family: Courier">The Show

### <span style="font-family: Courier">**Dream**

<span style="font-family: Courier">
From the beginning of our long work, our dream had been to make a game that is whole and complete. Which means that it should at least fulfill all the requirements of a normal chess game, have a menu and players have individule savings. Also, since it's a computer game, we wish to have strong AIs that can torture human players when tey are boring. That's why, when most of our classmates are using the teacher's demo as a template, we started to write the whole game from scratch.

### <span style="font-family: Courier">**Presentation**

<span style="font-family: Courier">
Naturally, our hard work was approved by our teachers. Not only did we get a high grade, we were also invited to present our work in the big class. We consider it to be a great opportunity to share our happiness with all our classmates. 

<span style="font-family: Courier">
It was at this time, that I learned how to write Markdown files. I wrote a README file for our repository, and another file for our presentation. The [presentation file](https://github.com/LittleEtx/ChessKing/blob/main/Presentation.md) contatins all the knowledges we had learnt during this wonderful experience.

<span style="font-family: Courier">
I'm so happy to see all the interested and astonished faces of my classmates when we did our presentation. After the class, they are all chatting in the chat group for our game. We feel so happy that our work is admitted by others. It's a wonderful learning experience!

<span style="font-family: Courier">
Lumi 2022.07.17
