import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\tiyam\\OneDrive\\Desktop\\Python_project\\Dataset.csv")
df


print("Dataset Overview: ")
print(df)

Analyze how teachers enrollment varies across different educational levels (e.g., pre-primary, primary, upper primary).
enrollment_levels = df[['Female (Pre-Primary Total(A+B))', 'Male (Pre-Primary Total(A+B))',
                        'Female (Primary Total(I-V)(B+C+D))', 'Male (Primary Total(I-V)(B+C+D))',
                        'Female (Upper Primary Total(VI-VIII)(D+E+F))', 'Male (Upper Primary Total(VI-VIII)(D+E+F))']].sum()

enrollment_levels.plot(kind='bar', figsize=(8,6), color=['#f1d2cd', '#e15e5e'])

plt.title('Student Enrollment Across Educational Levels')
plt.xlabel('Educational Level and Gender')
plt.ylabel('Total Enrollment')
plt.show()

