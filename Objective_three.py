import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\tiyam\\OneDrive\\Desktop\\Python_project\\Dataset.csv")
df

#2.  To analyze how teacher qualifications vary across different regions or locations.
qualification_df = df[["Location", "Academic Qualification"]]
qualification_df_clean = qualification_df.dropna()
qualification_counts = qualification_df_clean.groupby("Location")["Academic Qualification"].value_counts().unstack().fillna(0)
top_n_locations = 10
top_locations = qualification_counts.sum(axis=1).sort_values(ascending=False).head(top_n_locations).index
qualification_counts_top = qualification_counts.loc[top_locations]
qualification_counts_top.plot(kind="bar", figsize=(14, 7), colormap="tab20")
plt.title("Teacher Academic Qualifications by Location (Top 10)", fontsize=14)
plt.xlabel("Location", fontsize=12)
plt.ylabel("Number of Teachers", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Academic Qualification", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
