# pands-project

This repository contains the project for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU.\
This project involves researching Fisher's Iris data set and analysing it using Python.

This file will firstly give some background information to the dataset in question. 

I will then outline the steps which I needed to take before I could begin the actual analysis itself: downloading the data-set, adding the correct headings, and importing the modules, libraries and packages which I used for the project.

Next I will outline some summary statistics relating to the variables within the dataset. 
My script will redirect the summary statistics for each of the four variables on to a text file.

I will then carry out data visualisation on the Iris dataset, using histograms, scatterplots and some other types of plots. My script will save each plot generated from the data as a .png file, and these can be viewed below.

My project will conclude with a summary of my findings, and my thoughts upon conclusion of the project. \
I will also provide a list of references which I used to complete my work.

Note: To execute my script, please download analysis.py from my repository into a code editor such as VS Code (which I used to complete this project). While located in the folder in which you have saved analysis.py, go to the terminal window and type 'python analysis.py'. This should run the code and generate the text file with summary data for the dataset, and the histograms and other plots which analyse the data.

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

* Pandas is built on top on NumPy, and is a powerful and flexible Python package used for data analysis, especially of tabular data, such as the data in the .csv file used for this project. I used pandas to open the Iris dataset. Pandas creates data-structures which allow data to be manipulated, with the most important being 1-dimensional data 'series' and 2-dimensional 'Dataframes' (the structure which is used here to manipulate the Iris data). The Dataframe in pandas stores data as a two-dimensional structure where each piece of information has a row and column label.

* Seaborn is built on top of matplotlib. It enables us to make more appealing plots, utilising different styles.

* The sys module contains different methods and variables which allow us to interact with the environment in which we are executing the Python code. For example, the sys.stdout method (which I used in this project) provides the functionality to print script output from the terminal on to an external text document, where it can be read.



&nbsp; 

## Summary of each variable

Using pandas, we can generate various summary statistics of the data contained in a pandas Dataframe object. One way of doing this is to use methods to generate individual summary statistics for the columns of numerical data in the Dataframe: examples include the .mean() and .max() methods, used to calculate the mean value and max value, respectively, of each column of numerical data in the dataframe.

It is possible, however, to produce numerous summary statistics with one command by using the *.describe()* method. I used this method here, where I looked for summary statistics for:
1. each of the four measured traits ('sepal width', 'sepal height', 'petal width' and 'petal height') for all of the flowers as a group (sample size = 150), and
2. each of the four measured traits for *each* variety of Iris flower (3 groups each of sample size = 50).

I generated the second set of statistics because I was interested in seeing how different the statistics would be for each Iris variety in isolation. I used the pandas *groupby()* function in conjunction with the *.describe* method to generate these statistics. I also used the NumPy method *np.transpose()* to invert the way the summary statistics were printed, because when printed without inverting them, the results are not easily readible on the outputted text file.

The statistical properties measured are as follows:

* count: The count for the group as a whole was 150 samples, while the count for each class was 50 samples. Each sample had 4 variables measured.

* mean (average): For the group as a whole, sepal length has the highest average length (5.843 cm), followed by petal length (3.756 cm), then sepal width (3.05 cm), and finally petal width gave the lowest average length (1.2 cm). \
This ranking held for each of the three Iris varieties of Setosa, Versicolor and Virginica, but it is interesting to see how much smaller the numbers are for Iris Setosa compared to the other two varieties.

* standard deviation: This is a measure of the dispersion of the values of a given set a data. The value for standard deviation calculated by pandas is calculated using a population size of (N - 1) rather than (N), and this (N - 1) formula is suitable for the relatively small population sizes of 50 and 150 being analysed here.
The Coefficient of Variation (CoV), which measures the extent of standard deviation of a sample relative to the mean of the sample, is useful to give a sense of how variable a given trait is. The CoV is calculated as (sd/ mean), and among the sample of 150 flowers, the figure for CoV for sepal length and sepal width are remarkable similar, at 0.141, which is a much lower measure of variability than the figures for petal length (0.469) and petal width (0.637). 
Note: as CoV isn't directly calculated by the *.decribe()* method, I calculated them using the *.mean()* and *.std()* methods and printed the results to the text file.

* min: the smallest value, in cm, for the trait being measured. The smallest value for each trait within the group as a whole are as follows:
sepal length (4.3 cm), sepal width (2 cm), petal length (1 cm) and petal width (0.1 cm). \
For sepal length, petal length and petal width, Iris Setosa was the variety which was responsible for the smallest value, although for sepal width, the variety with the smallest value was Iris Versicolor.

* 50th percentile (median): the value for the trait being measured, which lies at the midpoint of all values for the trait (50% of values are above this value, and 50% of values are below it). Within the group as a whole, the median value for each of the four traits followed the same ranking as the mean, with the longest median being that of the sepal length (5.8 cm), followed by petal length (4.35 cm), sepal width (3 cm) and petal width (1.3 cm). We can see that the values for the median for three of the four traits are quite close to the values for the mean, but for petal length, the mean is significantly lower (3.756 cm compared to 4.35 cm): this can be explained by the much lower values for the petal length of Iris Setosa compared with Iris Versicolor and Iris Virginica.

* 25th and 75th percentile: For these values, we can see that, within the overal sample of 150 flowers, the values constituting the 25th percentile for petal length and petal width deviate much more from the median than is the case for the sepal length and sepal width. A quick look at the summary statistics for petal length and petal width for the three varieties in isolation shows us that the values for these traits are significantly lower in Iris Setosa compared with Iris Versicolor and Iris Virginica, and these lower figures drag down the figure for 25th percentile for each of these traits.
The summary statistics for Iris Versicolor and Iris Virginica do not differ as greatly between each other and either do from Iris Setosa (although Iris Virginica seems to have, overall, larger measurements than Versicolor for it's four traits); due to this, the figures for the 75th percentile values are not as distant from the median as the 25th percentile figures are. \
These values will be illustrated by boxplots later in the project.

* max: the largest value, in cm, for the trait being measured. The largest value for each trait within the group as a whole are as follows:
sepal length (7.9 cm), petal length (6.9 cm), sepal width (4.4 cm) and petal width (2.5 cm). \ 
For sepal length, petal length and petal width, Iris Virginica was the variety which was responsible for the largest value, although for sepal width, the variety with the largest value was Iris Versicolor.


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
