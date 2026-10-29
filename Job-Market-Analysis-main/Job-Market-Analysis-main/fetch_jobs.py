import os
from dotenv import load_dotenv
import requests
import pandas as pd
import time
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

SEARCH_TERMS = ["data analyst", "data scientist"]
CITIES = ["bangalore", "hyderabad", "pune", "mumbai", "delhi"]

BASE_URL = "https://api.adzuna.com/v1/api/jobs/in/search/{page}"

def fetch_jobs(what, where, max_pages=2):
    all_jobs = []
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page=page)
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 50,
            "what": what,
            "where": where,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error {response.status_code} for {what} in {where}, page {page}")
            print(response.text)
            break

        data = response.json()
        results = data.get("results", [])

        if not results:
            print("No results found.")
            break

        for job in results:
            all_jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
                "description": job.get("description"),
                "created": job.get("created"),
                "search_term": what,
                "search_city": where
            })

        time.sleep(1)

    return all_jobs

all_data = []
for term in SEARCH_TERMS:
    for city in CITIES:
        print(f"Fetching: {term} in {city}...")
        jobs = fetch_jobs(term, city, max_pages=2)
        all_data.extend(jobs)

df = pd.DataFrame(all_data)
df.to_csv("raw_job_data.csv", index=False)
print(f"Done. Collected {len(df)} job postings.")
print(df.head())

