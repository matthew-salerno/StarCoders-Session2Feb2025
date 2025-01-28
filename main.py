###
# Starter Code
#
# DTCC Star Coders Year 1 Session 2
###

import helpers as h

# This is the Main method. The entry point for the Python script run
if __name__ == "__main__":

  #inputs from the user. How should we take in the inputs?
  title = input("Enter the name of the movie: ")
  year = '*'
  try:
    response = h.get_info_from_api(title, year)
    print(response)
   
    # ***** What do we do with the Response? *****

    #Criteria:
    #critics rating
    #genre
    #year range
    #MPAA rating

    # ***** Critics Ratings *****
    critics_score = response['Ratings']
    score = h.parse_critics_score(critics_score)
    print("Total Critics Score across all ratings is:", score)

    # ***** Genres *****
    #TODO: Parse Genres
   
    # ******************

    # ***** Year *****
    # TODO: Parse Year

    # ******************

    # ***** MPAA Rating *****
    # TODO: Parse MPAA Ratings

    # ******************
   
    # TODO: Determine watch: yes or no?
    MINIMUM_SCORE = 70
    if score > MINIMUM_SCORE:
      print("It's a great Movie!")
    else:
      print("Terrible movie... don't watch it")

    #Anything else we can do?
 
  except Exception as e:
    print(e)
    print("Try another search")

  # ******************
