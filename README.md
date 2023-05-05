# pands-project

This repository contains the project for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU.\
This project involves researching Fisher's Iris data set and analysing it using Python.

This file will firstly give some background information to the dataset in question. 

I will then outline the steps which I needed to take before I could begin the actual analysis itself: this includes importing the libraries which I will use for the project; giving a description of these libraries.

Next I will outline some summary statistics relating to the variables within the dataset, as well as some information about the Dataframe itself. The Dataframe is the way the information is stored in pandas: as a two-dimensional structure where each piece of information has a row and column label. \
My script will redirect the summary statistics for each of the four variables on to a text file.

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

I downloaded the Iris dataset from https://archive.ics.uci.edu/ml/datasets/iris. I saved it as a .csv file into the folder where my I worked on my project. There were no headings for the data when I opened the dataset; however, the site which I downloaded the data from did provide the information about what each of the five columns in the dataset represents. I used this to add the headings to the data so I could manipulate it.

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

* Matplotlib is a library used by Python to make plots and graphs. It requires NumPy to run. Matplotlib.pyplot is a collection functions which allows us to do different things to the plots we make, such as create them, add headings, change the colour scheme etc.

* Numpy (Numerical Python) is a package used in Python to carry out mathemetical operations on numerical datatypes, such as integers and floating-point numbers. It creates multi-dimensional array objects which allow Python to carry out mathemetical operations much more efficiently than would be the case in Python without NumPy. 

* Pandas is a powerful and flexible Python package used for data analysis, especially of tabular data, such as the data in the .csv file used for this project. I used pandas to open the Iris dataset. Pandas creates data-structures which allow data to be manipulated, with the most important being 1-dimensional data 'series' and 2-dimensional 'dataframes' (this structure is used here). Pandas is built on top of NumPy.

* Seaborn is built on top of matplotlib. It enables us to make more appealing plots, utilising different styles.

* The sys module contains different methods and variables which allow us to interact with the environment in which we are executing the Python code. For example, the sys.stdout method (which I used in this project) provides the functionality to print script output from the terminal on to an external text document, where it can be read.



&nbsp; 

## Summary of each variable

The *.describe()* method in pandas produces summary statistics from the dataset which it used on. In this case, I looked for summary statistics for:
1. each of the four measured variables ('sepal width', 'sepal height', 'petal width' and 'petal height') for all of the flowers as a group (sample size = 150), and
2. each of the four measured variables for *each* variety of Iris flower (3 groups each of sample size = 50).\
I thought it would be interesting to see how different the statistics are for each Iris variety in isolation, so I used the pandas *groupby()* function in conjunction with the *.describe* method to generate these statistics. I also used the NumPy method *np.transpose()* to invert the way the summary statistics were printed, because when printed without inverting them, the results are not easily readible on the outputted text file.

* count: The count for the group as a whole was 150 samples, while the count for each class was 50 samples. Each sample had 4 variables measured.

* mean (average): For the group as a whole, sepal length has the highest average length (5.843 cm), followed by petal length (3.756 cm), then sepal width (3.05 cm), and finally petal width gave the lowest average length (1.2 cm). \
This ranking held for each of the three Iris varieties of Setosa, Versicolor and Virginica, but it is interesting to see how much smaller the numbers are for Iris Setosa compared to the other two varieties.

* standard deviation: 

* min 

* 50th percentile (median)

* 25th and 75th percentile

* max


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
