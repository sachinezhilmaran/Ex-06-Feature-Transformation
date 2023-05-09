import pandas as pd
import numpy as np
#Read the data from CSV file
data = pd.read_csv("Data_to_Transform.csv")
#Perform logarithm transformation on "Moderate Positive Skew" column
data['Moderate Positive Skew Log'] = np.log(data['Moderate Positive Skew'])
#Perform logarithm transformation on "Highly Positive Skew" column
data['Highly Positive Skew Log'] = np.log(data['Highly Positive Skew'])
#Perform logarithm transformation on "Moderate Negative Skew" column
data['Moderate Negative Skew Log'] = np.log(data['Moderate Negative Skew'])
#Perform logarithm transformation on "Highly Negative Skew" column
data['Highly Negative Skew Log'] = np.log(data['Highly Negative Skew'])
#Save the transformed data to a new CSV file
data.to_csv("Data_Transformed.csv", index=False)
#Print the transformed data
print(data)
