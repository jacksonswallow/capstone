
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes_data.csv')

df.head()

df.describe()

df.info()

df.columns = df.columns.str.lower()

df.columns

df = df.rename(columns={'heartdiseaseorattack': 'heart_disease', 'hvyalcoholconsump': 'hvy_alc'})

df.columns

df.isnull().sum()

df.duplicated().sum()
#not sure if these are actual duplicates or unique individuals with the same information
#lots of binary labels so could be plausible

df = df.astype('int8')

df

cleaned_df = df.copy()

cleaned_df.to_csv('cleaned_diabetes_data.csv', index=False)

#cleaned_df.describe()

cleaned_df['genhlth'].max()
#multiple types of scale, max just to refer to which scale

cleaned_df['education'].max()
#multiple types of scale, max just to refer to which scale

cleaned_df['income'].max()
#same as above, reference point for scale

cleaned_df['physhlth'].max()

cleaned_df['menthlth'].max()

