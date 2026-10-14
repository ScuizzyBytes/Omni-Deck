import requests

class ApiClient:
    def __init__(self, default_city: str = "Berlin") -> None:
        self.city = self.get_city_ip() or default_city

    def get_city_ip(self) -> str | None:
        try:
            response = requests.get("http://ip-api.com/json/", timeout=3)
            data = response.json()

            if data.get("status") == "success":
                return data.get("city") 
        except Exception:
            return None

    def get_weather_data(self) -> dict:
        url = f"https://wttr.in/{self.city}?format=j1"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                
                # Достаем текущую температуру и описание из структуры wttr.in
                current = data["current_condition"][0]
                temp = current["temp_C"]
                desc = current["weatherDesc"][0]["value"]
                
                return {
                    "city": self.city,
                    "temp": temp,
                    "desc": desc
                }
        except Exception:
            # Запасной вариант на случай сбоя сети
            return {
                "city": self.city,
                "temp": "--",
                "desc": "Offline"
            }



client = ApiClient()
print(client.get_weather_data())