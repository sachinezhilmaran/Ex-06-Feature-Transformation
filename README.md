# Ex-06-Feature-Transformation

# AIM:

To read the given data and perform Feature Transformation process and save the data to a file.

# Explanation:

Feature transformation is a mathematical transformation in which we apply a mathematical formula to a particular column (feature) and transform the values, which are useful for our further analysis. It is a technique by which we can boost our model performance.

# ALGORITHM:

### STEP 1

Read the given Data

### STEP 2

Clean the Data Set using Data Cleaning Process

### STEP 3

Apply Feature Transformation techniques to all the feature of the data set

### STEP 4

Save the data to the file

# PROGRAM:

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

# OUTPUT:
![image](https://user-images.githubusercontent.com/91734840/232521829-0009b49a-f035-492a-9f68-da431fefa916.png)

# RESULT:

Thus, to read the given data and perform Feature Generation process and save the data to a file has been successfully performed.
