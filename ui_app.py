import customtkinter as ctk
from api_client import ApiClient
from telemetry import SystemTelemetry


class UIApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    # Настройки окна
    self.title("Cyberpunk System HUD")
    self.geometry("400x500")

    # Подключаем наши модули (сеть и железо)
    self.api_client = ApiClient("Berlin")

    # 1. Заголовок
    self.title_label = ctk.CTkLabel(
        self, text="SYSTEM TELEMETRY HUD", font=("Arial", 20, "bold")
    )
    self.title_label.pack(pady=20)

    # 2. Метки для процессора, памяти и диска
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

    # 3. Метка для погоды (сетевой разведчик)
    self.weather_label = ctk.CTkLabel(
        self, text="Weather: Loading...", font=("Arial", 14, "bold")
    )
    self.weather_label.pack(pady=15)

    # Запускаем наш бесконечный цикл обновления
    self.update_loop()

  def update_loop(self):
    # Получаем данные о железе
    cpu = SystemTelemetry.get_cpu_load()
    ram = SystemTelemetry.get_ram_load()
    disk = SystemTelemetry.get_disk_load()

    # Получаем данные из сети
    weather = self.api_client.get_weather_data()

    # Обновляем текст в метках через .configure()
    self.cpu_label.configure(text=f"CPU Load: {cpu}%")
    self.ram_label.configure(
        text=f"RAM Load: {ram['percent']}% ({ram['used_md']}MB / {ram['total_mb']}MB)"
    )
    self.disk_label.configure(text=f"DISK Load: {disk}%")

    # Обновляем погоду
    self.weather_label.configure(
        text=f"Weather: {weather['temp']}°C | {weather['desc']}"
    )

    # Повторяем этот метод ровно через 1000 миллисекунд (1 секунду)
    self.after(1000, self.update_loop)

app = UIApp()
app.mainloop()

