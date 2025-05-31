Youtube_Trending_Pipeline

The Project fetches trending YouTube videos using the YouTube Data API, stores the data in Google Cloud Storage, and loads it into a BigQuery table for analysis.

files:
* fetch_trending.py: Fetches trending videos and uploads to GCS.
* load_to_bigquery.py:	Loads JSON file from GCS into BigQuery table.

Tech Stack:
* Python
* YouTube Data API v3
* Google Cloud Storage
* BigQuery
* google-cloud-storage
* google-cloud-bigquery
* python-dotenv.

References:
* How to build a data pipeline with Google Cloud - https://www.youtube.com/watch?v=yVUXvabnMRU
