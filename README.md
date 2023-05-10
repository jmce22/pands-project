# pands-project

---

### **Name: James McEneaney**
### **Course: Higher Diploma in Computing in Data Analytics, ATU Ireland**
### **Semester: Semester 1 2023**

---

This repository contains my submission for the project for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU.
This project involves researching Fisher's Iris data set and carrying out exploratory data analysis on it using Python.

I used Visual Studio Code (version 1.77.3) to write my scripts and to uploaded them to a repository on github for assessment.

This file will firstly give some background information to the dataset in question. 

I will then outline the steps which I needed to take before I could begin the actual analysis itself: downloading the data-set, preparing the dataset by adding the correct headings, and importing the modules, libraries and packages which I used for the project.

Next I will outline some summary statistics relating to the variables within the dataset. 
My script will redirect the summary statistics for each of the four variables on to a text file.

I will then carry out data visualisation on the Iris dataset, using histograms, scatterplots and some other types of plots. My script will save each plot generated from the data as a .png file, and these can be viewed below. I will discuss my interpretations of the histograms and plots.

My project will conclude with an overall summary of my findings, and my thoughts upon conclusion of the project. I will also provide a list of references which I used to complete my work.

**To execute my script**:
Please download *analysis.py* from my repository (*jmce22/pands-project*) into a code editor such as VS Code. While located in the folder in which you have saved *analysis.py*, go to the terminal window and type 'python analysis.py'. This should run the code and generate the text file with summary data for the dataset, and print into the folder the histograms, pairplots and other plots which analyse the data.

&nbsp; 

