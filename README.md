# Reverse Keylogger

I had the incredibly stupid idea of making a reverse keylogger, you know how a normal keylogger sends keystrokes from a target computer to the attacker's computer? Well this does the opposite, it sends keystrokes from the attacker's computer to the target computer. 

I have no idea why I made this, but I did. 
It receives `GET` requests using [flask](https://flask.palletsprojects.com/) and then simulates keyboard and mouse events with [pyautogui](https://github.com/asweigart/pyautogui). 

It's not very good, definitely not safe, not useful at all, but it works.

## Installation (please don't)
Clone the repo and install the requirements
```bash
git clone
cd reverse-keylogger
pip install -r requirements.txt
```
Run the server on the target computer
```bash
flask run
```
run the script on the attacker's computer
```bash
python3 reverse-keylogger.py
```
## Usage
The server will be running on port 5000 by default, you can change this by setting the `FLASK_RUN_PORT` environment variable in [.flaskenv](../master/.flaskenv).

The script will prompt you for the target's url
```
Enter the URL: http://localhost:5000
```
After that, you can enter keyboard and mouse events, the script will send them to the target computer.
```
ReverseKeylogger> help
Commands:
  help - Displays this message
  ma - Mouse actions
  mm - Mouse movement
  ka - Keyboard actions
  kr - Keyboard repeat
  ks - Keyboard shortcut
  kt - Keyboard type
  clear - Clear the screen
  quit - Exit the program
```

```
ReverseKeylogger> ks win+r
ReverseKeylogger> kt cmd
ReverseKeylogger> ka enter
```