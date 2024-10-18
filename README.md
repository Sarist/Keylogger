# Keylogger in Python

## Overview

This project is a simple keylogger implemented in Python, designed for educational purposes. It captures keyboard events and logs them to a file, allowing you to see what keys were pressed during its execution. This tool is meant to be used in a controlled environment for learning and testing purposes only.

### Features

- **Key Capture**: Logs keystrokes to a file for review.
- **Special Key Handling**: Identifies and logs special keys (e.g., Shift, Ctrl, etc.).
- **Simple Command-Line Interface**: Easy to run from the terminal with minimal setup.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Important Considerations](#important-considerations)
- [License](#license)

## Requirements

This keylogger requires the following:

- **Python 3.x**: Ensure that Python is installed on your machine.
- **Pynput Library**: A library for monitoring keyboard input.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
   ```

2. **Install Dependencies**:

   You need the `pynput` library to run the keylogger. Install it using pip:

   ```bash
   pip install pynput
   ```

## Usage

1. **Run the Keylogger**:

   Open a terminal and navigate to the directory where you saved the keylogger. Then run:

   ```bash
   python3 keylogger.py
   ```

2. **Capture Keystrokes**:

   The keylogger will start running and will log all keystrokes to a file named `keylogger.log`.

3. **Stop the Keylogger**:

   To stop the keylogger, press the **Esc** key on your keyboard.

4. **View Logged Keystrokes**:

   After stopping the keylogger, you can view the captured keystrokes by opening the `keylogger.log` file:

   ```bash
   cat keylogger.log
   ```

## Important Considerations

- **Ethical Use**: This keylogger is intended for educational and testing purposes only. Only use it on systems that you own or have explicit permission to monitor.
- **Legal Disclaimer**: Unauthorized interception of keystrokes is illegal and can lead to severe legal consequences. Always ensure you have consent before running this tool.
- **Privacy**: Respect user privacy and confidentiality. Be mindful of the ethical implications of using a keylogger.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
