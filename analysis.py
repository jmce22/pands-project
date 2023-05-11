
# This imports the libraries that I will use to complete the project
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# To redirect output from command line onto a text file, I need to import the sys module.
import sys


# Add headings to the columns
# Reference: https://realpython.com/python-csv/#reading-csv-files-with-pandas 
df = pd.read_csv("iris.data.csv", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'variety'])


# To print the summary statistics to a file, we create a function where all of the print statements contained within get printed to
# the text file when the function is called at the end of the script. 
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


# The following section of this script generates the histograms for the project.
# See Histogram section of README for explanation of code.
# Reference: https://seaborn.pydata.org/tutorial/distributions.html?highlight=histogram
# Reference: https://r02b.github.io/seaborn_palettes/ 


sns.set_theme(style="darkgrid")

sepal_length = sns.displot(df, x ="sepal length", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Sepal length for each Iris variety", xlabel = "Sepal length in cm")
plt.tight_layout()
plt.savefig('sepal_length_hist.png')

sepal_width = sns.displot(df, x ="sepal width", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Sepal width for each Iris variety", xlabel = "Sepal width in cm")
plt.tight_layout()
plt.savefig('sepal_width_hist.png')

petal_length = sns.displot(df, x ="petal length", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Petal length for each Iris variety", xlabel = "Petal length in cm")
plt.tight_layout()
plt.savefig('petal_length_hist.png')

petal_width = sns.displot(df, x ="petal width", bins = 20, hue ="variety", palette = "Set1_r", multiple = "stack").set(title = "Petal width for each Iris variety", xlabel = "Petal width in cm")
plt.tight_layout()
plt.savefig('petal_width_hist.png')


# The following section relates to scatterplots. 
# I created a pairplot for the overall Iris dataset and one each for the three Iris species in isolation.
# Please see Scatterplot section of README for an explanation of the scatterplot code.

# The use of the function 'regline' in the code for the overall Iris pairplot allowed me to have just one regression line 
# per segment in the overall Iris plot, instead of the three lines which are generated when the 'kind = "reg"' argument is used
# in the function sns.pairplot().
# Reference: answer to a question I asked on stackoverflow:
# https://stackoverflow.com/questions/76217544/how-to-fit-regression-lines-on-each-non-diagonal-segment-of-a-pairplot-while-re
# Also, reference for information on arguments: https://www.youtube.com/watch?v=-eyiVTLJuqI  (around 11 mins in).

sns.set_theme(style = "white")

# The 'corner' argument removes the top right corner of each pairplot. 
iris_pairplot = sns.pairplot(df, hue = "variety", palette="Dark2", height=3, aspect=1, corner=True)

def regline(x, y, **kwargs):
    sns.regplot(data=kwargs['data'], x=x.name, y=y.name, scatter=False, color=kwargs['color'])

iris_pairplot.map_offdiag(regline, color='red', data=df)

# fig.suptitle() adds a title, including increasing the fontsize.
iris_pairplot.fig.suptitle("Pairplot of traits for full Iris sample", fontsize = "xx-large")
plt.tight_layout()
plt.savefig('iris_pairplot.png')


# The df.loc[] property allows us to create three 'sub-DataFrames' from the overall DataFrame, based on the condition 
# that the entry in the 'variety' column equals one of the three varieties of Iris.
# Reference: https://sparkbyexamples.com/pandas/pandas-dataframe-loc/

setosa = df.loc[df['variety']=="Iris-setosa"]
versicolor = df.loc[df['variety']=="Iris-versicolor"]
virginica = df.loc[df['variety']=="Iris-virginica"]


# For each of the individual Iris pairplots, the argument kind = "reg" allows us to impose regression lines straight on to the plots.
setosa_pairplot = sns.pairplot(setosa, diag_kws = dict(color='grey'), plot_kws = dict(color = 'brown'), height=3, aspect=1, corner=True, kind = "reg")
setosa_pairplot.fig.suptitle("Pairplot of setosa traits", fontsize = "xx-large")
plt.savefig('setosa_pairplot.png')

versicolor_pairplot = sns.pairplot(versicolor, diag_kws=dict(color='grey'), plot_kws=dict(color = 'orange'),  height=3, aspect=1, corner=True, kind = "reg")
versicolor_pairplot.fig.suptitle("Pairplot of versicolor traits", fontsize = "xx-large")
plt.savefig('versicolor_pairplot.png')

virginica_pairplot = sns.pairplot(virginica, diag_kws=dict(color='grey'), plot_kws=dict(color = 'green'), height=3, aspect=1, corner=True, kind ="reg")
virginica_pairplot.fig.suptitle("Pairplot of virginica traits", fontsize = "xx-large")
plt.savefig('virginica_pairplot.png')


# calling the function for printing out the text file
summary_statistics()
