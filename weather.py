import requests

API_KEY = "bb85300b43334c5ad5bfa491f0e27616"

city = input("Enter City name: ")

url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


response = requests.get(url)
data = response.json()
print("Status Code:", response.status_code)
print("Response:", data)


if response.status_code == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
else:
    print("City not found. Please try again.")
