# Import Library
import pandas as pd
import numpy as np

import statsmodels.api as sm
import statsmodels.formula.api as smf

import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.outliers_influence import variance_inflation_factor

import os

# Assign Output Folder
# Output Directory
output_dir = r"D:\Research game addiction\output"
os.makedirs(output_dir, exist_ok=True)

# Load Data
print("load data...")
df = pd.read_csv(r"D:\Research game addiction\data\game addiction.csv")
print("data loaded.")

# ดูหน้าตาข้อมูล
print("\nPreview data")
print(df.head())

print("\nColumn name")
print(df.columns)

# Clean Column Name
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace("/","_")
              .str.replace("-","_")
)
#rename columns
df.columns = df.columns.str.replace("_+", "_", regex=True)
print(df.columns.tolist())

# Missing Value Check
print("\nMissing Value")
print(df[
    ["game_addiction_total", "hours_spend", "gpa", "gender", "years", "cp1", "cp2", "cp3", "cp4", "cp5", "cp6", "cp7", "cp8", "cp9"]
].isnull().sum())


# Model 1 : Determinant of Game Addiction
model_addiction_robust = smf.ols(
    "game_addiction_total ~ hours_spend + C(gender) + C(years) + competitive_action + role_progression + causal_chance + cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7 + cp8 + cp9",
    data=df
).fit(cov_type="HC3")
print(model_addiction_robust.summary())

#export
results = model_addiction_robust
table = pd.DataFrame({
    "Coef": results.params,
    "Robust SE (HC3)": results.bse,
    "z": results.tvalues,
    "p-value": results.pvalues
})
table.to_excel("regression_result_addiction.xlsx")

# drop  ใช้เฉพาะแถวนี้ใช่
df_gpa = df[["gpa", "game_addiction_total", "cp1", "cp2", "cp3", "cp4", "cp5", "cp6", "cp7", "cp8", "cp9"]].dropna()

model_gpa = smf.ols(
    "gpa ~ game_addiction_total + cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7 + cp8 + cp9",
    data=df_gpa
).fit()
print(model_gpa.summary())

# Model 2 : Addiction > GPA
model_gpa_robust = smf.ols(
    "gpa ~ game_addiction_total + hours_spend + C(years) + cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7 + cp8 + cp9",
    data=df
).fit(cov_type="HC3")
print(model_gpa_robust.summary())

#export 
results = model_gpa_robust
table = pd.DataFrame({
    "Coef": results.params,
    "Robust SE (HC3)": results.bse,
    "z": results.tvalues,
    "p-value": results.pvalues
})
table.to_excel("regression_result_gpa.xlsx")

# Anova: Gender
anova_gender = smf.ols(
    "game_addiction_total ~ C(gender)",
    data=df
).fit()
anova_table = sm.stats.anova_lm(anova_gender,type=2)
print(anova_table)

#export Anova to csv
anova_table
anova_table.to_csv(f"{output_dir}/anova_gender_addiction.csv")

# ตรวจ missing
df["gender"].isna().sum()
df_tukey = df[["gender", "game_addiction_total"]].dropna()
df_tukey["gender"] = df_tukey["gender"].astype("category")

# Tukey Post-Hoc
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(
    endog=df_tukey["game_addiction_total"],
    groups=df_tukey["gender"],
    alpha=0.05
)
print(tukey)

# Export Post-Hoc
tukey_df = pd.DataFrame(
    data=tukey.summary().data[1:],
    columns=tukey.summary().data[0:]
)
tukey_df.to_csv(f"{output_dir}/tukey_gender_addiction.csv", index=False)

# Bar Plot Addiction by Gender
gender_mean = (
    df.groupby("gender", as_index=False)["game_addiction_total"]
    .mean()
    .sort_values("game_addiction_total")
)
plt.figure(figsize=(6,4))
ax= sns.barplot(
    data=gender_mean,
    x="gender",
    y= "game_addiction_total"
)

for p in ax.patches:
    ax.annotate(
        f"{p.get_height():.2f}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom"
    )

plt.title("Mean Game Addiction Score by Gender")
plt.tight_layout()
plt.savefig(f"{output_dir}/Gender Addiction.png",dpi=300)
plt.show()

#Phase 8 Diagnotics Test
plt.figure()    
sns.residplot(
    x=model_addiction_robust.fittedvalues,
    y=model_addiction_robust.resid,
    lowess=True,
)
plt.title("Residuals vs Fitted")
plt.show()

# QQ plot
sm.qqplot(model_addiction_robust.resid, line="45")
plt.title("Normal Q-Q Plot")
plt.show()

#VIF (Multicolinearlity)
X=model_addiction_robust.model.exog
vif_df = pd.DataFrame()
vif_df["Variable"] = model_addiction_robust.model.exog_names
vif_df["VIF"] = [
    variance_inflation_factor(X, i)
    for i in range(X.shape[1])
]
print(vif_df)
