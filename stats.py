#This program converts data into a dataframe object and then prints some descriptive statistics about the data

import pandas as pd #import pandas package as pd
import scipy.stats as stats#import the stats portion of scipy package as stats

data = '''Region,Alcohol,Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''#data to be used

data=data.splitlines()#split the string by new line

data=[i.split(',') for i in data]#create a list of lists where each list component is broken up where there is a comma

cols=data[0]#saves header

rows=data[1::]#eliminates header so import easier into the dataframe object

df=pd.DataFrame(rows, columns=cols)#creates data frame object where import the headerless data and use cols as the header

df['Alcohol'] = df['Alcohol'].astype(float)#convert data in Alcohol col into float
df['Tobacco']=df['Tobacco'].astype(float)#convert data in tobacco col into float

print "The mean for the Alcohol dataset is: "+str(df['Alcohol'].mean())#print mean for alcohol col
print "The median for the Alcohol dataset is: "+str(df['Alcohol'].median())#print median for alcohol col
print "The mode for the Alcohol dataset is: "+str(stats.mode(df['Alcohol'])[0][0])#print mode for alcohol col
print "The range for the Alcohol dataset is: "+str(max(df['Alcohol'])-min(df['Alcohol']))#print range for alcohol col
print "The variance for the Alcohol dataset is: "+str(df['Alcohol'].var())#print var for alcohol col
print "The standard deviation for the Alcohol dataset is: "+str(df['Alcohol'].std())#print standard deviation for alcohol col

print "The mean for the Tobacco dataset is: "+str(df['Tobacco'].mean())#print mean for Tobacco col
print "The median for the Tobacco dataset is: "+str(df['Tobacco'].median())#print median for Tobacco col
print "The mode for the Tobacco dataset is: "+str(stats.mode(df['Tobacco'])[0][0])#print mode for Tobacco col
print "The range for the Tobacco dataset is: "+str(max(df['Tobacco'])-min(df['Tobacco']))#print range for Tobacco col
print "The variance for the Tobacco dataset is: "+str(df['Tobacco'].var())#print var for Tobacco col
print "The standard deviation for the Tobacco dataset is: "+str(df['Tobacco'].std())#print standard deviation for Tobacco col



