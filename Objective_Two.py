import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\tiyam\\OneDrive\\Desktop\\Python_project\\Dataset.csv")
df


print("Dataset Overview: ")
print(df)

df_management = df['School Management'].value_counts().reset_index()
df_management.columns = ['Management Type', 'Count']
df_management
plt.figure(figsize=(8,6))
plt.pie(df_management['Count'], labels=df_management['Management Type'], autopct='%1.1f%%', colors=['skyblue', 'peachpuff'])
plt.title('Distribution of Schools by Management Type')
plt.show()
