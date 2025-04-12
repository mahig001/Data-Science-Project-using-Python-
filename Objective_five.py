import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\tiyam\\OneDrive\\Desktop\\Python_project\\Dataset.csv")
df


print("Dataset Overview: ")
print(df)

# 5.Analyze the gender distribution of teachers across different educational levels (Pre-Primary, Primary, Upper Primary, Secondary, and Higher Secondary) to identify trends and disparities in teacher representation.
qualification_counts = pd.DataFrame({
    'Female': [
        df['Female (Pre-Primary Total(A+B))'].sum(),
        df['Female (Primary Total(I-V)(B+C+D))'].sum(),
        df['Female (Upper Primary Total(VI-VIII)(D+E+F))'].sum(),
        df['Female (Secondary Total(IX-X)(F+G+H))'].sum(),
        df['Female (Higher Secondary Total(XI-XII)(H+I))'].sum()
    ],
    'Male': [
        df['Male (Pre-Primary Total(A+B))'].sum(),
        df['Male (Primary Total(I-V)(B+C+D))'].sum(),
        df['Male (Upper Primary Total(VI-VIII)(D+E+F))'].sum(),
        df['Male (Secondary Total(IX-X)(F+G+H))'].sum(),
        df['Male (Higher Secondary Total(XI-XII)(H+I))'].sum()
    ]
}, index=['Pre-Primary', 'Primary', 'Upper Primary', 'Secondary', 'Higher Secondary'])
qualification_counts.plot(kind="bar", figsize=(14, 7), colormap="tab20")
plt.title('Gender Distribution of Teachers Across Educational Levels')
plt.xlabel('Educational Level')
plt.ylabel('Total Number of Teachers')
plt.xticks(rotation=0)  
plt.grid(axis='y')  
plt.tight_layout()
plt.show()
