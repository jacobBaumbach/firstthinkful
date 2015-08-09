#This program takes data and prints its frequencies, plots a boxplot based on the data, plots a histogram based on the data and then finally plots a QQ plot based on the data
#each plot is saved and displayed

import scipy.stats as stats#import the stats package
import matplotlib.pyplot as plt#import plotting package
import collections#import collections package

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]#data

#display frequencies
c=collections.Counter(x)#creates an object where each unique value of x corresponds to its number of occurrences in the list x
count_sum=sum(c.values())#sums occurrences which is equal to the number of values in x

for k,v in c.iteritems():#loop that prints the unique value of x,k, and the number of times it occurs in x,v
	print "The frequency of number "+str(k)+" is "+str(v)+"\n"

#plot boxplot
plt.figure()#create new figure
plt.boxplot(x)#generate the boxplot with data from x
plt.savefig("boxplot.png")#save the boxplot
plt.show()#print the boxplot to the screen

#plot histogram
plt.figure()#create new figure
plt.hist(x, histtype='bar')#generate the histogram with data from x
plt.savefig("histogram.png")#save the histogram
plt.show()#print the histogram

#plot QQ-plot
plt.figure()#create new figure
graph4=stats.probplot(x, dist="norm", plot=plt)#generate the QQ-plot with x data against the normal distribution
plt.savefig("QQ_normal.png")#save the QQ-plot
plt.show()#print the QQ-plot

