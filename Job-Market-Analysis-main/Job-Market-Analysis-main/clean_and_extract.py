import pandas as pd
import re

# Load the raw data we collected
df = pd.read_csv("raw_job_data.csv")

print(f"Starting rows: {len(df)}")

# --- CLEANING ---

# Remove duplicate postings (same title + company + location)
df = df.drop_duplicates(subset=["title", "company", "location"])
print(f"After removing duplicates: {len(df)}")

# Drop rows where description is missing (can't extract skills without it)
df = df.dropna(subset=["description"])
print(f"After dropping missing descriptions: {len(df)}")

# Clean city names from search_city into a proper "city" column (title case)
df["city"] = df["search_city"].str.title()

# --- SKILL EXTRACTION ---

# List of common skills to search for in each job description
SKILLS = [
    "SQL", "Python", "Excel", "Power BI", "Tableau", "R programming",
    "Machine Learning", "Deep Learning", "Statistics", "Pandas", "NumPy",
    "AWS", "Azure", "GCP", "Big Data", "Hadoop", "Spark",
    "Data Visualization", "Data Warehousing", "NLP", "Communication",
    "PowerPoint", "VBA", "SAS", "SPSS", "Looker", "Google Analytics",
    "A/B Testing", "Data Cleaning", "Predictive Modeling", "Regression",
    "Time Series", "Java", "Scala", "MongoDB", "NoSQL", "MySQL",
    "PostgreSQL", "Data Mining", "Business Intelligence"
]

def extract_skills(description, skills_list):
    """Check which skills from our list appear in the job description."""
    found = []
    text = str(description).lower()
    for skill in skills_list:
        # simple substring match, case-insensitive
        if skill.lower() in text:
            found.append(skill)
    return found

# Apply skill extraction to every row
df["skills_found"] = df["description"].apply(lambda x: extract_skills(x, SKILLS))
df["num_skills"] = df["skills_found"].apply(len)

# Create one column per skill (1 if mentioned, 0 if not) — makes analysis much easier later
for skill in SKILLS:
    col_name = skill.replace(" ", "_")
    df[col_name] = df["skills_found"].apply(lambda x: 1 if skill in x else 0)

# --- SAVE CLEANED DATA ---
df.to_csv("cleaned_job_data.csv", index=False)
print(f"Saved cleaned_job_data.csv with {len(df)} rows and {len(df.columns)} columns")
print("\nTop 10 most common skills:")
skill_cols = [s.replace(" ", "_") for s in SKILLS]
print(df[skill_cols].sum().sort_values(ascending=False).head(10))