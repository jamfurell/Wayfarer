### Must install requests to use the API call functions
# 'pip install requests' 

### Must run this command to create a j_seed.json file of your database 
# python manage.py dumpdata --natural-foreign --natural-primary >  main_app/fixtures/j_seed.json

### After running this module and you have a newly filled j_seed.json, you now must use it to fil your database
# python manage.py loaddata j_seed.json

import requests
import json
print("Sanity")

with open('main_app/fixtures/j_seed.json') as f:
  my_data = json.load(f)
print(type(my_data))

# Initial API request
response = requests.get("https://api.teleport.org/api/urban_areas/")
# Check status code, 200 means API call successfully returned data
print(response.status_code)
# Put data into a usable format
city_list = response.json()
# Test response
print(city_list['_links']['ua:item'][0])

### WHERE ALL CITY INFORMATION WILL GO
cities_data = []
print(type(cities_data))

# Loop the API requests and append the formatted data to cities_data (266 cities in the database at this point in time)
number_of_cities = 266
for i in range(number_of_cities):
  
  response2 = requests.get(city_list['_links']['ua:item'][i]['href'])
  city_data = response2.json()
  
  # City Name
  city_name = city_data['name']

  # City Country
  city_country = city_data['_links']['ua:countries'][0]['name']

  # City Picture and Photographer
  picture_response = requests.get(city_data['_links']['ua:images']['href'])
  picture_parse = picture_response.json()
  picture_url = picture_parse['photos'][0]['image']['mobile']
  photographer = picture_parse['photos'][0]['attribution']["photographer"]
  
  # Create list of new city data
  cities_data.append(
    {"model": "main_app.city", 
    "pk": i + 1, 
    "fields": {
      "name": city_name, 
      "country": city_country, 
      "city_pic": picture_url, 
      "photographer": photographer,
      "profiles": []
      }
    }
  )
  # print out cities_data progress for the sweet asthetic
  print(i + 1, city_name + ",", city_country)

# # Open and add the new data to the j_seed.json file
### -------------- COMMENTED OUT FOR YOUR AND MY SAFTEY (Uncomment next 5 lines to leave testing mode)
combined_data = cities_data + my_data
f = open('main_app/fixtures/j_seed.json', 'w')
json.dump(combined_data, f)
# Close the file
f.close()
print("Successfully added", number_of_cities,  "new cities")

### CITY MODEL FORMAT
# {"model": "main_app.city", "pk": 1, "fields": {"name": "Denver", "country": "USA", "city_pic": "https://d13k13wj6adfdf.cloudfront.net/urban_areas/aarhus-67c2f42848.jpg", "photographer": "Calvin Smith", "profiles": []}},

# text = json.dumps(data2['_links']['ua:countries'], sort_keys=True, indent=4)
# print(text)