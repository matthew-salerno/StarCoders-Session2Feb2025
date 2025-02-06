###
# Starter Code
#
# DTCC Star Coders Year 1 Session 2
###

import omdb_api as api

# This is the function we'll be working with
def main():
  #inputs from the user. How should we take in the inputs?
  title = input("Enter the name of the movie: ")
  try:
    response = api.get_info_from_api(title)
    print("OMDB Response:")
    print(response)
    print()
   
    # ***** What do we do with the Response? *****

    #Criteria:
    #critics rating
    #genre
    #year range
    #MPAA rating

    # ***** Critics Ratings *****
    # We provide critic scores as an example
    critics_score =  parse_critics_score(response['Ratings'])
    print("Total Critics Score across all ratings is:", critics_score)

    # ***** Genres *****
    #TODO: Parse Genres
    print("Genres: Unknown")
   
    # ******************

    # ***** Year *****
    # TODO: Parse Year
    print("Year: Unknown")

    # ******************

    # ***** MPAA Rating *****
    # TODO: Parse MPAA Ratings
    print("MPAA Rating: Unknown")

    # ******************
   
    # TODO: Determine watch: yes or no?
    print("Recommendation: Unknown")

    #Anything else we can do?
 
  except Exception as e:
    print(e)
    print("Try another search")

  # ******************

# We use this function in our example to get critic scores.
# Feel free to add as many other additional functions as you'd like when implementing the other parts of the exercise! 
def parse_critics_score(critic_scores):
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


# This part of the code will only run when this file is run*, we use it to call our main function
# * This code would not run if we imported this file from another, for example.
if __name__ == "__main__":
  main()
