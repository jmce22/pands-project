# Importing the libraries I will use to complete the project

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

# add headings to the columns
# reference: https://realpython.com/python-csv/#reading-csv-files-with-csv
data = pd.read_csv("iris.data.csv", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'variety'])

#print(data)

sns.set(style="darkgrid")
df = sns.load_dataset('iris')
sns.histplot(df['petal_length'],kde = False)
plt.show()