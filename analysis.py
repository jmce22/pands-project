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
# other output from the terminal.
def summary_statistics():


# The function sys.stdout allows us to redirect the print statements contained within it to a text file
# Reference: https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
    f = open("summary statistics.txt", 'w')
    sys.stdout = f

# The groupyby function in pandas allows us to split the dataframe into groups separated according to the data in the column 'variety'. 
# We can then generate summary statistics for each class of Iris in the dataset.
# Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/ 
    summary_statistics_class = df.groupby("variety").describe()


# This firstly transposes the output of the .describe() method, to make it easier to read it when it is printed out. 
# This transposed output is then converted into a string, to allow us to print it to a text file using 'with open'.
# Reference: https://www.digitalocean.com/community/tutorials/numpy-matrix-transpose-array#transpose-of-an-array-like-object
# Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/


    transpose_summary_class = np.transpose(summary_statistics_class)
    summary_class_string= transpose_summary_class.to_string()

    print("Here are some summary statistics for each class of Iris flower: \n ")
    print(summary_class_string)

    f.close()

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

#df.hist(bins = 20)
#plt.savefig('histograms.png')
#plt.show()

#df.hist(x = 'petal length', y = 'iris setosa')
#plt.show()

#sns.set(style="darkgrid")
#sns.displot(df, x = 'petal length', kde = False)
#plt.savefig('petal_length_hist.png')
#plt.show()

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

#print(df.groupby('variety').mean())

#with open('summary_statistics.txt', 'w') as f:
 
