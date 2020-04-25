import requests
import json


def post(url, postData, token):
  with open('answer.json', 'w', encoding='utf-8') as file:
      json.dump(postData, file, ensure_ascii=False, indent=4)
    
  answer = { 'answer' : open('answer.json','rb') }
  results = requests.post(url + 'submit-solution', files=answer, params={'token': token})
  print(results.status_code)
  print(results.text)