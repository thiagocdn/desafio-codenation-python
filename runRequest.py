import requests
import json

def request(url, token):
  rawResponse = requests.get(url + 'generate-data', params={'token': token})
  response = json.loads(rawResponse.content)
  with open('answer.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)
  return response
