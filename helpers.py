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

# Helper method to parse the different critic ratings input
def parse_critics_score(critic_scores: Iterable[Mapping[str, float]]) -> float:
  """
  returns total critic score from list of critic scores from different sources
  """
  num_of_ratings = len(critic_scores)
  total_score = 0.0
 
  for critic_rating in critic_scores:
    source = critic_rating['Source']
    value = critic_rating['Value']
    score = 0.0

    if source == 'Internet Movie Database':
      value = float(value.split("/")[0])
      score = value * 10
    elif source == 'Rotten Tomatoes':
      score = float(value.split("%")[0])
    elif source == 'Metacritic':
      score = float(value.split("/")[0])

    total_score += round(score / num_of_ratings, 1)

  return total_score

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