import requests
import json
from typing import Optional, Dict, Any


class WeatherAPI:
    def __init__(self):
        self.base_url = "https://wttr.in/"

    def get_weather(self, location: str) -> Optional[Dict[str, Any]]:
        try:
            url = f"{self.base_url}{location}?format=j1"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            weather_data = response.json()
            return self._format_weather_data(weather_data)

        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
        except json.JSONDecodeError:
            print("Error parsing weather data")
            return None

    def _format_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            current = data['current_condition'][0]
            weather_info = data['weather'][0]

            return {
                'location': data['nearest_area'][0]['areaName'][0]['value'],
                'country': data['nearest_area'][0]['country'][0]['value'],
                'temperature_c': current['temp_C'],
                'temperature_f': current['temp_F'],
                'condition': current['weatherDesc'][0]['value'],
                'humidity': current['humidity'],
                'wind_speed': current['windspeedKmph'],
                'wind_direction': current['winddir16Point'],
                'feels_like_c': current['FeelsLikeC'],
                'feels_like_f': current['FeelsLikeF'],
                'max_temp_c': weather_info['maxtempC'],
                'min_temp_c': weather_info['mintempC']
            }
        except (KeyError, IndexError) as e:
            print(f"Error formatting weather data: {e}")
            return None

    def display_weather(self, weather_info: Dict[str, Any]) -> None:
        if not weather_info:
            print("No weather information available")
            return

        print(f"\n{'='*50}")
        print(f"Weather for {weather_info['location']}, {weather_info['country']}")
        print(f"{'='*50}")
        print(f"Current Temperature: {weather_info['temperature_c']}°C ({weather_info['temperature_f']}°F)")
        print(f"Feels Like: {weather_info['feels_like_c']}°C ({weather_info['feels_like_f']}°F)")
        print(f"Condition: {weather_info['condition']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind: {weather_info['wind_speed']} km/h {weather_info['wind_direction']}")
        print(f"Today's Range: {weather_info['min_temp_c']}°C - {weather_info['max_temp_c']}°C")
        print(f"{'='*50}\n")