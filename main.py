from flask import Flask
import pyautogui as ag

app = Flask(__name__)

# Create a route for using the mouse
@app.route('/mouse/<action>')
def mouse(action):
    if action == "left":
        ag.click()
    elif action == "right":
        ag.click(button="right")
    elif action == "middle":
        ag.click(button="middle")
    elif action == "double":
        ag.doubleClick()
    elif action == "triple":
        ag.tripleClick()
    elif action == "scrollup":
        ag.scroll(100)
    elif action == "scrolldown":
        ag.scroll(-100)
    return "Mouse action: " + action  + "\n"

# Create a route for moving the mouse
@app.route('/mouse/move/<int:x>/<int:y>')
def mousemove(x, y):
    ag.moveTo(x, y)
    return "Mouse moved to: " + str(x) + ", " + str(y) + "\n"

#create a route for using the keyboard
@app.route('/keyboard/<action>')
def keyboard(action):
    ag.press(action)
    return "Keyboard action: " + action + "\n"

#create a route for repeating keyboard actions
@app.route('/keyboard/repeat/<action>/<int:count>')
def keyboardrepeat(action, count):
    ag.press(action, presses=count)
    return "Keyboard action: " + action + " repeated " + str(count) + " times\n"

#create a route for shortcuts
@app.route('/keyboard/shortcut/<string:shortcut>')
def keyboardshortcut(shortcut):
    shortcut_list = shortcut.split("+") 
    ag.hotkey(shortcut_list)
    return "Keyboard shortcut: " + shortcut + "\n" 

# Create a route for typing
@app.route('/keyboard/type/<string:word>')
def keyboardtype(word):
    ag.write(word)
    return "Keyboard typed: " + word + "\n"