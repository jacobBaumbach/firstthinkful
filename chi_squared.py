#This program imports data from a link, cleans the data, and then performs a chi squared test on the columns of data that contain discrete, bounded data
from scipy import stats#imports stats portion of the scipy project
import collections#imports collections package
import pandas as pd #imports pandas package as pd

ld=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')#read in csv data from given link and enters data into ld

ld.dropna(inplace=True)#removes rows with null values

discrete_data=["Loan.Purpose","State","FICO.Range","Open.CREDIT.Lines","Inquiries.in.the.Last.6.Months","Employment.Length"]#list containing column names of discrete, bounded data

for i in discrete_data:#loops through each element of discrete_data list, so each col of discerete, bounded data will have a chi square test performed on it
	freq=collections.Counter(ld[i])#creates an object where each unique value of the column of ld corresponds to its number of occurrences in the column of ld
	chi, p = stats.chisquare(freq.values())#performs Chi square test on col of ld and saves the chi square value in chi and the corresponding p value in p
	print "The Chi squared value for "+i+" is "+str(chi)+" which has an accompanying p value of "+str(p)+"\n"#prints the result of chi square test for the col