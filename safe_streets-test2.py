# Safe Streets - find 2020 crime stats with postcode from Police Data API

import requests
import datetime
from geopy.geocoders import Nominatim
import time

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")


# make the user input a function
def user_address():
    """
      Function to prompt the users postcode or address
    """
    postcode input("What is your postcode or street address? ")
    return postcode

# convert postcode to longitude & lattitude
def convert_postcode(address):
    """
      This function returns a location as raw from an address, will repeat until success.
    """
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return convert_postcode(address)
