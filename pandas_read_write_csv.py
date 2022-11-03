import pandas as pd

#Task 1
heights_A=pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'],name='Student_height')
weihts_A=pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'],name='Student_weight')
heights=pd.DataFrame(heights_A)
df_A=heights.join(weihts_A)

#Writing df_A int csv file
df_A.to_csv('classA.csv')

#Task 2
df_A2=pd.read_csv('classA.csv')
print(df_A2)

#Task 3
df_A3=pd.read_csv('classA.csv',index_col=0)
print(df_A3)

#Task 4
import numpy as np
np.random.seed(100)
x=np.random.normal(loc=170,scale=25.0,size=5)
heights_B=pd.Series(x,index=['s1','s2','s3','s4','s5'],name='Student_height')

np.random.seed(100)
y=np.random.normal(loc=75.0,scale=12.0,size=5)
weights_B=pd.Series(y,index=['s1','s2','s3','s4','s5'],name='Student_weight')
heightsB=pd.DataFrame(heights_B)
df_B=heightsB.join(weights_B)
df_B.to_csv('classB.csv',index=False)#Writing into csv file without index data

#Task 5
df_B2=pd.read_csv('classB.csv')
print(df_B2)

#Task 6
df_B3=pd.read_csv('classB.csv',header=None)
print(df_B3)#when header is set to None, indexes of dataframe will be default to ints starting with 0 index

#Task 7
df_B4=pd.read_csv('classB.csv',header=None,skiprows=2)
print(df_B4)import pandas as pd

#Task 1
heights_A=pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'],name='Student_height')
weihts_A=pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'],name='Student_weight')
heights=pd.DataFrame(heights_A)
df_A=heights.join(weihts_A)

#Writing df_A int csv file
df_A.to_csv('classA.csv')

#Task 2
df_A2=pd.read_csv('classA.csv')
print(df_A2)

#Task 3
df_A3=pd.read_csv('classA.csv',index_col=0)
print(df_A3)

#Task 4
import numpy as np
np.random.seed(100)
x=np.random.normal(loc=170,scale=25.0,size=5)
heights_B=pd.Series(x,index=['s1','s2','s3','s4','s5'],name='Student_height')

np.random.seed(100)
y=np.random.normal(loc=75.0,scale=12.0,size=5)
weights_B=pd.Series(y,index=['s1','s2','s3','s4','s5'],name='Student_weight')
heightsB=pd.DataFrame(heights_B)
df_B=heightsB.join(weights_B)
df_B.to_csv('classB.csv',index=False)#Writing into csv file without index data

#Task 5
df_B2=pd.read_csv('classB.csv')
print(df_B2)

#Task 6
df_B3=pd.read_csv('classB.csv',header=None)
print(df_B3)#when header is set to None, indexes of dataframe will be default to ints starting with 0 index

#Task 7
df_B4=pd.read_csv('classB.csv',header=None,skiprows=2)
print(df_B4)