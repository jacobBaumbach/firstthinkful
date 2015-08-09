#This program imports data from a link, cleans the data and then generates a boxplot, histogram and QQ-Plot for a specific column of the data
#each plot is saved and printed to the screen

#Observations:  From the boxplot and histogram it is apparent that the data is skewed right (mean<median).
#Observations (cont'd): From the QQ-Plot there is a high R**2 between the data and the theoretical normal but the fact that the data at the smallest and largest quantiles does not fit well indicates to me a normal distribution is not an optimal fit and a distribution with "fatter tails" would probably better suit the data

import matplotlib.pyplot as plt #import plotting package
import pandas as pd #import pandas package as pd
import scipy.stats as stats#import stats portion of scipy as stats

loansData=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')#read in csv data from given link and enters data into loansData

loansData.dropna(inplace=True)#removes rows with null values

#boxplot
plt.figure()#generate new figure
loansData.boxplot(column='Amount.Requested')#generate boxplot for data in "Amount Requested" col
plt.savefig('Amount_Funded_By_Investors_BOXPLOT.png')#saves boxplot
plt.show()#prints boxplot

#histogram
plt.figure()#generate new figure
loansData.hist(column='Amount.Requested')#generate histogram for data in "Amount Requested" col
plt.savefig('Amount_Funded_By_Investors_HISTOGRAM.png')#save histogram
plt.show()#prints histogram 

#QQ Plot
plt.figure()#generate new figure
graph=stats.probplot(loansData['Amount.Requested'], dist="norm",plot=plt)#generate QQ-Plot for data in "Amount Requested" col against normal dist
plt.savefig('Amount_Funded_By_Investors_QQPLOT.png')#save QQ-Plot
plt.show()#prints QQ-Plot