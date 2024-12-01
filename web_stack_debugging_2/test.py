import requests
import json

url = "https://ebay-sold-items-api.herokuapp.com/findCompletedItems"

payload = json.dumps({
  "keywords": "iPhone",
  "max_search_results": "25",
  "category_id": "15032",
  "remove_outliers": True,
  "site_id": "0",
  "aspects": [
    {
      "name": "Model",
      "value": "Apple iPhone X"
    },
    {
      "name": "Network",
      "value": "Unlocked"
    },
    {
      "name": "Storage Capacity",
      "value": "256 GB"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)