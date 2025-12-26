import requests
import json
import time
import os

ES_URL = os.environ.get("ES_URL", "http://elasticsearch:9200")
INDEX_NAME = "documents"

HEADERS = {"Content-Type": "application/json"}

def create_index():
    mapping = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "content": {"type": "text"},
                "tags": {"type": "keyword"}
            }
        }
    }

    for _ in range(5):
        try:
            response = requests.put(
                f"{ES_URL}/{INDEX_NAME}",
                headers=HEADERS,
                data=json.dumps(mapping),
                timeout=5
            )

            if response.status_code in [200, 201]:
                print("Index created")
                return
            elif response.status_code == 400:
                print("Index already exists")
                return

        except requests.exceptions.RequestException:
            print("Elasticsearch not ready, retrying...")
            time.sleep(3)
