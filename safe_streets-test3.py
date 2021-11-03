# API from Rapid API

import requests

url = "https://jgentes-crime-data-v1.p.rapidapi.com/crime"

querystring = {"startdate":"10/19/2021","enddate":"10/25/2021","long":"-122.5076392","lat":"37.757815"}

headers = {
    'x-rapidapi-host': "jgentes-Crime-Data-v1.p.rapidapi.com",
    'x-rapidapi-key': "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
