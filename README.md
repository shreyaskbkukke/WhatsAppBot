# WhatsApp Message Delivery Bot

## Overview
This Python script automates sending messages on WhatsApp using the web version. It reads phone numbers and messages from a CSV file and sends them one by one, including optional features like images and additional documents.

## Features
- **Message Sending:** Sends messages to WhatsApp contacts using the web version.
- **Dynamic Content:** Supports dynamic content, including text, images, and additional documents.
- **Automated Process:** The script automates the message-sending process, reducing manual effort.

## Dependencies
- [pandas](https://pandas.pydata.org/): Data manipulation library.
- [webbrowser](https://docs.python.org/3/library/webbrowser.html): Module for opening web browsers.
- [time](https://docs.python.org/3/library/time.html): Module for handling time-related functions.
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/): Library for GUI automation.

## Usage
1. Install the required dependencies using:
    ```
    pip install pandas webbrowser pyautogui
    ```
2. Prepare a CSV file named `victim.csv` with columns `PhNumber` and `Message`.
3. Set the configuration options in the script, such as `Images`, `Addmore`, and `ImageName`.
4. Run the script:
    ```
    python your_script_name.py
    ```

## Configuration
- `Images`: Set to `True` if you want to include images in your messages.
- `Addmore`: Set to `True` if you want to include additional documents in your messages.
- `ImageName`: Specify the name of the image file to be included.

## Notes
- Ensure your system is ready for GUI automation.
- The script opens WhatsApp Web in a web browser, so keep it logged in before running the script.

## Disclaimer
This script is for educational purposes only. Use it responsibly and respect privacy.

## Author
Your Name

## License
This project is licensed under the CC License - see the [LICENSE](LICENSE) file for details.

## WhatsAppBot
+ This python application can send dynamic WhatsApp messages to any number of people without getting your number into the spam lists.
+ This bot can send messages with greeting text, text, links, and multiple attachments that can be different foreach people.
+ No any any extream effort needed just give the list people and and click a button then just relax. Bot take care all the work need. just we have to monitor the activities.
