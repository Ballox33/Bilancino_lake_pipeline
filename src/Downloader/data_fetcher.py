from config import *
import os
import requests
from datetime import datetime

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

def data_downloader(url=DATA_2026_URL, save_path=DATA_2026_PATH):
    print("Downloading data from :", url)
    
    try:
        response = requests.get(url,timeout = 10, headers=headers)
        response.raise_for_status()  # error if status != 200
    except requests.RequestException as e:
        print(f"Error downloading data: {e}")
        return
    
    print("Data downloaded successfully.\n")

    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("Data written successfully.")

    return

if __name__ == "__main__":
    data_downloader() 