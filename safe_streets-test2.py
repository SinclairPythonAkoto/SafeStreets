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
    postcode = input("What is your postcode or street address? ")
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


user_address = user_address()
address = f"{user_address}, United Kingdom"
location = convert_postcode(address)
latitude = location["lat"]
longitude = location["lon"]

# getting current month
month = datetime.datetime.now()
month = month.strftime("%m")

# dynamic crime stats via month
# connect to Police API
response = requests.get(
    f'https://data.police.uk/api/crimes-at-location?date=2020-{month}&lat={latitude}&lng={longitude}'
)

# convert json months into dictionaries
crime_stats = response.json()[0:]


print(crime_stats['outcome_status'])

# print crime stats
# print("2020 Crime Report of Area: ")
# for stats in range(len(crime_stats)):
#     print(f"Category: {crime_stats[stats]['category']}")
#     print(f"Crime ID: {crime_stats[stats]['id']}")
#     print(f"Location: {crime_stats[stats]['location']['street']['name']}")
#     print(f"Outcome: {crime_stats[stats]['outcome_status']}")
#     print("\n")
