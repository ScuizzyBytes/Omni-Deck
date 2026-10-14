from typing import Any, Dict  # noqa: UP035

import psutil


class SystemTelemetry:
    
    @staticmethod
    def get_cpu_load():
        return psutil.cpu_percent(interval=None)

    @staticmethod
    def get_ram_load() -> Dict[str, Any]:  # noqa: UP006
        mem = psutil.virtual_memory()
        return {
            "percent": mem.percent,
            "used_md": mem.used // (1024 ** 2),
            "total_mb": mem.total // (1024 ** 2)
        }

    @staticmethod
    def get_disk_load() -> float:
        return psutil.disk_usage("/").percent
        