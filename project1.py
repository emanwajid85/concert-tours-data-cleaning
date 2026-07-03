import pandas as pd

# Step 1: Load the file
df = pd.read_csv("dataset.csv")

# Step 2: Fix column names — replace hidden special spaces, then strip
df.columns = df.columns.str.replace("\xa0", " ", regex=False).str.strip()

# Step 3: Confirm the fix worked
print(df.columns.tolist())
df = df.drop(columns=["Peak", "All Time Peak", "Ref."])
print(df.columns.tolist())
money_columns = ["Actual gross", "Adjusted gross (in 2022 dollars)", "Average gross"]

for col in money_columns:
    df[col] = df[col].str.replace("$", "", regex=False)
    df[col] = df[col].str.replace(",", "", regex=False)
    df[col] = df[col].str.replace(r"\[.*?\]", "", regex=True)   # NEW: removes anything like [1], [b], [23]
    df[col] = df[col].astype(float)

print(df.head())
print(df.info())
print(df.duplicated().sum())
df = df.sort_values("Actual gross", ascending=False)
df.to_csv("cleaned_project1.csv", index=False)
print("Cleaning complete! Saved as cleaned_project1.csv")