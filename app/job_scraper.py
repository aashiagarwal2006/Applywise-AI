import requests
import json

def fetch_internships(query="software engineering intern", pages=10):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "d9c88da11dmsh6523350b2bdc044p10e1d1jsnf584f315d6be",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    all_jobs = []
    for page in range(1, pages + 1):
        params = {"query": query, "page": page}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        for job in data.get("data", []):
            all_jobs.append({
                "title": job["job_title"],
                "company": job["employer_name"],
                "location": job.get("job_city", "Remote"),
                "description": job["job_description"]
            })

    return all_jobs

def save_jobs_to_file(jobs, filename="data/jobs_cache.json"):
    with open(filename, "w") as f:
        json.dump(jobs, f, indent=2)

# === RUN THIS TO FETCH AND SAVE JOBS ===
if __name__ == "__main__":
    jobs = fetch_internships()
    save_jobs_to_file(jobs)
    print(f"Saved {len(jobs)} internships to data/jobs_cache.json")
