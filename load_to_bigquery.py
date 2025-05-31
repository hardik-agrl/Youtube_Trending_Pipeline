import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
FILE_NAME = "raw/trending_IN_20250530_173831.json" 
DATASET_ID = "youtube_trending"
TABLE_ID = "trending_videos"

client = bigquery.Client()

def load_data_from_gcs():
    uri = f"gs://{BUCKET_NAME}/{FILE_NAME}"
    
    table_ref = client.dataset(DATASET_ID).table(TABLE_ID)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    load_job = client.load_table_from_uri(
        uri,
        table_ref,
        job_config=job_config
    )

    print(f"Started job: {load_job.job_id}")
    load_job.result()
    print("Data loaded into BigQuery table.")

if __name__ == "__main__":
    load_data_from_gcs()
