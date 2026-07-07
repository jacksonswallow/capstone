
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_data.csv')

fig, ax = plt.subplots(figsize=(8,4))
counts = df['diabetes_012'].value_counts().sort_index()
labels = ['No Diabetes', 'Prediabetes', 'Diabetes']
ax.bar(labels, counts.values)
for i, v in enumerate(counts.values):
  pct = 100 * v/counts.sum()
  ax.text(i, v, f"{v:,}\n({pct:.1f}%)", ha="center", va="bottom")
ax.set_ylabel('Respondents')
ax.set_title("Distribution of Diabetes Status")
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(15,4))
label_map = {0: 'No Diabetes', 1: 'Prediabetes', 2: 'Diabetes'}

binary_cols = ["highbp", "highchol", "cholcheck", "smoker", "stroke",
    "heart_disease", "physactivity", "fruits", "veggies", "hvy_alc",
    "anyhealthcare", "nodocbccost", "diffwalk", "sex"]

non_binary_cols = ["bmi", "menthlth", "physhlth","genhlth", "age", "education", "income"]

target = ['diabetes_012']

for ax, col in zip(axes, non_binary_cols):
  for target_val, label in label_map.items():
    subset = df.loc[df['diabetes_012']==target_val, col]
    ax.hist(subset, bins=40, alpha=0.6, label=label, density = True)
  ax.set_title(f"{col} by Diabetes Status")
  ax.set_xlabel(col)
  ax.set_ylabel('Density')
  ax.legend()
plt.tight_layout()
plt.show()

binary_presence = df.groupby(target)[binary_cols].mean().T.rename(columns=label_map)

fig, ax = plt.subplots(figsize=(12,6))
binary_presence.plot(kind='barh', ax=ax, width = 0.8)
ax.set_xlabel('Proportion')
ax.set_ylabel('Binary Feature')
ax.legend(title='')
plt.tight_layout()
plt.show()

from numpy.random.mtrand import f
fig, axes = plt.subplots(1,4, figsize=(14,8))

demo_cols = ['age', 'income', 'education', 'genhlth']

for ax, col in zip(axes, demo_cols):
  rate = df.groupby(col)[target].apply(lambda s: (s ==2).mean())
  rate.plot(kind ='bar', ax=ax, color = '#c44e52')
  ax.set_title(f"Diabetes Rate by {col}")
  ax.set_ylabel('Diabetes Rate')
  ax.set_xlabel(col)
  ax.tick_params(axis='x', rotation=0)
plt.tight_layout()
plt.show()

heat_map = df.corr(numeric_only = True)

fig, ax = plt.subplots(figsize=(12,10))
sns.heatmap(
    heat_map, cmap = 'RdBu_r', center = 0, vmin = -1, vmax = 1, annot = True, fmt = '.2f', annot_kws={'size': 7}, square = True, cbar_kws={"shrink": 0.7}, ax=ax

)
ax.set_title("Heatmap")
plt.tight_layout()
plt.show()

