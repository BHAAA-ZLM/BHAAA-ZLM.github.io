---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 15min 
publish_date: 2022.09.09
---

## <span style="font-family: Courier"> Me and the Book
<span style="font-family: Courier"> *The Art of Statistics* is a book by English statistician David Spiegelhalter (maybe Sir D.J.Spiegelhalter). In the summer holidays of 2022, I got into the fields of bioinformatics and start doing some basic RNA sequencing, when we analyse the data of the RNA sequencing, we use things like *Principle Component Analysis* and *p-value* to determine the significance between our experiment group and our control group. The statistics part realy confused me because I don't have the background knowledge, and are definetely not familiar with things like normal distribution or linear regression (although I'm pretty good at linear algebra and understood PCA and SVD quite easily). Just when I was struggling with this problem, I came across this book while walking around a bookstore (One Page in GZ book center to be precise). I didn't buy it at the moment, but it lingered in my brain. After seeing the book again online, I decided to buy it.

<span style="font-family: Courier"> Well, then I fell in love with it and finished the book in two and a half weeks. The fact that I love the book doesn't necessarily mean that this book is perfect. In fact, I think this book is far and far away from pefect, with (I don't know if my english is good enough to judge) some grammar issues (or it might be my own problem), and places where the authour just explain things in a very messy and unclear way (like the linear regression part).

<span style="font-family: Courier"> But still, it's a very great introduction level book. It tells you the basic knowledge you need and how people should think about a problem in a statistiacally correct way.

<span style="font-family: Courier"> All in all, this is a pretty great book.

### <span style="font-family: Courier"> Chapter 0 Introduction
<span style="font-family: Courier"> With a stunning case-study about the Harold Shipman murder, the author led us into a beautiful world of statistics. Using data to find patterns. He also introduced the most important workflow for a statistician, the Problem-Plan-Data-Analysis-Conclusion (PPDAC) workflow. 

### <span style="font-family: Courier"> Chapter 1 Getting Things in Proportion: Categorical Data and Percentages
<span style="font-family: Courier"> In this chapter, the author introduced the very basic idea of a binary variable, sets of which can be summarized as proportions. Different ways of showing your data might lead to different emotional impact on your audiences. We need to be very careful on how we express our findings so that our audiences won't be misled.

### <span style="font-family: Courier"> Chapter 2 Summarizing and Communicating Numbers. Lots of Numbers.
<span style="font-family: Courier"> When you have a lot of data, you need a better way of summarizing it and communicating it. The well-known mean median and mode are just easy ways to describe the data. We can also draw strip-charts, box-and-whisker plots or histograms. While we are exploring data, we want to search for a common trend, that is, finding factors that explains the overall variation.

### <span style="font-family: Courier"> Chapter 3 Why Are We Looking at Data Anyway? Populations and Measurement.
<span style="font-family: Courier"> We perform our studies in order to get a more general understanding of the whole population. That's why we need to go from our data to our study sample and study population, and finally to our target population.

### <span style="font-family: Courier"> Chapter 4 What Causes What?
<span style="font-family: Courier"> This is one of my favourite chapters where the author talks about how do we determine the cause and effect relationship between two events. The *apophenia* nature of human tends to lead us to finding causation in two events just based on their correlation. This chapter also inspired me to buy another book, which is talking about causations.

### <span style="font-family: Courier"> Chapter 5 Modelling Relationships Using Regression
<span style="font-family: Courier"> Building statistical models are very important for analysis. This is also something we learnt during high school. But we were just remembering the equations by then, not caring the deeper knowledge behind them. But this is not a very good chapter if you want to learn about regression models. Because although the author explains the concepts in a very clear way, it lacks mathematical explaination, making all the regression models very abstract. So I guess google will help you a lot on learning about regression modelling.

### <span style="font-family: Courier"> Chapter 6 Algorithms, Analytics and Prediction
<span style="font-family: Courier"> What we learnt in high school is that regression modelling is a way to find a general trend in our data points, and can also be used as a simple model to predict results. But in the real world, there are whole bunch of different algorithms in order to predict. From the most simple and elegant classification tree, to complicated and enormous machine learning, all methods can be used to predict the rate of survival for a passenger on the Titanic. And the simpler algorithm might work better than you think! The author also introduced how to compare different algorithms. It is so surprising that the 3 layered classification tree provided by the author actually works very well in predicting the results.

### <span style="font-family: Courier"> Chapter 7 How Sure Can We Be About What Is Going On? Estimates and Intervals
<span style="font-family: Courier"> We cannot be 100% sure about our prediction based on our statistics, but we have a margin error, which indicates where the true value might lie. In other words, we are 95% sure that the true value will lie between the margin of error, based on past experiences and bootstrapping. The percentages in this chapter is actually quite confusing, like the 95% doesn't imply that our prediction is 95% true. 

### <span style="font-family: Courier"> Chapter 8 Probability - the Language of Uncertainty and Variability
<span style="font-family: Courier"> Probability is a very amazing thing. It does not exist in the real world, it's just something human made up to try to explain the world. Like the coin wasn't born with a probability of 1/2 to land on heads or tails, we humans gave it this probability.

### <span style="font-family: Courier"> Chapter 9 Putting Probability and Statistics Together
<span style="font-family: Courier"> This chapters combine bootstrapping, probability and statistics together to explain the concept of the margin of error.

### <span style="font-family: Courier"> Chapter 10 Answering Questions and Claiming Discoveries
<span style="font-family: Courier"> This is by far my most favourite chapter. Based on past experiences, we are able to calculate the probability of an event happening. And if the probability is super small, then we can consider this event as very significant. That is precisely where my interest *p-value* comes. It describes getting the same result if your hypothesis is not true and some event is just randomly happening. It's very simple and elegant value, and is also controversial, because it might lead to false discoveries. So there is also the Neyman-Pearson Theory, where we can set previously the size and power of the test based on the possibility of finding the null hypothesis true. So that we can get a more accurate p-value and set a reasonable sample number.

### <span style="font-family: Courier"> Chapter 11 Learning from Experience the Bayesian way
<span style="font-family: Courier"> This is a very interesting chapter, which talks about giving a former distribution to all the factors that might influence our experiment, and finally getting a score for our hypothesis, indicating it is true or not. This idea is very interesting, and I'm super interested in the math behind all of this. Sadly, the author stopped again at the basic concepts and basic maths.

### <span style="font-family: Courier"> Final 2 chapters
<span style="font-family: Courier"> After all the statistical knowledge, the author introduced how things can go wrong on each step of the PPDAC workflow, and how can things go wrong while our results are delivered to the public. He also provided solutions to all the problems.