# pands-project

This repository contains the project for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU.\
This project involves researching Fisher's Iris data set and analysing it using Python.

This file will firstly give some background information to the dataset in question. 

I will then outline the steps which I needed to take before I could begin the actual analysis itself: this includes importing the libraries which I will use for the project; giving a description of these libraries.

Next I will outline some summary statistics relating to the variables within the dataset, as well as some information about the Dataframe itself. The Dataframe is the way the information is stored in pandas: as a two-dimensional structure where each piece of information has a row and column label. \
My script will redirect the summary statistics for each of the four variables onto a text file.

I will then carry out data visualisation on the Iris dataset, using histograms, scatterplots and some other types of plots. My script will save each plot generated from the data as a .png file, and these can be viewed below.

My project will conclude with a summary of my findings, and my thoughts upon conclusion of the project. \
I will also provide a list of references which I used to complete my work.

Note: To execute my script, please download analysis.py from my repository into a code editor such as VS Code (which I used to complete this project). \
While located in the folder in which you have saved analysis.py, go to the terminal window and type 'python analysis.py'. \
This should run the code and generate the text file with summary data for the dataset, and the histograms and other plots which analyse the data.

&nbsp; 

## Table of contents
* [Background](#background)
* [Pre-analysis](#pre-analysis)
* [Summary of each variable](#summary-of-each-variable)
* [Histograms](#histograms)
* [Plots](#plots)
* [Other analysis](#other-analysis)
* [Summary](#summary)
* [References](#references)

&nbsp; 

## Background



The data set was collected in 1935 by the American botanist Edgar Anderson, and used in 1936 by the British statistician and biologist Ronald A. Fisher. It relates to data collected from samples of three species of the Iris flowering plant genus: Iris setosa, Iris virginica, and Iris versicolor. \
It is commonly used as an introductory data set by people who are learning how to analyse and visualise data using programming languages.

Fifty samples were collected for each species, giving one hundred and fifty samples in total. \
For each sample, four features of the flower were measured; these were: sepal length, sepal width, petal length and petal width. These attributes of the samples are contained in columns 1, 2, 3 and 4 respectively within the dataset. The species name of the flower is also included in the dataset in column 5.

The petal of a flowering plant are the leaves of the flower which surround the reproductive parts of the flower, and which are often brightly coloured to attract pollinators [1]. Sepals usually protect the flower when it is in a bud and structurally support the petals when the flower is in bloom. [2]

The below is an image of the three flowers analysed in the dataset, along with a label for the sepal and petal of one of the three flower species (Iris Versicolor):

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/iris_flowers.png)

&nbsp; 

## Pre-analysis

I downloaded the Iris dataset from https://archive.ics.uci.edu/ml/datasets/iris. I saved it as a .csv file into the folder where my I worked on my project. There were no headings for the data when I opened the dataset; however, the site which I downloaded the data from did provide the information about what each of the five columns in the dataset represents. I used this to add the headings to the data so I could manipulate it. \

The headings for the five columns were given as below:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
* Iris Setosa
* Iris Versicolour
* Iris Virginica

To enable me to analyse the dataset, I imported some libraries and modules commonly used for this purpose. These were as follows:

Matplotlib is a libarary used by Python to make plots and graphs. It requires NumPy to run. Matplotlib.pyplot is a collection functions which allows us to do different things to the plots we make, such as create them, add headings, change the colour scheme etc.

Numpy (Numerical Python) is a package used in Python to carry out mathemetical operations on numerical datatypes, such as integers and floating-point numbers. It creates multi-dimensional array objects which allow Python to carry out mathemetical operations much more efficiently than would be the case in Python without NumPy. Matplotlib requires NumPy

Pandas is a powerful and flexible Python package used for data analysis, especially of tabular data, such as the data in the .csv file used for this project. I used pandas to open the Iris dataset. Pandas creates data-structures which allow data to be maniulated, with the most important being 1-dimensional data 'series' and 2-dimensional 'dataframes' (this structure is used here). Pandas is built on top of NumPy.

Seaborn is built on top of matplotlib. It enables us to make more appealing plots, utilising different styles.

sys



&nbsp; 

## Summary of each variable


&nbsp; 

## Histograms

&nbsp; 

## Plots

&nbsp; 

## Other Analysis

&nbsp; 

## Summary

&nbsp; 

## References
