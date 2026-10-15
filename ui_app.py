import customtkinter as ctk
from api_client import ApiClient
from config_manager import ConfigManager
from PIL import Image
from telemetry import SystemTelemetry


class UIApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.config_manager = ConfigManager()
    self.settings = self.config_manager.config

    self.title("Cyberpunk System HUD")
    self.geometry("400x500")

    self.api_client = ApiClient("Berlin")

    self.title_label = ctk.CTkLabel(
        self, text="SYSTEM TELEMETRY HUD", font=("Arial", 20, "bold"), text_color="green"
    )
    self.title_label.pack(pady=20)

    self.cpu_label = ctk.CTkLabel(
        self, text="CPU Load: 0%", font=("Arial", 14, "bold")
    )
    self.cpu_label.pack(pady=10)

    self.ram_label = ctk.CTkLabel(
        self, text="RAM Load: 0%", font=("Arial", 14, "bold")
    )
    self.ram_label.pack(pady=5)

    self.disk_label = ctk.CTkLabel(
        self, text="DISK Load: 0%", font=("Arial", 14, "bold")
    )
    self.disk_label.pack(pady=5)

    self.weather_label = ctk.CTkLabel(
        self, text="Weather: Loading...", font=("Arial", 14, "bold")
    )
    self.weather_label.pack(pady=15)

    self.button1 = ctk.CTkButton(self, font=("Arial", 14, "bold"), text="Click to Change")

    self.button1.pack(pady=20)

    weather = self.api_client.get_weather_data()
    city_name = weather["city"]

    image_path = f"My First Project/assets/{city_name}.jpg"

    City_image = Image.open(image_path)

    self.city_img = ctk.CTkImage(light_image=City_image, dark_image=City_image, size=(300, 150))

    self.Ip_City = ctk.CTkLabel(self, text="", image=self.city_img)

    self.Ip_City.pack(pady=15)

    self.update_loop()

  def update_loop(self):

    cpu = SystemTelemetry.get_cpu_load()
    ram = SystemTelemetry.get_ram_load()
    disk = SystemTelemetry.get_disk_load()

    weather = self.api_client.get_weather_data()

    self.cpu_label.configure(text=f"CPU Load: {cpu}%")
    self.ram_label.configure(
        text=f"RAM Load: {ram['percent']}% ({ram['used_md']}MB / {ram['total_mb']}MB)"
    )
    self.disk_label.configure(text=f"DISK Load: {disk}%")

    self.weather_label.configure(
        text=f"Weather: {weather['temp']}°C | {weather['desc']}"
    )

    interval = self.settings.get("refresh_rate_ms", 1000)
    self.after(interval, self.update_loop)



app = UIApp()
app.mainloop()

