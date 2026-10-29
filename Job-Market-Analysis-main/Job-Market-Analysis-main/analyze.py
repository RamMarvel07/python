import pandas as pd

df = pd.read_csv("cleaned_job_data.csv")

skill_cols = [c for c in df.columns if c not in 
    ["title","company","location","salary_min","salary_max","description",
     "created","search_term","search_city","city","skills_found","num_skills"]]

# --- 1. Overall top skills (%) ---
print("=== TOP SKILLS OVERALL (% of postings) ===")
skill_pct = (df[skill_cols].sum() / len(df) * 100).sort_values(ascending=False)
print(skill_pct.head(15).round(1))

# --- 2. Data Analyst vs Data Scientist skill comparison ---
print("\n=== DATA ANALYST vs DATA SCIENTIST (top skills) ===")
da = df[df["search_term"] == "data analyst"]
ds = df[df["search_term"] == "data scientist"]

da_pct = (da[skill_cols].sum() / len(da) * 100).sort_values(ascending=False).head(10)
ds_pct = (ds[skill_cols].sum() / len(ds) * 100).sort_values(ascending=False).head(10)

print("\nTop skills for Data Analyst roles:")
print(da_pct.round(1))
print("\nTop skills for Data Scientist roles:")
print(ds_pct.round(1))

# --- 3. City-wise posting counts ---
print("\n=== POSTINGS BY CITY ===")
print(df["city"].value_counts())

# --- 4. Salary disclosure rate ---
disclosed = df["salary_min"].notna().sum()
print(f"\n=== SALARY DISCLOSURE ===")
print(f"{disclosed} out of {len(df)} postings disclosed salary ({disclosed/len(df)*100:.1f}%)")

# --- 5. Average number of skills required per posting ---
print(f"\n=== AVG SKILLS PER POSTING ===")
print(f"Average: {df['num_skills'].mean():.1f} skills mentioned per posting")

# --- 6. SQL + Python combo — how many postings ask for both ---
both = df[(df["SQL"] == 1) & (df["Python"] == 1)]
print(f"\n=== SQL + PYTHON COMBO ===")
print(f"{len(both)} postings ({len(both)/len(df)*100:.1f}%) require BOTH SQL and Python")