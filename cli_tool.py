import argparse
import requests

def get_weather(api_key: str, city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The current weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "Failed to get weather data."

def greet_user(name: str, uppercase: bool, repeat: int, api_key: str = None, city: str = None):
    greeting = f"Hello, {name}! Welcome to the CLI tool."
    if uppercase:
        greeting = greeting.upper()
    for _ in range(repeat):
        print(greeting)
    if api_key and city:
        weather_info = get_weather(api_key, city)
        print(weather_info)

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool example with more features.")
    parser.add_argument('name', type=str, help='The name of the person to greet.')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Convert the greeting to uppercase.')
    parser.add_argument('-r', '--repeat', type=int, default=1, help='Number of times to repeat the greeting.')
    parser.add_argument('-k', '--apikey', type=str, help='API key for accessing the weather service.')
    parser.add_argument('-c', '--city', type=str, help='City name to get the weather information.')

    args = parser.parse_args()
    greet_user(args.name, args.uppercase, args.repeat, args.apikey, args.city)

if __name__ == "__main__":
    main()
