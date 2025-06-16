import pandas as pd

# Step 1: Load the actual ball-by-ball match file
data = pd.read_csv("match.csv", error_bad_lines=False)
  # ✅ update path as per your machine

# Step 2: Clean and group by over
df['over_number'] = df['ball'].astype(str).str.split('.').str[0].astype(int)

summary = df.groupby('over_number').agg({
    'runs_off_bat': 'sum',
    'wicket_type': lambda x: x.notnull().sum()
}).reset_index()

# Step 3: Rename columns
summary.columns = ['over', 'runs', 'wicket']

# Step 4: Save cleaned file
summary.to_csv("match_cleaned.csv", index=False)
print("✅ match_cleaned.csv created!")
