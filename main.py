from flask import Flask, request
import pyautogui as ag
import time
from flask import send_file


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
    return "Mouse action: " + action

# Create a route for moving the mouse
@app.route('/mouse/move/<int:x>/<int:y>')
def mousemove(x, y):
    ag.moveTo(x, y)
    return "Mouse moved to: " + str(x) + ", " + str(y)

#create a route for using the keyboard
@app.route('/keyboard/<action>')
def keyboard(action):
    ag.press(action)
    return "Keyboard action: " + action

#create a route for repeating keyboard actions
@app.route('/keyboard/repeat/<action>/<int:count>')
def keyboardrepeat(action, count):
    ag.press(action, presses=count)
    return "Keyboard action: " + action + " repeated " + str(count) + " times"

#create a route for shortcuts
@app.route('/keyboard/shortcut/<string:shortcut>')
def keyboardshortcut(shortcut):
    shortcut_list = shortcut.split("+") 
    ag.hotkey(shortcut_list)
    return "Keyboard shortcut: " + shortcut

# Create a route for typing
@app.route('/keyboard/type/<string:word>')
def keyboardtype(word):
    ag.write(word)
    return "Keyboard typed: " + word

# Create a route for getting the screenshot
@app.route('/screenshot')
def screenshot():
    screenshotName = 'screenshot.png'
    ag.screenshot(f'static/{screenshotName}')
    #serve the screenshot as a file
    return app.send_static_file(screenshotName)

# Create a route for live streaming the screen by using js to refresh image
@app.route('/stream/<int:ms>')
def stream(ms):
    screenshotName = 'screenshot.png'
    ag.screenshot(f'static/{screenshotName}')
    # js will replace the image every few seconds
    js = f'''<script>
    function refresh(){{
        document.getElementById("screen").src = "/screenshot?" + Math.random();
    }}
    setInterval(refresh, {ms}); 
    </script>
    '''
    return '<body>' +f'<img id="screen" src="/screenshot?" + Math.random()>' + js + '</body>'

# Create a route for serving the screenshot image
@app.route('/screenshot')
def serve_screenshot():
    screenshotName = 'screenshot.png'
    return send_file(f'static/{screenshotName}', mimetype='image/png')
    