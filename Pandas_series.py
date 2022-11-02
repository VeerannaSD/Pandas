import pandas as pd
import numpy as np

#Task1
'''
Create Series with below data list of heights [176.2,158.4,167.6,156.2,161.4] of 5 students s1,s2,s3,s4 and s5
Print shape of Series created
'''
heights_A=pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'])
#print(heights_A)
print(heights_A.shape)

#Task2
'''
Create Series with below data list of weights [85.1,90.2,76.8,80.4,78.9] of 5 students s1,s2,s3,s4 and s5
Print data types of Series created
'''
weights_A=pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
# print(weights_A)
print(weights_A.dtype)

#Task3
'''
Combine 2 series heights_A and weights_A to form DataFrame
'''
heights=pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'],name='Student_heights')
weights=pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'],name='Students_weight')
heights=pd.DataFrame(heights)
#Using join method, to join two series,one series should be converted to DataFrame and then join series
df_A=heights.join(weights)
print(df_A)

#Task4
'''
Create Series named heights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 170.0 and standard deviation 25.0.
Note: Set random seed to 100 before creating heights_B series. Use numpy.
Create Series named weights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 75.0 and standard deviation 12.0.
Note: Set random seed to 100 again before creating weights_B series. Use numpy.
Label both Series elements with s1, s2, s3, s4 and s5.
Create a dataframe df_B containing the height and weight of students s1, s2, s3, s4 and s5
'''
np.random.seed(100)
x=np.random.normal(loc=170.0,scale=25.0,size=5)
np.random.seed(100)
heights_B=pd.Series(x,index=['s1','s2','s3','s4','s5'])
#print(heights_B)

np.random.seed(100)
y=np.random.normal(loc=75.0,scale=12.0,size=5)
np.random.seed(100)
weights_B=pd.Series(x,index=['s1','s2','s3','s4','s5'])
# print(weights_B)

#Task5
df_B=pd.DataFrame({'Student_height':heights_B,'Students_weight':weights_B},index=weights_B.index)
print(df_B)




