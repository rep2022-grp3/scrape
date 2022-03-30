import requests
import json

headers = {"Content-Type": "application/json"}

# Reference: https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html
data = json.dumps(
    {
        "from": 0,
        "size": 10000, # https://www.elastic.co/guide/en/elasticsearch/reference/7.16/paginate-search-results.html
        "query": {
            "bool": {
                "must": [
                    {"term": {"aggregation": "hourly"}},
                    {"term": {"area": "Kota Tangerang"}},
                    {"term": {"unit": "C"}},
                ]
            }
        },
    }
)

response = requests.post(
    "https://api.faraday.id/bmkg/forecast", headers=headers, data=data
)

import pandas as pd

df = pd.DataFrame(response.json()["payload"])
