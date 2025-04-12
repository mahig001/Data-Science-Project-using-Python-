import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

qualification_df = df[[ "School Category", "Academic Qualification"]]
qualification_df_clean = qualification_df.dropna()
academic_counts = qualification_df_clean.groupby("School Category")["Academic Qualification"].value_counts().unstack().fillna(0)
selected_qualifications = ['Below Secondary', 'Higher secondary', 'Graduate', 'Post graduate', 'M.Phil', 'Ph.D']
academic_counts_filtered = academic_counts[selected_qualifications]
plt.figure(figsize=(10, 6))
sns.heatmap(academic_counts_filtered, annot=True, fmt='g', cmap='YlGnBu', linewidths=.5)
plt.title("Heatmap of Teacher Academic Qualifications by School Category", fontsize=14)
plt.xlabel("Academic Qualification", fontsize=12)
plt.ylabel("School Category", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
