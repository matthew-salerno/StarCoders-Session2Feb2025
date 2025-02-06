###
# Helper methods for API Client
# API sample client for OMDB API: http://omdbapi.com/
###


import requests
import json
import os
import sys
from collections.abc import Mapping, Iterable

if 'OMDB_API' in os.environ:
  apiKey = os.environ['OMDB_API']
else:
  sys.exit('Could not find OMDB_API environment variable')

# Helper method to call API
def get_info_from_api(title: str) -> dict:
  """
  Return a dictionary containing the API response from an omdbapi search for a title and year
  Raises Exception if there is no response
  """
  url = 'http://www.omdbapi.com/'
  headers = {
    'Accept': 'application/json'
  }
  search_payload = {'t': title, 'apikey': apiKey}
 
  r = requests.get(url=url, params=search_payload, headers=headers)
  responseBody = json.loads(r.text)
  if responseBody['Response'] == "False":
    print(responseBody['Error'])
    raise Exception("Error in the search")
  else:
    return responseBody
   
# ******************************************************

# This part of the code will only run when this file is run*, we use it to tell the user to run main.py
# * This code would not run if we imported this file from another, for example.
if __name__ == "__main__":
  print("Try running main.py instead!")
