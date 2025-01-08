import requests

# Function to get weather data
def get_weather(city_name):
    api_key = "216525736cde4fd4a29145843250801" 
    base_url = "https://api.weatherapi.com/v1/current.json"
    
    url = f"{base_url}?key={api_key}&q={city_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        location = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"] 
        weather_description = data["current"]["text"]
        
    except requests.exceptions.RequestException as e:
        print("Error fetching the weather data")
    except KeyError:
        print("Error: Unexpected response format from the API.")
        
city = input("Enter a city name: ")

get_weather(city)   

# m = min([5,3,2,11,8,9])
# print(m)

# import builtins
# print(dir(builtins))

# x = 'global x'
# def outer():
#     x = 'outer x'
    
#     def inner(): 
#         # nonlocal x
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)
    
# outer()
# print(x)