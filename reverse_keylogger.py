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
    action = input("Enter the action ([M]ouse/[K]eyboard) or [Q]uit: ").lower()

    if action == 'q':
        break

    if action == 'm':
        action = input("Enter the action ([A]ction/[M]ovement): ").lower()
        if action == 'a':
            print("Mouse actions: " + str(mouse_actions))
            action = input("Enter the action: ").lower()
            if action in mouse_actions:
                response = requests.get(url + "/mouse/" + action)
                print(response.text)
            else:
                print("Invalid action")
        elif action == 'm':
            (x, y) = (coord.strip() for coord in input("Enter the coordinates (x,y): ").split(","))
            if x.isdigit() and y.isdigit():
                response = requests.get(url + "/mouse/move/" + x.strip() + "/" + y.strip())
                print(response.text)
            else:
                print("Invalid coordinates")

    elif action == 'k':
        action = input("Enter the action ([A]ction/[T]yping/[H]otkey): ").lower()
        if action == 'a':
            print("Keyboard actions: " + str(keyboard_actions))
            action = input("Enter the action: ").lower()
            if action in keyboard_actions:
                count = input("Enter the count (default 1): ")
                if count.isdigit():
                    response = requests.get(url + "/keyboard/repeat/" + action + "/" + count)
                    print(response.text)
                else:
                    response = requests.get(url + "/keyboard/" + action)
                    print(response.text)
            else:
                print("Invalid action")
        elif action == 't':
            word = input("Enter the string to type: ")
            response = requests.get(url + '/keyboard/type/"' + word + '"')
            print(response.text)
        elif action == 'h':
            shortcut = input("Enter the shortcut (separate with +): ")
            response = requests.get(url + "/keyboard/shortcut/" + shortcut)
            print(response.text)
        else:
            print("Invalid action")
