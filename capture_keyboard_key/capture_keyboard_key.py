import os

try:
    from pynput.keyboard import Key, Listener
except:
    os.system("pip install pynput")
    print("Biblioteca instalada - Execute novamente")

x = 1

def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    pass

def on_release(key):
    os.system("cls")
    print("pressione (->),(<-) \nou presssione (ESC) para encerrar a execucao")
    global x
    # print('{0} release'.format(
    #     key))
    if key == Key.right:
        x = x + 1
        if x > 20:
            x = 1
        print(str(x))

    if key == Key.left:
        x = x - 1
        if x < 1:
            x = 20
        print(str(x))


    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