## Table of contents
* [Background of dataset](#background-of-dataset)
* [Pre-analysis](#pre-analysis)
* [Summary of each variable](#summary-of-each-variable)
    * [Explanation of code](#explanation-of-code)
    * [Outline of summary statistics](#outline-of-summary-statistics)
* [Histograms](#histograms)
    * [Background](#background)
    * [Explanation of code](#explanation-of-code)
    * [Histograms](#histograms)
    * [Interpretation of findings](#interpretation-of-findings)
* [Plots](#plots)
    * [Background](#background)
    * [Explanation of code](#explanation-of-code)
    * [Pairplots](#pairplots)
    * [Interpretation of findings](#interpretation-of-findings)
* [Other analysis](#other-analysis)
* [Summary](#summary)
* [References](#references)

&nbsp; 

## Background of dataset


The data set was collected in 1935 by the American botanist Edgar Anderson, and used in 1936 by the British statistician and biologist Ronald A. Fisher. It relates to data collected from samples of three species of the Iris flowering plant genus: Iris setosa, Iris virginica, and Iris versicolor. \
It is commonly used as an introductory data set by people who are learning how to analyse and visualise data using programming languages.

Fifty samples were collected for each species, giving one hundred and fifty samples in total. \
For each sample, four features of the flower were measured; these were: sepal length, sepal width, petal length and petal width. These attributes of the samples are contained in columns 1, 2, 3 and 4 respectively within the dataset. The species name of the flower is also included in the dataset in column 5.

The petal of a flowering plant are the leaves of the flower which surround the reproductive parts of the flower, and which are often brightly coloured to attract pollinators. Sepals usually protect the flower when it is in a bud and structurally support the petals when the flower is in bloom.

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
* Iris setosa
* Iris versicolour
* Iris virginica

To enable me to analyse the dataset, I imported some libraries and modules commonly used for this purpose. 

code for importing modules and libraries :
```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

```

These were as follows:

* *Matplotlib* is a library used by Python to make plots and graphs. It requires NumPy to run. *Matplotlib.pyplot* is a collection functions which allows us to do different things to the plots we make, such as create them, add headings, change the colour scheme etc.

* *NumPy* (Numerical Python) is a package used in Python to carry out mathemetical operations on numerical datatypes, such as integers and floating-point numbers. It creates multi-dimensional array objects which allow Python to carry out mathemetical operations much more efficiently than would be the case in Python without NumPy. 

* *pandas* is built on top on NumPy, and is a powerful and flexible Python package used for data analysis, especially of tabular data, such as the data in the .csv file used for this project. I used pandas to open the Iris dataset. Pandas creates data-structures which allow data to be manipulated, with the most important being 1-dimensional data 'series' and 2-dimensional 'DataFrames' (the structure which is used here to manipulate the Iris data). The DataFrame in pandas stores data as a two-dimensional structure where each piece of information has a row and column label.

* *Seaborn* is built on top of matplotlib. It enables us to make more appealing plots, utilising different styles.

* The *sys* module contains different methods and variables which allow us to interact with the environment in which we are executing the Python code. For example, the *sys.stdout* method (which I used in this project) provides the functionality to print script output from the terminal on to an external text document, where it can be read.

I then created a pandas DataFrame object to use in my analysis. I did this by reading the .csv file with pandas and assigning names to each colum, based on the information available on the website I downloaded the .csv file from.

code for creating DataFrame object from data in .csv file, and assigning variable name 'df' to DataFrame:
```
df = pd.read_csv("iris.data.csv", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'variety'])
```

&nbsp; 

## Summary of each variable

### Explanation of code ###

Using pandas, we can generate various summary statistics of the data contained in a pandas DataFrame object. For this project, we were instructed to *"output a summary of each variable to a text file"*, and I found this a challenge initially. I spent time trying to work out a way to do this by converting the summary statistics to a string using the *to.string()* method and then writing them to the text file using *"with open("summary.txt", "w") as f"* to open the file. However, I found a very useful piece of code on the site https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file to write the output of the terminal to the txt file.

```
import sys
f = open("test.out", 'w')
sys.stdout = f
print "test"
f.close()
```

This code allows all print statements printed within it to be printed to the file specified in *f = open()*. Since I only wanted the summary statistics to be printed to the text file (and none of my script relating to the other sections) I created a function called summary_statistics and enclosed the above code within it. I made sure to call the function outside of the code also.

Before setting out to analyse the dataset, I wanted to ensure that the DataFrame had been created properly and that I could be confident that I could use it to generate accurate summary statistics. For this purpose, I printed the first five rows, a random five rows and the last five rows of the DataFrame, and this allowed me to see that the headings were applied correctly, that the index ranges from 0 to 149 (and therefore contains 150 values) and that the contents of the DataFrame seem to be a full 5 x 150 array. To do this, I used the *.head()*, *.sample()* and *.tail()* methods on the DataFrame.

One way of compiling summary statistics for a DataFrame is to use seperate methods to generate seperate individual summary statistics for the columns of numerical data in the DataFrame: examples include the *.mean()* and *.max()* methods, used to calculate the mean value and max value, respectively, of each column of numerical data in the DataFrame.

It is possible, however, to produce multiple summary statistics with one command by using the *.describe()* method. I used this method here, where I looked for summary statistics for:  \
i). each of the four measured traits ('sepal width', 'sepal length', 'petal width' and 'petal length') for all of the flowers as a group (sample size = 150), and
ii). each of the four measured traits for *each* variety of Iris flower (three groups, each with a sample size of 50).

I generated the second set of statistics because I was interested in finding out how different the statistics would be for each Iris variety in isolation. I used the pandas *groupby()* function in conjunction with the *.describe* method to generate these statistics. I also used the NumPy method *np.transpose()* to invert the way the summary statistics were printed, because when printed without inverting them, the results are not easily readible on the outputted text file. I used https://numpy.org/doc/stable/reference/generated/numpy.transpose.html to work this out and was relieved when it produced a good result.

Below is the code I used for this section:


```

def summary_statistics():

    f = open("summary statistics.txt", 'w')
    sys.stdout = f

    first_five_rows = df.head()
    sample_five_rows = df.sample(n=5)
    last_five_rows = df.tail()

    summary_stats = df.describe()

    transpose_summary = np.transpose(summary_stats)
    summary= transpose_summary

    summary_stats_by_class = df.groupby("variety").describe()
    transpose_summary_class = np.transpose(summary_stats_by_class)
    summary_by_class= transpose_summary_class

    meansl = df["sepal length"].mean()
    sdsl = df["sepal length"].std()
    meansw = df["sepal width"].mean()
    sdsw = df["sepal width"].std()
    meanpl = df["petal length"].mean()
    sdpl = df["petal length"].std()
    meanpw = df["petal width"].mean()
    sdpw = df["petal width"].std()

    skewsl = df["sepal length"].skew()
    skewsw = df["sepal width"].skew()
    skewpl = df["petal length"].skew()
    skewpw = df["petal width"].skew() 

    print("\n\n")
    print("Below are some samples of rows of data found within the data frame.") 
    print("These reassure us that the dataframe has been created correctly, with appropriate headings,\ncapturing all data as expected, and taking a consistent form throughout.")
    print("\n")
    print("First five rows: ")
    print(first_five_rows)
    print("\n")
    print("A random sample of five rows: ")
    print(sample_five_rows)
    print("\n")
    print("Last five rows: ")
    print(last_five_rows)
    print("\n\n")
    print("Below are some summary statistics for the four variables measured for the Iris data set: ")
    print(summary)
    print("\n\n")
    print("Here are the same summary statistics for each class of Iris flower: \n")
    print(summary_by_class)
    print("\n\n")
    print("The coefficient of variation for each trait within the sample as a whole is as follows: ")
    print(f'Sepal length: CoV = {sdsl/meansl}')
    print(f'Sepal width: CoV = {sdsw/meansw}')
    print(f'Petal length: CoV = {sdpl/meanpl}')
    print(f'Petal width: CoV = {sdpw/meanpw}')
    print("\n\n")
    print("The skewness of each trait within the sample as a whole is as follows: ")
    print(f'Sepal length: Skewness = {skewsl}')
    print(f'Sepal width: Skewness = {skewsw}')
    print(f'Petal length: Skewness = {skewpl}')
    print(f'Petal width: Skewness = {skewpw}')
    print("\n\n")
    print("Finally, here are the correlation coefficients for each pair of traits: ")
    print("Sepal length vs Sepal width: ", np.corrcoef(df['sepal length'], df['sepal width'])[0,1])
    print("Petal length vs Petal width: ",  np.corrcoef(df['petal length'], df['petal width'])[0,1], "\n")
    print("Sepal length vs Petal length: ", np.corrcoef(df['sepal length'], df['petal length'])[0,1])
    print("Sepal width vs Petal width: ", np.corrcoef(df['sepal width'], df['petal width'])[0,1], "\n")
    print("Sepal length vs Petal width: ",  np.corrcoef(df['sepal length'], df['petal width'])[0,1])
    print("Sepal width vs Petal length: ",  np.corrcoef(df['sepal width'], df['petal length'])[0,1])
    print("\n\n")
    print("For a description of these summary statistics, please see the README file for this project.")

    f.close()

summary_statistics()

```

### Outline of summary statistics ###

Below I give a description of the statistical properties measured and an overview of the figures obtained for this dataset:

* *count*: This returns the number of 'non-empty' values for each column of numerical values. In this case, each 'trait' column was shown to contain 150 samples, while the count within each 'trait' column for each class of Iris was 50 samples. Each sample had 4 traits measured. This statistic reassures us that there are no null values in the dataset.

* *mean* (average): For the group as a whole, sepal length has the highest average length (5.843 cm), followed by petal length (3.756 cm), then sepal width (3.05 cm), and finally petal width gave the lowest average length (1.2 cm).  \
This ranking held for each of the three Iris varieties, but it is interesting to see how much smaller the measurements are for Iris Setosa compared with the other two varieties.

* *min*: the smallest value, in cm, for the trait being measured. The smallest measurement for each trait within the group as a whole are as follows:
sepal length (4.3 cm), sepal width (2 cm), petal length (1 cm) and petal width (0.1 cm).  \
For sepal length, petal length and petal width, Iris setosa was the variety which was responsible for the smallest value, while for sepal width, the variety with the smallest value was Iris versicolor.

* *50th percentile* (median): here, the median value for a trait being measured is that value which lies at the midpoint of all values for the trait (50% of values are above this value, and 50% of values are below it). Within the group as a whole, the median value for each of the four traits followed the same ranking as the mean, with the largest median value being that for the sepal length (5.8 cm), followed by petal length (4.35 cm), sepal width (3 cm) and petal width (1.3 cm).  \
We can see that the values for the median for three of the four traits are quite close to the values for the mean, but for petal length, the mean is significantly lower (3.756 cm compared to 4.35 cm): this can be explained by the much lower values for the petal length of Iris setosa compared with Iris versicolor and Iris virginica. In this case of petal width, the mean and median values for setosa are significantly lower than those for versicolor, while the mean and median for virginica are significantly higher, with the result that the median and mean for the group overall is closest to the mean and median of versicolor.

* *25th and 75th percentile*: For these values, we can see that, within the overal sample of 150 flowers, the values constituting the 25th percentile for petal length and petal width deviate much more from the median than is the case for the sepal length and sepal width. A quick look at the summary statistics for petal length and petal width for the three varieties in isolation shows us that the values for these traits are significantly lower in Iris setosa compared with Iris versicolor and Iris virginica, and these lower figures for setosa drag down the figure for 25th percentile for each of these traits.  \
The summary statistics for versicolor and virginica do not differ as greatly between each other as either do from setosa (although virginica seems to have, overall, larger measurements than versicolor for its four traits); as a result, the figures for the 75th percentile values are not as distant from the median as the 25th percentile figures are. These values will be illustrated by boxplots later in the project.

* *max*: the largest value, in cm, for the trait being measured. The largest value for each trait within the group as a whole are as follows:
sepal length (7.9 cm), petal length (6.9 cm), sepal width (4.4 cm) and petal width (2.5 cm).
For sepal length, petal length and petal width, virginica was the variety which was responsible for the largest value, although for sepal width, the variety with the largest value was setosa.

* *standard deviation*: This is a measure of how far the values of a given dataset tend to lie from the mean of the values of the dataset. The value for standard deviation calculated by pandas is calculated using a population size of (N - 1) rather than (N), and this (N - 1) formula is suitable for the relatively small population sizes of 50 and 150 being analysed here. Rather than analyse the figures for standard deviation in isolation, I thought it would be more appropriate to calculate the coefficient of variation for each trait instead (see below), as this gives a more meaningful picture of the degree of dispersion of values for each trait and allow us to better compare results between traits.

* The *Coefficient of Variation (CoV)*, or relative standard deviation, measures the extent of standard deviation of a sample relative to the mean of the sample, is useful to give a sense of how variable a given trait is. The CoV is calculated as (sd/ mean), and among the sample of 150 flowers, the figure for CoV for sepal length and sepal width are remarkable similar, at 0.141, which is a much lower measure of variability than the figures for petal length (0.469) and petal width (0.637).  \
From looking at the histograms (next section) for petal length and petal width, it is clear that the values for these two petal traits for setosa are much lower than they are for versicolor and virginica, and the aggregation of approximately two thirds of the datapoints to the right hand-side of the histogram, and one third to the left hand side, causes the mean value to deviate more on average from the values of the datapoints than is the case for either of the two sepal traits (both of which display more balanced distributions in their histograms).  \
Note: as CoV isn't directly calculated by the *.describe()* method, I calculated them using the *.mean()* and *.std()* methods and printed the results to the text file.

* *Skewness*: I generated figures for the skewness of the distrubution for values for each trait within the dataset. I did this using the code DataFrame['column name'].skew().  \
Skewness measures the degree of asymmetry of a distribution, with a value of zero representing a normal distribution. A negative value for skewness indicates that the distribution is left-skewed, with the left-tail long relative to the right. A positive value indicates the opposite; that the distribution is right-skewed and therefore the right-tail is longer relative to the left. A value which lies between -0.5 and 0.5 is considered to represent a fairly symmetrical plot, and all four traits fall within this range for skewness.  \
For petal length and petal width, the values for skewness are slightly negative (-0.274 and -0.105, respectively), indicating that there is a slight weighting of values for these traits towards the right (and a correspondingly longer left-tail): this can be explained by the significantly higher values for these traits found in Iris vertosa and Iris virginica than are found in Iris setosa.  \
For sepal length and sepal width, the values for skewness are slightly positive (0.315 and 0.334, respectively), which shows that there is a slight weighting of the values for these traits towards the left: from looking at the histograms for sepal length and sepal width, we can see that the values for sepal length trail to the right mostly due to the higher measurements for Iris virginica, and the values for sepal width trail to the right due to the higher measurements for Iris setosa.

* *Correlation coefficients*: I included the correlation coefficient, 'r', for each of the six pairs of traits. This statistic, which always lies between -1 and 1, is explained in the Plots section, along with the figures generated for trait-pairs for the overall Iris dataset. I mention them here because I have outputted the figures to the summary statistics text file.



&nbsp; 

## Histograms

### Background ###

To begin visualising the data, I created four histograms using Seaborn. A histogram is a chart used to depict the frequency at which different values occur within a dataset. It does this using narrow vertical bars, or 'bins', of equal width, where each bin represents a range of values. Data points from the dataset are placed in a bin according to their value and the number of data points which fall into each bin is counted on the y-axis. This produces a useful visual representation of the spread of values within a dataset.

### Explanation of code ###

I decided to create one histogram for each trait, and to include on each histogram the contribution of each Iris flower to the data in the histogram. I achieved this passing the *hue* argument into the sns.displot function which I used to generate each histogram: this allowed me to split the histogram into three different colours, with the colours denoting which species of Iris the data belongs to (ie. which value is found in the "variety" column on the same row of the DataFrame as the point of data being included in the histogram). 

I then specified that the histograms should be stacked on top of each other, rather than overlapping each other, as I found that this enabled me to more easily get a sense of how the data is distributed: to create these stacked histograms, I passed the argument *multiple = stack* into the function *sns.displot*.

I added a title and changed the label on the x-axis by appending the *.set()* function to the sns.displot function. I also improved the appearance of each histogram by using the *plt.tight_layout()* to increase the amount of space for the heading at the top. I then saved each histogram as a .png file and these are included below:

code used to create histograms:

```
sns.set(style="darkgrid")

sepal_length = sns.displot(df, x ="sepal length", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Sepal length for each Iris variety", xlabel = "Sepal length in cm")
plt.tight_layout()
plt.savefig('sepal_length_hist.png')

(similar code for the three other histograms)

```

### Histograms ###

**i) Petal length **

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/petal_length_hist.png)

**ii) Petal width **

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/petal_width_hist.png)

**iii) Sepal length **

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/sepal_length_hist.png)

**iv) Sepal width: **

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/sepal_width_hist.png)


### Interpretation of findings ###

The most obvious visual result from the histograms are the *much* smaller values for petal length and petal width for Iris setosa compared to Iris versicolor and Iris virginica. It is also clear that virginica has larger petals overall compared to versicolor.

In terms of sepal length and sepal width, the ranking of size from smallest to largest measurements (setosa < versicolor < virginica) holds for sepal length, albeit to a less marked degree than for either of the petal characteristics. However, for sepal width, it appears that setosa has the largest measurements overall, with the measurements for versicolor and virginica being noticeably lower, with virginica having slightly higher values for sepal width than versicolor overall.


&nbsp; 

## Plots

### Background ###

A scatterplot is a type of plot in which the values of two variables are plotted seperately along the x-axis and the y-axis, and the pattern of the plot can be used to determined the degree to which the two variables are correlated. A figure known as the sample correlation coefficient, 'r', can be calculated between two variables to put a figure on the degree of correlation, and it lies between -1 and 1. Regression lines ('line of least squares' or 'line of best fit') can be drawn through the plot, to visually illustrate the degree of correlation between the variables. This is the line that minimises the sum of distances between the data points and the line.

* If x tends to increase while y increases, x is said to be positively correlated with y, and r > 0. This is indicated by a positively sloping line from the bottom left corner of the axis. A 45-degree angle with the x-axis indicates a perfect positive correlation between variables.
* If x tends to decrease while y increases, x is said to be negatively correlated with y, and r < 0. This is indicated by a negatively sloping line from the top left corner of the axis. A 45-degree angle with the x-axis indicates a perfect negative correlation between variables.
* A figure close to zero implies little or no correlation between the variables and is indicated by a flat or almost-flat line through the middle of the plot.
These three scenarios are illustrated in the image below:  


&nbsp; 


![image](https://raw.githubusercontent.com/jmce22/pands-project/main/correlation_coeff.png)


&nbsp; 

### Explanation of code ###

To capture the six different trait-pair combinations within this sample I have used pairplots. Pairplots combine multiple scatterplots into one plot. I created a pairplot based on the data set as a whole to show the correlation between the 6 different pairs of traits within the whole sample, and also created three further pairplots to depect the correlation between traits for each Iris species in isolation.

In order to create the three pairplots for the individual Iris species, I needed to split the dataset into three sub-datasets. To do this, I used the *df.loc[]* property to create three 'sub-DataFrames' from the overall Dataframe. I split the dataset based on the condition that the entry in the 'variety' column equals one of the three varieties of Iris (for example, *df['variety']=="Iris-setosa"*). I then assigned each sub-DataFrame to an appropriate variable name for use in the formulas for the pairplots for each Iris species. I found this code within this page: https://sparkbyexamples.com/pandas/pandas-dataframe-loc/

I modified my plots to enhance their appearance and to make them easier to interpret. I used the *corner* argument to removes the top right corner of each pairplot, as the top right corner showed redundant information which I felt cluttered the appearance of the plot and made it harder to interpret. 

To produce a clearer picture of the strength of correlation between the different traits, I wanted to include regression lines in my pairplots. Initially, I used the *kind = "reg"* argument in all four of my plots to insert regression lines into each non-diagonal segment. I really liked the regression lines in the individual Iris pairplots, as the bold colours of the plots and data points against the white background make it easy to interpret the nature of the relationship between the traits. However, I wasn't satisfied with the result for the overall pairplot, as the *kind = reg"* argument led to three regression lines in each segment (one for each Iris species) rather than just one regression line per segment, as I wanted. I turned to the website stackoverflow for help, and I asked my first question on it: https://stackoverflow.com/questions/76217544/how-to-fit-regression-lines-on-each-non-diagonal-segment-of-a-pairplot-while-re.  

It turned out that I couldn't simultaneously split the data into three groups using the *hue* argument, while also imposing just one regression line per segment using the *kind = "reg"* argument. The contributor (username: "Redox") defined a function called 'regline', which plots a single regression line: this function is then passed into the *.map_offdiag()* function, which enables us to apply the 'regline' function to each non-diagonal segment of the pairplot. By using *x=x.name* and *y=y.name*, we convert each trait name to a string, and each combination of traits can have a regression line imposed on the plot of their values, because the function takes the names of the traits from the x and y axes of the pairplot. Values for 'data' and 'color' are given for the regline function when it is called.

I found the quick response the my question on stackoverflow to be very helpful, as I had spent a lot of time to no avail trying to figure out how to achieve this outcome with the overall pairplot. I will consider using the site in future to get help with coding problems if I am really stuck.

I experimented with many different colours for the plots. For the overall plot, I passed in the  the *hue* argument to seperate the datapoints by 'variety' of Iris, and then passed in the *palette* argument with the palette "Dark2", to produce a distinct colour scheme for the plot. For the individual species plots, I needed to pass in separate "keyword arguments" for the diagonal component (*diag_kws = dict(color = )*) and for the plots (*plot_kws = dict(color = )*). I figured our how to modify the colors of the invidual plots in this way from watching the following youtube video (especially around 11 mins in): https://www.youtube.com/watch?v=-eyiVTLJuqI.
The diagonal component of each pairplot gives an overview of the distribution pattern for each individual trait, but as I was more interested in the comparison of each trait with the other traits, I chose to make the diagonal component grey for each plot. I then choose bold and distinct colours for the other componetns of each plot.

I also experimented with different figures for height and aspect, and settled on a height of '3' and an aspect of '1', as I felt these dimensions resulted in a desirable size for the plots when I uploaded them to this Readme document (aspect is the extent to which the horizontal dimension of the plot is multiplied by the given height).

I also added a title using the fig.suptitle() method, and increased the fontsize of the title.


Below is the code I used for this section:


```
sns.set(style = "white")

iris_pairplot = sns.pairplot(df, hue = "variety", palette="Dark2", height=3, aspect=1, corner=True)

def regline(x, y, **kwargs):
    sns.regplot(data=kwargs['data'], x=x.name, y=y.name, scatter=False, color=kwargs['color'])

iris_pairplot.map_offdiag(regline, color='red', data=df)

iris_pairplot.fig.suptitle("Pairplot of traits for full Iris sample", fontsize = "xx-large")
plt.tight_layout()
plt.savefig('iris_pairplot.png')

setosa = df.loc[df['variety']=="Iris-setosa"]
versicolor = df.loc[df['variety']=="Iris-versicolor"]
virginica = df.loc[df['variety']=="Iris-virginica"]

setosa_pairplot = sns.pairplot(setosa, diag_kws = dict(color='grey'), plot_kws = dict(color = 'brown'), height=3, aspect=1, corner=True, kind = "reg")
setosa_pairplot.fig.suptitle("Pairplot of setosa traits", fontsize = "xx-large")
plt.savefig('setosa_pairplot.png')

(similar code for versicolor and virginica pairplots)

```

### Pairplots ###

My four pairplots are shown below. following the plots I have given my interpretation of their contents.

**i) Overall pairplot**

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/iris_pairplot.png)

**ii) Setosa pairplot**

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/setosa_pairplot.png)

**iii) Versicolor pairplot**

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/versicolor_pairplot.png)

**iv) Virginica pairplot**

![image](https://raw.githubusercontent.com/jmce22/pands-project/main/virginica_pairplot.png)


### Interpretation of findings ###

a) *Sepal length vs Sepal width:*
For the sample overall, the correlation coefficient is -0.109, which represents a very weak negative relationship. This is interesting, because the plot for these two traits for each Iris species in isolation show a significant positive correlation. My interpretation, from viewing the group regression line, is this: because Iris setosa has the largest sepals out of the three species and has the smallest petals, when we include it in the regression plot of sepal length vs sepal width, its high sepal values act to pivot the group regression line upwards on the left hand-side of the graph. As a result, the correlation coefficient for the group for this trait is dissimilar to that which holds for the invidiual Iris species. This may indiciate that the species are fundamentally disimilar in their traits, and in the picture I have included in this file, setosa does look quite different to versicolor and virginica.

b) *Petal length vs Petal width:*
For the sample overall, the correlation coefficient is almost perfectly positive at a value of 0.963. This result appears closest to that which is found for versicolor, although setosa and virginica also show a definite positive relationship between petal length and petal width.

*c) Sepal length vs Petal length:*
For the sample overall, the correlation coefficient is 0.872. Again, this is a very strong positive relationship, which holds for both versicolor and virginica; sepal length seems to be correlated with petal length much less strongly with setosa, although the relationship is still positive.

