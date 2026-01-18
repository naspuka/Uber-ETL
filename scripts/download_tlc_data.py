import requests
import os
from datetime import datetime

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
FILES = ["yellow_tripdata_2023-01.parquet"]

os.makedirs("data/bronze", exist_ok=True)
for file in FILES:
    url = f"{BASE_URL}/{file}"
    local_path = f"data/bronze/{file}"

    if os.path.exists(local_path):
        print(f"{file} already exists")
        continue
    print(f"Downloading {file}")
    r = requests.get(url, timeout=60) #requests.exceptions.Timeout timeout return
    r.raise_for_status() #requests.exceptions.HTTPError status code return

    with open(local_path, "wb") as f:
        f.write(r.content)
    print(f"Saved {file}")
