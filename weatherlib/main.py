#!/usr/bin/env python3

from weatherlib.weatherlookup.weather_api import WeatherAPI
from weatherlib.weatherlookup.user_input import UserInput


def main():
    weather_api = WeatherAPI()
    user_input = UserInput()

    user_input.show_welcome_message()

    while True:
        location = user_input.get_location()

        if user_input.should_exit(location):
            user_input.show_goodbye_message()
            break

        if not location:
            user_input.show_invalid_location_message()
            continue

        weather_info = weather_api.get_weather(location)

        if weather_info:
            weather_api.display_weather(weather_info)
        else:
            print(f"Could not fetch weather information for '{location}'. Please try again.\n")


if __name__ == "__main__":
    main()