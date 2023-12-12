import requests
import cmd
import os
class ReverseKeylogger(cmd.Cmd):
    intro = "Reverse Keylogger v0.0.0 (plz work)"
    prompt = "ReverseKeylogger> "

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

    def do_help(self, arg):
        if not arg:
            print("Commands:")
            print("  help - Displays this message")
            print("  ma - Mouse actions")
            print("  mm - Mouse movement")
            print("  ka - Keyboard actions")
            print("  kr - Keyboard repeat")
            print("  ks - Keyboard shortcut")
            print("  kt - Keyboard type")
            print("  clear - Clear the screen")
            print("  quit - Exit the program")
        elif arg == "ma":
            print("Mouse actions:")
            print("  left - Left click")
            print("  right - Right click")
            print("  middle - Middle click")
            print("  double - Double click")
            print("  triple - Triple click")
            print("  scrollup - Scroll up")
            print("  scrolldown - Scroll down")
        elif arg == "mm":
            print("Mouse movement:")
            print("  <x> <y> - Move the mouse to the coordinates")
        elif arg == "ka":
            print("Keyboard actions:")
            print("  <key> - Press the key")
            print("Keys:")
            for key in self.keyboard_actions:
                print("  " + key)
        elif arg == "kr":
            print("Keyboard repeat:")
            print("  <key> <count> - Press the key the specified number of times")
        elif arg == "ks":
            print("Keyboard shortcut:")
            print("  <key>+<key>+... - Press the keys at the same time")
        elif arg == "kt":
            print("Keyboard type:")
            print("  <text> - Type the given text")
        else:
            print("Invalid command")

    def do_ma(self, arg):
        if arg in self.mouse_actions:
            requests.get(url + "/mouse/" + arg)
        else:
            print("Invalid command")

    def do_mm(self, arg):
        args = arg.split(" ")
        if len(args) == 2:
            requests.get(url + "/mouse/move/" + args[0] + "/" + args[1])
        else:
            print("Invalid command")

    def do_ka(self, arg):
        if arg in self.keyboard_actions:
            requests.get(url + "/keyboard/" + arg)
        else:
            print("Invalid command")

    def do_kr(self, arg):
        args = arg.split(" ")
        if len(args) == 2:
            if args[0] in self.keyboard_actions and args[1].isdigit():
                requests.get(url + "/keyboard/repeat/" + args[0] + "/" + args[1])
            else:
                print("Invalid command")
        else:
            print("Invalid command")

    def do_ks(self, arg):
        if arg:
            requests.get(url + "/keyboard/shortcut/" + arg)
        else:
            print("Invalid command")

    def do_kt(self, arg):
        if arg:
            requests.get(url + '/keyboard/type/' + arg)
        else:
            print("Invalid command")

    def do_clear(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_quit(self, arg):
        return True
    
    def do_q(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
if __name__ == '__main__':
    url = input("Enter the URL: ")
    ReverseKeylogger().cmdloop()
