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


#sns.set(style="darkgrid")
#sns.displot(df, x = 'petal length', kde = False)
#plt.savefig('pet_len_hist.png')

#sns.set(style="darkgrid")
#sns.displot(df, x = 'petal width', kde = False)
#plt.savefig('pet_wid_hist.png')

#sns.set(style="darkgrid")
#sns.displot(df, x = 'sepal length', kde = False)
#plt.savefig('sep_len_hist.png')

#sns.set(style="darkgrid")
#sns.displot(df, x = 'sepal width', kde = False)
#plt.savefig('sep_wid_hist.png')

#sns.pairplot(df)
#plt.savefig('iris_pairplot.png')

# boxplots:

#sns.set_style('whitegrid')
#sns.boxplot( y=df['sepal length'], x=df['variety'])
#plt.savefig('sep len boxplot')

sns.set_style('whitegrid')
sns.boxplot( y=df['sepal width'], x=df['variety'])
plt.savefig('sep wid boxplot')

sns.set_style('whitegrid')
sns.boxplot( y=df['petal length'], x=df['variety'])
plt.savefig('pet len boxplot')

sns.set_style('whitegrid')
sns.boxplot( y=df['petal width'], x=df['variety'])
plt.savefig('pet len boxplot')