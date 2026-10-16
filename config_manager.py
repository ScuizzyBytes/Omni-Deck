import json
import os


class ConfigManager:
    def __init__(self, filename="My First Prroject/settings.json") -> None:
        self.filename = filename
        self.default_config = {
            "theme": "Dark",
            "accent_color": "#00ff66",
            "refresh_rate_ms": 1000,
            "default_city": "Berlin"
        }
        self.config = self.load_config()

    def load_config(self) -> dict:
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            self.save_config(self.default_config)
            return self.default_config

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return self.default_config

    def save_config(self, settings: dict) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
