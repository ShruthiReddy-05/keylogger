# Keylogger with Real-Time Flask API Monitoring

## Overview

This repository contains a Python-based keylogger that captures keyboard input at the OS level and streams it in real time to a Flask-based web dashboard. The project demonstrates core operating system concepts, including process management, file I/O, multiprocessing, and inter-process communication (IPC).

> **Disclaimer:**  
> This project is for educational and research purposes only. Do **not** use it for unauthorized monitoring or malicious activity.

---

## Features

- Captures all keystrokes using low-level OS hooks (`pynput`)
- Sends keystrokes to a Flask API in real time via multiprocessing and a queue
- Stores keystrokes securely in a log file
- Provides a web dashboard for live monitoring and log management
- Demonstrates core OS concepts: process management, file I/O, multiprocessing, IPC

---

## Project Structure

```
├── keylogger.py      # Keylogger process (captures keystrokes, sends to API)
├── api.py            # Flask API (receives, logs, and displays keystrokes)
└── README.md         # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/keylogger-flask-os.git
    cd keylogger-flask-os
    ```

2. **Install dependencies:**
    ```bash
    pip install flask pynput
    ```

---

## Usage

1. **Start the Flask API server:**
    ```bash
    python api.py
    ```
    This will start the web dashboard on [http://127.0.0.1:1344](http://127.0.0.1:1344).

2. **Run the keylogger process:**
    ```bash
    python keylogger.py
    ```
    The keylogger will capture keystrokes and send them to the API.

3. **View the dashboard:**
    - Open your browser and go to [http://127.0.0.1:1344/dashboard](http://127.0.0.1:1344/dashboard)
    - You will see a live feed of captured keystrokes.
    - Use the "Clear Logs" link to erase the log file.

---

## File Descriptions

- **keylogger.py**  
  Captures keystrokes using `pynput` and sends them to the Flask API using a multiprocessing queue.

- **api.py**  
  Flask server that receives keystrokes, logs them to `keystrokes.log`, and serves a real-time dashboard.

---

## OS Concepts Demonstrated

- **Process Management:**  
  Keylogger and API run as separate processes, managed using Python’s `multiprocessing`.

- **File I/O:**  
  Keystrokes are written to a log file for persistence and review.

- **Multiprocessing:**  
  Enables parallel execution of the keylogger and API server.

- **Inter-Process Communication (IPC):**  
  Uses a multiprocessing queue to transfer data between processes.

---

## Security & Ethics

- Only use this software on systems you own or have explicit permission to monitor.
- Do not use for malicious purposes.
- Logs are stored locally and are not encrypted by default.

---

## Troubleshooting

- **Port already in use:**  
  Change the port in `api.py` if 1344 is occupied.
- **No keystrokes captured:**  
  Ensure you have the necessary OS permissions and are running Python with sufficient privileges.

---

## References

- [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html)
- [Flask documentation](https://flask.palletsprojects.com/)
- [pynput documentation](https://pynput.readthedocs.io/)

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue to discuss your ideas or report bugs.

---

**Educational Use Only. Unauthorized use is strictly prohibited.**
