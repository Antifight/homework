import requests


class OpenWeatherMap:
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "e90fab7014064d2c88795d9fd95afa6f"

    def __init__(self, city):
        self.city = city
        self.data = self._fetch_data()

    def _fetch_data(self):
        try:
            response = requests.get(f"{self.API_URL}?q={self.city}&appid={self.API_KEY}")
            response.raise_for_status()  # Выбросит ошибку, если статус не 200
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data: {e}")

    def get_temp(self):
        return round(float(self.data.get('main', {}).get('temp', 273.15)) - 273.15, 1)

    def get_weather(self):
        return self.data.get('weather', [{}])[0].get('main', 'Unknown')

    def get_wind(self):
        return self.data.get('wind', {}).get('speed', 'Unknown')

    def get_city(self):
        return self.data.get('name', 'Unknown')

    def get_any_key(self, *args):
        result = self.data
        for arg in args:
            if isinstance(result, dict):
                result = result.get(arg, None)
            else:
                return None
        return result

    def get_text(self):
        return (f"City: {self.get_city()}\n"
                f"Temperature: {self.get_temp()} °C\n"
                f"Weather: {self.get_weather()}\n"
                f"Wind Speed: {self.get_wind()} m/s")

    def __str__(self):
        return f"{self.get_city()}: {self.get_temp()}°C, {self.get_weather()}, Wind {self.get_wind()} m/s"


def main():
    city = input("Enter city: ")
    try:
        weather = OpenWeatherMap(city)
        print(weather.get_text())
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
