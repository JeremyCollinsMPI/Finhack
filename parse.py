import requests
import os
from retry import retry
import pymongo

stanford_ip = os.environ["stanford_ip"]
url = 'http://' + stanford_ip + ':9000/?properties={"annotators":"parse","outputFormat":"json"}'

def parse(sentence):
  response = requests.post(url, 'On August 24 , 2012 , a jury returned a verdict awarding the Company $ 1.05 billion in its lawsuit against Samsung Electronics and affiliated parties in the United States District Court , Northern District of California , San Jose Division .')
  dict = response.json()
  return dict['sentences'][0]['parse']