*d) Sepal width vs Petal width:*
For the sample overall, the correlation coefficient is -0.357. This is a moderate negative relationship. Like for sepal width and sepal length, the group correlation does not reflect the correlation found in the individual samples: versicolor and virginica each show a solid positive relationship between sepal width and petal width, with setosa also showing a moderate positive relationship. In a similar fashion as I outlined above, it seems to me that the combination of highest sepal width measurments and lowest petal width measurements on average acts to pivot the group regression line downwards. Remember that the regression line tries to minimise the distance between all the points and the line, and if there are many data points aggregated near the bottom right of the plot, the regression line will pivot downwards in that direction.

*e) Sepal length vs Petal width:*
For the sample overall, the correlation coefficient between these two traits is 0.818. This struck me as a strong correlation considering that differences in appearance of the three species, and the follow on that the petals of one species might not be strong correlated with the sepals of another species. The regression lines for the individual plots are flatter than the group line, although versicolor still shows a definite positive relationship.

*f) Petal length vs Sepal width:*
For the sample overall, the correlation coefficient betwen the two traits is -0.42. The same analysis for 'sepal width vs petal width' applies here: setosa's high values for sepal width and low values for petal length drag the group regression line towards the bottom right corner, causing the group regression line to look different to positively sloped lines for the individual traits. That said, the positive relationship for setosa is weak, virginica is a bit stronger and vertosa shows the strongest relationship between petal length and sepal width.



&nbsp; 

## Other Analysis

&nbsp; 

## Summary

&nbsp; 

## References
