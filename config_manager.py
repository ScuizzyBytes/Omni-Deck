import json
from pathlib import Path
from typing import Any, Dict


class ConfigManager:
    def __init__(self, filepath: str = "settings.json") -> None:
        self.filepath = Path(filepath)
        self.default_config: Dict[str, Any] = {
            "theme": "Dark",
            "refresh_rate_ms": 1000,
            "accent_color": "#00ff66"
        }
        self.config = self.load_config

    def load_config(self) -> Dict[str, Any]:

        if self.filepath.exists():
            self.save_config(self.default_config)
            return self.default_config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return self.default_config

    def save_config(self, config_data: Dict[str, Any]) -> None:
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4)
        
