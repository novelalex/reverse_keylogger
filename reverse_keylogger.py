import requests

print("Reverse Keylogger v0.0.0(plz work)")

url = input("Enter the URL: ")

mouse_actions = ["left", "right", "middle", "double", "triple", "scrollup", "scrolldown"]
keyboard_actions = ['accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

while True:
    action = input("ReverseKeylogger> ").split(" ")
    if action[0] == "help":
        if len(action) == 1:
            print("Commands:")
            print("  [H]elp - Displays this message")
            print("  ma - Mouse actions")
            print("  mm - Mouse movement")
            print("  ka - Keyboard actions")
            print("  kr - Keyboard repeat")
            print("  ks - Keyboard shortcut")
            print("  kt - Keyboard type")
            print("  [Q]uit - Exit the program")
        elif len(action) == 2:
            if action[1] == "ma":
                print("Mouse actions:")
                print("  left - Left click")
                print("  right - Right click")
                print("  middle - Middle click")
                print("  double - Double click")
                print("  triple - Triple click")
                print("  scrollup - Scroll up")
                print("  scrolldown - Scroll down")
            elif action[1] == "mm":
                print("Mouse movement:")
                print("  <x> <y> - Move the mouse to the coordinates")
            elif action[1] == "ka":
                print("Keyboard actions:")
                print("  <key> - Press the key")
                print("Keys:")
                for key in keyboard_actions:
                    print("  " + key)
            elif action[1] == "kr":
                print("Keyboard repeat:")
                print("  <key> <count> - Press the key the specified number of times")
            elif action[1] == "ks":
                print("Keyboard shortcut:")
                print("  <key>+<key>+... - Press the keys at the same time")
            elif action[1] == "kt":
                print("Keyboard type:")
                print("  <text> - Type the given text")
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    elif action[0] == "ma":
        if len(action) == 2:
            if action[1] in mouse_actions:
                requests.get(url + "/mouse/" + action[1])
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    elif action[0] == "mm":
        if len(action) == 3:
            requests.get(url + "/mouse/move/" + action[1] + "/" + action[2])
        else:
            print("Invalid command")
    elif action[0] == "ka":
        if len(action) == 2:
            if action[1] in keyboard_actions:
                requests.get(url + "/keyboard/" + action[1])
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    elif action[0] == "kr":
        if len(action) == 3:
            if action[1] in keyboard_actions and action[2].isdigit():
                requests.get(url + "/keyboard/repeat/" + action[1] + "/" + action[2])
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    elif action[0] == "ks":
        if len(action) == 2:
            requests.get(url + "/keyboard/shortcut/" + action[1])
        else:
            print("Invalid command")
    elif action[0] == "kt":
        if len(action) == 2:
            requests.get(url + '/keyboard/type/"' + action[1] + '"')
        else:
            print("Invalid command")
    elif action[0] == "q":
        break
    else:
        print("Invalid command")
        
           
