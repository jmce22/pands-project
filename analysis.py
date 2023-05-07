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
# provide a high-level picture of which traits are the most variable within the population as a whole.

    meansl = df["sepal length"].mean()
    sdsl = df["sepal length"].std()
    meansw = df["sepal width"].mean()
    sdsw = df["sepal width"].std()
    meanpl = df["petal length"].mean()
    sdpl = df["petal length"].std()
    meanpw = df["petal width"].mean()
    sdpw = df["petal width"].std()
    

    print("Summary statistics for the four variables measured for the Iris data set")
    print("\n\n")
    print(summary)
    print("\n\n")
    print("Here are some summary statistics for each class of Iris flower: \n")
    print(summary_by_class)
    print("\n")
    print("The coefficient of variation for each trait is as follows: \n")
    print(f'Sepal length: CoV = {sdsl/meansl}')
    print(f'Sepal width: CoV = {sdsw/meansw}')
    print(f'Petal length: CoV = {sdpl/meanpl}')
    print(f'Petal width: CoV = {sdpw/meanpw}')
    print("\n\n")
    print("For a description of these summary statistics, please see the README file for this project.")

    f.close()

# this calls the function defined above
summary_statistics()



# the first ten rows of the dataframe
# print(df.head(10))

# general overview of dataframe
# print(df.info())

# the index labels of the dataframe
# print(df.index)

# the column lables of the dataframe
# print(df.columns)

# numpy representation of the dataframe
# print(df.values)

# size of dataframe (number of elements in it)
# print(df.size)

# summary statistics
# print(df.describe())

# df.hist(bins = 20)
# plt.savefig('histograms.png')
# plt.show()

#df.hist(x = 'petal length', y = 'iris setosa')
#plt.show()

sns.set(style="darkgrid")
sns.displot(df, x = 'petal length', kde = False)
plt.savefig('petal_length_hist.png')
plt.show()

#sns.set(style="darkgrid")
#sns.displot(df, x = 'petal width', kde = False)
#plt.savefig('petal_width_hist.png')

#sns.set(style="darkgrid")
#sns.displot(df, x = 'sepal length', kde = False)
#plt.savefig('sepal_length_hist.png')

#sns.set(style="darkgrid")
#sns.displot(df, x = 'sepal width', kde = False)
#plt.savefig('sepal_width_hist.png')

#sns.pairplot(df)
#plt.savefig('iris_pairplot.png')

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

 
