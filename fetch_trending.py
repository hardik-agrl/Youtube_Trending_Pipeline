import os
import requests
import json
from datetime import datetime
from google.cloud import storage
from dotenv import load_dotenv


load_dotenv()



API_KEY = os.getenv("YOUTUBE_API_KEY")
BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
SERVICE_ACCOUNT = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT

def fetch_trending(country_code='IN', max_results=25):
    print(f"Fetching trending videos for {country_code}...")
    
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": country_code,
        "maxResults": max_results,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    
    
    data["fetchedAt"] = datetime.utcnow().isoformat()
    data["country"] = country_code

    return data

def save_to_gcs(data, country_code):
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    filename = f"trending_{country_code}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    blob = bucket.blob(f"raw/{filename}")

    blob.upload_from_string(json.dumps(data), content_type='application/json')
    print(f"Uploaded to GCS: gs://{BUCKET_NAME}/raw/{filename}")

if __name__ == "__main__":
    country = "IN"  
    data = fetch_trending(country)
    save_to_gcs(data, country)
