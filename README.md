# ⚡ CYBERPUNK SYSTEM HUD ⚡

A high-performance, modular telemetry and dynamic interface constructed in Python using **CustomTkinter** and **PIL**. Designed with strict asynchronous thread isolation, real-time hardware monitoring, and low-latency UI responsiveness.

---

## 🛠️ Key Architectural Principles

This application avoids blocking standard I/O calls on the main execution thread by leveraging clean Python concurrency patterns:

1. **Non-Blocking Main Thread (UI Thread):**
   * The primary Tkinter loop (`mainloop`) strictly manages rendering, widget redraws, and user interaction.
   * Direct network calls (weather API) and heavy file operations (image I/O with PIL) are explicitly forbidden on this thread to eliminate window freezing.

2. **Isolated Background Worker (`threading.Thread`):**
   * Heavy telemetry fetching (CPU/RAM metrics, external network requests) runs on an isolated background worker.
   * Periodic updates are orchestrated without locking the main thread.

3. **Thread-Safe Data Synchronization (`self.after` / `queue.Queue`):**
   * Background threads pass gathered system metrics and status payloads back to the UI thread safely, avoiding data races and GUI thread-safety violations.

---

## 🏗️ Project Structure

```
cyberpunk-hud/
│
├── main.py                 # Application entry point & bootstrapping
├── ui_app.py               # CustomTkinter main window & widget layout
├── worker.py               # Background worker (Threading & Data Queueing)
├── api_client.py           # Network requests & weather service abstraction
├── system_monitor.py       # Hardware telemetry (CPU, RAM, Disk, System)
│
└── assets/                 # Cached UI graphics & static resources
    ├── Tokyo.jpg
    ├── NightCity.jpg
    └── default.jpg
```

---

## ⚡ Features & Modular Roadmap

- [x] **Asynchronous Telemetry Pipeline:** Fully separated backend data fetcher and frontend rendering engine.
- [x] **Dynamic Weather & City Sync:** Fetch local weather data and adaptively trigger graphic overlays.
- [ ] **Overload Alert Protocol:** Automatic UI style/color shift (Cyber Green $\rightarrow$ Alert Red) when system metrics cross predefined stress thresholds.
- [ ] **Asset Manager Caching:** In-memory image loading and scaling to avoid disk I/O lag during visual transitions.
- [ ] **Hot-Reload Config Watcher:** Dynamically reload local settings/JSON configs without restarting the application process.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.10+** installed on your host system.

### Dependencies

Install the required core libraries:

```bash
pip install customtkinter pillow psutil requests
```

### Running the Application

Execute the entry point from the root directory of the project:

```bash
python main.py
```

---

## 🔧 Core Mechanics Overview

### Background Worker Pattern

```python
# Thread Communication Paradigm:
# [Hardware / API]  --->  (Background Thread / Worker)  --->  [ queue.Queue / self.after ]  --->  (Main GUI Thread)
```

1. **Data Ingestion:** The background thread queries hardware specs and APIs on a dedicated cycle.
2. **Payload Dispatch:** Once the payload is ready, it queues the update or invokes a thread-safe UI delegate via `self.after(0, callback)`.
3. **UI Render:** The main GUI thread updates labels and meters without dropped frames or interface input lag.
