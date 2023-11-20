import requests
api_key = 'd9eed6b80a1c4271974224250233110'
location = 'Portland'

# get current weather
base = 'http://api.weatherapi.com/v1/'
method = 'current.json'
params = {
    'key': api_key,
    'q': location
}
response = requests.get(base+method, params=params)
#print(response)
current_weather_data = response.json()
print(current_weather_data)

