import pandas as pd
df = pd.read_csv(r"C:\Users\HP\Practice GitHub\new_repo\ds_salaries_clean.csv")

print(df.isna().sum())