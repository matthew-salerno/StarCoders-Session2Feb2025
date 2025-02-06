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
  try:
    response = h.get_info_from_api(title)
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
    critics_score =  h.parse_critics_score(response['Ratings'])
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
