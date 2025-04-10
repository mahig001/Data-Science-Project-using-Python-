import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\tiyam\\OneDrive\\Desktop\\Python_project\\Dataset.csv")
df


print("Dataset Overview: ")
print(df)


print("Basic EDA prints: ")
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.isnull().sum())


#A. To understand the distribution of teacher qualifications across different academic levels (e.g., graduate, postgraduate).
df_qualifications = df.groupby('Academic Qualification')['Professional Qualification'].value_counts().reset_index(name='Count')
plt.figure(figsize=(10,6))
plt.bar(df_qualifications['Academic Qualification'], df_qualifications['Count'])
plt.title('Teacher Qualifications by Academic Level')
plt.xlabel('Academic Qualification')
plt.ylabel('Count')
plt.show()

#B. To understand how schools are distributed across different management types (e.g., government, private)
df_management = df['School Management'].value_counts().reset_index()
df_management.columns = ['Management Type', 'Count']
df_management
plt.figure(figsize=(8,6))
plt.pie(df_management['Count'], labels=df_management['Management Type'], autopct='%1.1f%%', colors=['skyblue', 'peachpuff'])
plt.title('Distribution of Schools by Management Type')
plt.show()

#C. To analyze how teacher qualifications vary across different regions or locations.
df_region_qualifications = df.groupby(['Location', 'Professional Qualification']).size().reset_index(name='Count')

plt.figure(figsize=(10,6))
sns.barplot(data=df_region_qualifications, x='Location', y='Count', hue='Professional Qualification')
plt.title('Teacher Qualifications Across Different Regions')
plt.xlabel('Location')
plt.ylabel('Count')
plt.show()

#4. Analyze how teachers enrollment varies across different educational levels (e.g., pre-primary, primary, upper primary).
enrollment_levels = df[['Female (Pre-Primary Total(A+B))', 'Male (Pre-Primary Total(A+B))',
                        'Female (Primary Total(I-V)(B+C+D))', 'Male (Primary Total(I-V)(B+C+D))',
                        'Female (Upper Primary Total(VI-VIII)(D+E+F))', 'Male (Upper Primary Total(VI-VIII)(D+E+F))']].sum()

enrollment_levels.plot(kind='bar', figsize=(10,6), color=['pink', 'blue'])

plt.title('Student Enrollment Across Educational Levels')
plt.xlabel('Educational Level and Gender')
plt.ylabel('Total Enrollment')
plt.show()


