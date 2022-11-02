import pandas as pd
import numpy as np

#Task 1
heights_A=pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'])
print(heights_A[1])#print second element in Series using indexing
# print(heights_A['s2'])#print second element in series using index value

#Task 2
# print(heights_A[1:5])#Printing middle trhee elements of Series using slicing
print(heights_A['s2':'s4'])#Printing middle three elements using index values

#Task 3
weights_A=pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])

data={
  'Student_height':heights_A,
  'Student_weight':weights_A
}
df_A=pd.concat(data,axis=1)
height=df_A['Student_height']
print(type(height))

#Task 4

df_s1s2=df_A.loc[['s1','s2','s5']]#Uisng loc
df_s1s2=df_A.iloc[[0,1,4]]#Using iloc
print(df_s1s2)

#Task 5
df_s1s4=df_A.loc[df_A.index.str.endswith('1')| df_A.index.str.endswith('4')]
print(df_s1s4)

