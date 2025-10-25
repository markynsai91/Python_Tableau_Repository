#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 20:47:21 2025

@author: markynsailamar
"""

#Users/markynsailamar/Dropbox/My Mac (Markynsai’s MacBook Pro)/Documents/UDEMY PROJECT/Data/transaction.csv
import pandas as pd

# file_name=pd.read_csv('file.csv') <-- format o f read_csv

data=pd.read_csv('transaction.csv', sep=';')

#summary of the data 
data.info()

#working with calculations


#adding a new column to a dataframe
data['CostPerTransaction']=data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transasction
data['SalesPerTransaction']=data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitperTransaction']= data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/ Cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding Marking


data['Markup'] =round(data['Markup'],2)

#Column for  date

data['date']=data['Day'].astype(str) + '-' + data['Month'].astype(str) + '-' + data['Year'].astype(str)


data.head(5) # first 5 rows

#using split to split the  clientkeywords field

#var=col.str.split('',expand=True)
split_col=data['ClientKeywords'].str.split(',' , expand=True )

#creating new columns for the split columns in Client Keyword

data['ClientAge']=split_col[0]
#using the replace function to remove the '[' character in ClinetAge & LengthOfContract
data['ClientAge']=data['ClientAge'].str.replace('[','')


data['ClientType']=split_col[1]
data['LengthOfContract']=split_col[2]
data['LengthOfContract']=data['LengthOfContract'].str.replace(']','')
#Changing item to lowercase
data['ItemDescription']=data['ItemDescription'].str.lower()

#how to merge files

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

#merge Files -: merge_df=pd.merge(df_old,df_new,on='key')

data=pd.merge(data, seasons,on = 'Month')

#Dropping Columns ClientKeywords ,Day, Month, Year

data=data.drop(['Month','Year', 'Day','ClientKeywords'],axis=1)


#Export into CSV

data.to_csv('ValueInc_Cleaned.csv',index=False)


