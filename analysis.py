# Importing the libraries I will use to complete the project

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# to redirect output from command line onto a text file, we need to import the sys module.
import sys

# add headings to the columns
# reference: https://realpython.com/python-csv/#reading-csv-files-with-pandas 
df = pd.read_csv("iris.data.csv", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'variety'])


# To print the summary statistics to a file, we create a function where all of the print statements contained within get printed to
# the text file when the function is called. This will allow us to just print the summary statistics to the text file and none of the
# other output from the script which will be in the terminal.
def summary_statistics():


# The function sys.stdout allows us to redirect the print statements contained within it to a text file
# Reference: https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
    f = open("summary statistics.txt", 'w')
    sys.stdout = f

# These three functions generate a sample of rows from the data frame (the first five, a random five and the last five rows, respectively).
# The reason for printing these out is the give me confidence that the dataframe is set up properly, showing the headings,
# where the index begins (at zero) and that it contains 150 rows. 
    first_five_rows = df.head()
    sample_five_rows = df.sample(n=5)
    last_five_rows = df.tail()

    summary_stats = df.describe()
    
    
# This firstly transposes the output of the .describe() method, to make it easier to read it when it is printed out. 
# References: https://numpy.org/doc/stable/reference/generated/numpy.transpose.html 


    transpose_summary = np.transpose(summary_stats)
    summary= transpose_summary

    
# The groupyby function in pandas allows us to split the dataframe into groups separated according to the data in the 
# column with heading 'variety'. 
# We can then generate summary statistics for each class of Iris in the dataset.
# Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/ 
    
    summary_stats_by_class = df.groupby("variety").describe()
    transpose_summary_class = np.transpose(summary_stats_by_class)
    summary_by_class= transpose_summary_class


# I have added calculations for the Coefficient of Variation summary statistic to the outputted text file, 
# because this statistic isn't provided directly by the .decribe() method, but I feel this is a useful statistic to 
# provide a high-level picture of which traits are the most variable within the sample as a whole.

    meansl = df["sepal length"].mean()
    sdsl = df["sepal length"].std()
    meansw = df["sepal width"].mean()
    sdsw = df["sepal width"].std()
    meanpl = df["petal length"].mean()
    sdpl = df["petal length"].std()
    meanpw = df["petal width"].mean()
    sdpw = df["petal width"].std()


# I have also added the skewness of each trait among the population, to get an idea of how close to normal the distribution
# of each trait is.
    skewsl = df["sepal length"].skew()
    skewsw = df["sepal width"].skew()
    skewpl = df["petal length"].skew()
    skewpw = df["petal width"].skew() 

    print("Below are some samples of rows of data found within the data frame.") 
    print("These reassure us that the dataframe has been created correctly, with appropriate headings,\ncapturing all data as expected, and taking a consistent form throughout.")
    #print(dataframe_info)
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
    print("The coefficient of variation for each trait within the sample as a whole is as follows: \n")
    print(f'Sepal length: CoV = {sdsl/meansl}')
    print(f'Sepal width: CoV = {sdsw/meansw}')
    print(f'Petal length: CoV = {sdpl/meanpl}')
    print(f'Petal width: CoV = {sdpw/meanpw}')
    print("\n\n")
    print("The skewness of each trait within the sample as a whole is as follows: \n ")
    print(f'Sepal length: Skewness = {skewsl}')
    print(f'Sepal width: Skewness = {skewsw}')
    print(f'Petal length: Skewness = {skewpl}')
    print(f'Petal width: Skewness = {skewpw}')
    print("\n\n")
    print("For a description of these summary statistics, please see the README file for this project.")

    f.close()

# this calls the function defined above
summary_statistics()


# The below section of this script generates the histograms for the project.

# Reference: https://seaborn.pydata.org/tutorial/distributions.html?highlight=histogram
# Reference: https://r02b.github.io/seaborn_palettes/ 

sns.set(style="darkgrid")

sepal_length = sns.displot(df, x ="sepal length", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Sepal length for each Iris variety", xlabel = "Sepal length in cm")
plt.tight_layout()
plt.savefig('sepal_length_varieties.png')


sepal_width = sns.displot(df, x ="sepal width", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Sepal width for each Iris variety", xlabel = "Sepal width in cm")
plt.tight_layout()
plt.savefig('sepal_width_varieties.png')


petal_length = sns.displot(df, x ="petal length", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Petal length for each Iris variety", xlabel = "Petal length in cm")
plt.tight_layout()
plt.savefig('petal_length_varieties.png')


petal_width = sns.displot(df, x ="petal width", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Petal width for each Iris variety", xlabel = "Petal width in cm")
plt.tight_layout()
plt.savefig('petal_width_varieties.png')


# This section of my script relates to scatterplots. To capture the 6 different trait-pair combinations, I have used a pairplot.
# I created a pairplot based on the data set as a whole which show the correlation between the 6 different pairs of traits
# within the whole sample, and also created three pairplots where each is based only on the data relating to a single Iris species.


sns.set(style = "white")

sns.pairplot(df, hue = "variety", palette="Dark2", height=2, aspect=1.5)
plt.savefig('iris_pairplot.png')


# The df.loc[] property allows us to create three 'sub-DataFrames' from the overall Dataframe, based on the condition 
# that the entry in the 'variety' column equals one of the three varieties of Iris. I will then assign it to a variable 
# and use that variable to create pairplots for each trait within each class of Iris flower. 
# Reference: https://sparkbyexamples.com/pandas/pandas-dataframe-loc/

setosa = df.loc[df['variety']=="Iris-setosa"]
versicolor = df.loc[df['variety']=="Iris-versicolor"]
virginica = df.loc[df['variety']=="Iris-virginica"]

#sns.pairplot(df, vars=["sepal width", "sepal length"])
#plt.savefig("sepal_pairplot.png")

sns.pairplot(setosa)
plt.savefig('setosa_pairplot.png')

sns.pairplot(versicolor)
plt.savefig('versicolor_pairplot.png')

sns.pairplot(virginica)
plt.savefig('virginica_pairplot.png')


# boxplots:

#sns.set_style('whitegrid')
#sns.boxplot( y=df['sepal length'], x=df['variety'])
#plt.savefig('sepal_length_boxplot')

#sns.set_style('whitegrid')
#sns.boxplot( y=df['sepal width'], x=df['variety'])
#plt.savefig('sepal_width_boxplot')

#sns.set_style('whitegrid')
#sns.boxplot( y=df['petal length'], x=df['variety'])
#plt.savefig('petal_length_boxplot')

#sns.set_style('whitegrid')
#sns.boxplot( y=df['petal width'], x=df['variety'])
#plt.savefig('petal_length_boxplot')

#sns.violinplot(x=df["sepal length"])
#plt.savefig('sepal length violin')

#sns.kdeplot(x=df['sepal length'])
#plt.savefig('kde_plot')

 
