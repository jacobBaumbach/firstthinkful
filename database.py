"""This program takes data, creates a database using the data via SQLite, places the data into a DataFrame object(pandas), 
   takes user input on a month, and then outputs information from the DataFrame object about the chosen month 
"""
#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#Packages

import sqlite3 as lite #importing the sqlite3 package and naming it lite
import pandas as pd #importing the pandas package and naming it pd
import sys #importing sys package for user input

#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#Data

cities_data = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')) #created a tuple of tuples for city data

weather_data = (('New York City', 2013, 'July', 'January', 62),
  ('Boston', 2013, 'July', 'January', 59),
  ('Chicago', 2013, 'July', 'January', 59),
  ('Miami', 2013, 'August', 'January', 84),
  ('Dallas', 2013, 'July', 'January', 77),
  ('Seattle', 2013, 'July', 'January', 61),
  ('Portland', 2013, 'July', 'December', 63),
  ('San Francisco', 2013, 'September', 'December', 64),
  ('Los Angeles', 2013, 'September', 'December', 75))#created a tuple of tuples for weather data

#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#Database

con=lite.connect('getting_started.db')#connect to database

with con:
	cur=con.cursor()#create cursor object
	cur.execute("DROP TABLE IF EXISTS cities;")#remove cities table before execution
	cur.execute("DROP TABLE IF EXISTS weather;")#remove weather table before execution

	cur.execute("CREATE TABLE cities (name text, state text);")# create cities table with 2 text col named: name and state
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities_data)#insert data from cities_data tuple into cities table

	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);")# create weather table with five col (3 text, 2 integer) named: city, year, warm_month, cold_month, average_high
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather_data)#insert data from weather_data tuple into weather table

	cur.execute("SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city;")#performing an inner join between cities and weather table based on name = city

	rows=cur.fetchall()#fetches the data from inner join and inserts into row variable
	cols=[desc[0] for desc in cur.description]#cols is a list that holds the header names for each col
	df=pd.DataFrame(rows, columns=cols)#df is of type DataFrame containing data from rows(data from the inner join) and header names from rows

#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#User input

mlist=['January','February', 'March','April','May','June','July','August','September','October','November','December']#list of months


while True:#loops until you have a valid response to the warm month you want to investigate
	try:
		month=raw_input('\nChoose a month which you would like to know all the cities for which that month is considered a warm month(please write out the full month):')
		#user inputs warm month
		month=str(month)#converts user input to string
		month=month.lower().title()#converts user input so first character is capatilized and the remaining characters are lower case
		m=mlist.index(month)#checks to see if user input is a month, if not there will be a valueerror
		ff=df['warm_month'].value_counts()#counts the number of elements for each group in warm month
		fsize=ff[month]#obtains the number of observations for the user input, if the user input is not a month contained in warm_month there will be a keyerror
		break
	except ValueError:#accessed if user entered something that is not a month
		print "\nSorry, but this is not a month"
	except KeyError:#accessed if user enters a month that is not a member of warm_month
		print "\nSorry, but these cities are in the northern hemisphere, so your choice is not considered a warm month"

#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#Output after valid user input

t=1#counter variable used to help track the instances of the user inputted month

gsize=len(df.index)#number of rows in df


for ii in range(0,gsize):#loop through each row of df
	if t==1 and fsize==1 and df.ix[ii,'warm_month']==month:#checks to see if the row is the first instance of the user inputted month and if there is only one occurrence of the month
		print "\nThe cities that is the warmest in "+month+" is: "+df.ix[ii,'name']+'.'
	elif t==1 and fsize==2 and df.ix[ii,'warm_month']==month:#checks to see if the row is the first instance of the user inputted month and if there are only two occurrences of the month
		print "\nThe cities that are warmest in "+month+" are: "+df.ix[ii,'name']+', and'
		t+=1#increase counter 
	elif t==1 and df.ix[ii,'warm_month']==month:#checks to see if the row is the first instance of the user inputted month 
		print "\nThe cities that are warmest in "+month+" are: "+df.ix[ii,'name']+','
		t+=1#increase counter 
	elif t==fsize and fsize==2 and df.ix[ii,'warm_month']==month:#checks to see if the row is the last instance of the user inputted month and if there are only two occurrences of the month
		print " "+df.ix[ii,'name']+'.'
	elif t==fsize and df.ix[ii,'warm_month']==month:#checks to see if the row is the last instance of the user inputted month
		print " and "+df.ix[ii,'name']+'.'
	elif df.ix[ii,'warm_month']==month:#checks to see if the row is an instance of the user inputted month
		print " "+df.ix[ii,'name']+','
		t+=1#increase counter 








