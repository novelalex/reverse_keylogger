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
Help displays all the commands
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
Type `help <command>` to get more information about a command
```
ReverseKeylogger> help mm
Mouse movement:
  <x> <y> - Move the mouse to the coordinates
```

You could write scripts to if you really wanted to
```bash
$ echo "ks win+r
> kt cmd
> ka enter" >> open_terminal.txt

$ echo "http://localhost:5000" | cat - open_terminal.txt | python3 reverse-keylogger.py
```

At the end of the day this is done with `GET` requests, so you can just use a browser

![Browser navigating to http://localhost:5000/mouse/move/100/300](https://github.com/novelalex/reverse_keylogger/blob/master/media/browser_screenshot.png?raw=true)

Or curl
```bash
curl http://localhost:5000/mouse/move/100/300
```

---
All of this implies that you have the power to start a server on the target computer, if you do, you probably don't need this.
