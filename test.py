import requests
import json
print("Sanity")

with open('main_app/fixtures/full_seed.json') as f:
  my_data = json.load(f)

# f = open('main_app/fixtures/full_seed.json',)
print(type(my_data))
# print(json.dumps(my_data, sort_keys=True, indent=2))

response = requests.get("https://api.teleport.org/api/urban_areas/")
print(response.status_code)
data = response.json()
print(data['_links']['ua:item'][0])

### WHERE ALL CITY INFORMATION WILL GO
cities_data = []
print(type(cities_data))

for i in range(3):
  print(i)
  response2 = requests.get(data['_links']['ua:item'][i]['href'])
  data2 = response2.json()
  # print(data2['_links']['ua:images']['href'])
  picture_response = requests.get(data2['_links']['ua:images']['href'])
  
  # City Name
  city_name = data2['name']

  # City Country
  city_country = data2['_links']['ua:countries'][0]['name']

  # City Picture and Photographer
  picture_parse = picture_response.json()
  picture_url = picture_parse['photos'][0]['image']['mobile']
  photographer = picture_parse['photos'][0]['attribution']['photographer']
  
  cities_data.append(
    {"model": "main_app.city", 
    "pk": i, 
    "fields": {
      "name": city_name, 
      "country": city_country, 
      "city_pic": picture_url, 
      "photographer": photographer,
      "profiles": []
      }
    }
  )

# packed_city_data = json.loads(cities_data)
print(cities_data)
print("------------------------------------------------------------------------------------------")
# combined_data = cities_data + my_data
# print(combined_data)
# combined_data.append(my_data)
# print(json.dumps(combined_data, sort_keys=True, indent=2))
# print(json.loads(combined_data))
print("------------------------------------------------------------------------------------------")
# print(my_data)

# print(json.dumps(cities_data, sort_keys=True, indent=2))

# text = json.dumps(data2['_links']['ua:countries'], sort_keys=True, indent=4)
# print(text)

# CITY MODEL FORMAT
# {"model": "main_app.city", "pk": 1, "fields": {"name": "Denver", "country": "USA", "city_pic": "N/A", "profiles": []}},