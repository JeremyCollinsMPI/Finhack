import requests
import os
from retry import retry
import gzip

stanford_ip = os.environ["stanford_ip"]
url = 'http://' + stanford_ip + ':9000/?properties={"annotators":"parse","outputFormat":"json"}'

@retry(tries=3, delay=10)
def segment_file(filename, part=None, limit=20000):
  if '.gz' in filename:
    file = gzip.open(filename, 'rt', encoding = 'utf-8').read()
  else:
    file = open(filename, 'r', encoding = 'utf-8').read()
  if not part == None:
    end = (((part+1)*limit)+500)
    end = min(end, len(file))
    file = file[(part*limit):end]
  response = requests.post(url, file.encode('utf-8'))
  dict = response.json()
  return dict
  
def find_tokens(dict):
  token_sets = []
  for i in range(len(dict['sentences'])):
    tokens = dict['sentences'][i]['tokens']
    tokens = [x['originalText'] for x in tokens]
    token_sets.append(tokens)
  return token_sets

def token_set_to_sentence(token_set):
  return ' '.join(token_set)


