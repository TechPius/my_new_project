#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing csv files


# In[4]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[8]:


filename = 'C:/Users/Pius/Desktop/data/car_financing.csv'
df = pd.read_csv(filename)
df


# In[12]:


filename = 'C:/Users/Pius/Desktop/data/car_financing.xlsx'
df = pd.read_excel(filename)
df


# In[17]:


#Select top N number of the records (default = 5)
df.head()


# In[18]:


df.tail()


# In[19]:


#check column datatypes 
df.dtypes


# In[20]:


#use the shape attribute to get number of rows and columns in your dataframe
df.shape


# In[21]:


# the info method gives the column datatypes, number of non null valus
# notice that seem to have 408 non-values for all but the interest paid values
df.info


# In[22]:


df.head()


# In[23]:


#select one column of a dataset
df[['car_type']].head()


# In[28]:


#select multiple column using double brackes
df[['car_type', 'Principal Paid']].head()


# In[29]:


#This is a pandas DataFrame
type(df[['car_type']].head())


# In[30]:


#select one column using 
#this produce a pandas series which is a one dimensional array which can be labled 
df['car_type'].head()


# In[31]:


#This is pandas series
type(df['car_type'].head())


# Pandas Slicing
#with pasndas series, we can select rows using slicing like this;
#series[start_index:end_index]
#The end index is not inclusive. this behavious is very similar to python list
# In[32]:


df['car_type']


# In[36]:


df['car_type'][0:10]


#  #select column using dot notation 
#  #however this is not recommended
# 

# In[37]:


df.car_type.head()


# In[ ]:


#it is safer to use single bracket 


# In[38]:


df['Principal Paid']


# In[39]:


#Selecting Column Using Loc
#Pandas dataframe
df.loc[:, ['car_type']].head()


# In[40]:


#Pandas series
df.loc[:, 'car_type'].head()


# In[41]:


#Lets first start by car_type column
df['car_type'].value_counts()


# In[48]:


#car_type filter
car_filter = df['car_type']=='Toyota Sienna'


# In[49]:


car_filter.head()


# In[51]:


#Approach 1, using square bracket
#Filter dataframe to get a Dataframe of only 'Toyota Sienna'
df[car_filter].head()


# In[54]:


#use the loc approach
#filter dataframe to get a fataframe of only 'Toyota Sienna'
df.loc[car_filter, :]


# In[ ]:





# In[ ]:


df = df.loc[car_filter, :]


# In[55]:


df['car_type'].value_counts()


# In[56]:


#interest rate filter
df['interest_rate'].value_counts()


# In[57]:


#Notice that the filter produces a panda series of True and False values
interest_filter = df['interest_rate']==0.0702


# In[58]:


df = df.loc[interest_filter, :]


# In[59]:


df['interest_rate'].value_counts(dropna = False)


# In[61]:


df.loc[car_filter & interest_filter, :]


# In[74]:


df = df.rename(columns={'Starting Balance': 'starting_balance',
                        'Interest Paid': 'interest_paid',
                        'Principal Paid': 'principal_paid',
                        'New Balance': 'new_balance'})


# In[75]:


df.head()


# In[76]:


#Approach 2 list replacement
#only changing Month to month so we will have to list the rest of the columns
df.columns = ['month',
             'starting_balance',
             'Repayment',
             'interest_paid',
             'principal_paid',
             'new_balance',
             'term',
             'interest_rate',
             'car_type']


# In[80]:


df.head()


# In[89]:


#deleting colums
#Approach 1
#The approach allows you to drop multiple columns at a time
df = df.drop(columns = ['term'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[81]:


df.head()


# In[92]:


#apparoach 2
#use the delete command
del df['Repayment']


# In[93]:


df.head()

   AGGREGATE FUNCTIONS
   SUM
# In[94]:


#sum the values in a column
#total amount of interest paid over the course of the loan
df['interest_paid'].sum()


# In[98]:


#sum all the values accross all colums
df.sum()


# In[99]:


#to use help
help(df['interest_paid'].sum)


# In[101]:


#the info method gives the column datatype + number of null values
 #we have 60 non-null values for all but the interest paid column
#Identifying missing values
# below table shows one missing value in interest paid
 df.info()


# In[113]:


df['interest_paid'].isna().head()


# In[114]:


interest_missing = df['interest_paid'].isna()


# In[104]:


#looks at the roe that contains the NaN for interest_paid
df.loc[interest_missing,:]


# In[115]:


#keep in mind that we can use the not operator (-) to negate the filter
#every row that doesnt have a nan is returned
df.loc[-interest_missing,:]


# In[116]:


#This code counts the number of missing values
#sum works because boolean are a subtype of integers
df['interest_paid'].isna().sum()


# In[117]:


True + False + False


# In[118]:


#REMOVE MISSING VALUES
#You can drop an entire row if they contain any missing values in them or all
#this may not be the best strategy for our dataset
df[30:40].dropna(how = 'any')


# In[120]:


#Export Dataframe to csv File
df.tocsv(path_or_buf='C:/Users/Pius/Desktop/data/table_i702t60.csv',
        index = False)


# In[ ]:




