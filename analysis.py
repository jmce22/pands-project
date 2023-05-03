# Importing the libraries I will use to complete the project

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

# add headings to the columns
# reference: https://realpython.com/python-csv/#reading-csv-files-with-pandas 
df = pd.read_csv("iris.data.csv", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'variety'])

# print(df)

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
