import win32api, win32con, keyboard, time, math, random

print('Press Q to quit')
rottype = input('Select rotation type (available types: rot, sin, tan, sinabs, rand): ')
delay = (float)(input('Enter starting delay: '))

if not rottype == 'rand':
    multiplier = (float)(input('Set speed: '))
    print(f'You have {delay} seconds to alt-tab... Wheeee!')
    time.sleep(delay)

if rottype == 'rot':
    while not keyboard.is_pressed('q'):
        mouseX = (int)(time.time()*0.000000001* multiplier)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
        time.sleep(0.01)
elif rottype == 'sin':
    while not keyboard.is_pressed('q'):
        mouseX = (int)(math.sin(time.time())* multiplier)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
        time.sleep(0.01)
elif rottype == 'tan':
    while not keyboard.is_pressed('q'):
        mouseX = (int)(math.tan(time.time())* multiplier)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
        time.sleep(0.01)
elif rottype == 'sinabs':
    while not keyboard.is_pressed('q'):
        mouseX = (int)(math.fabs(math.sin(time.time())* multiplier))
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
        time.sleep(0.01)
elif rottype == 'rand':
    maxval = (int)(input('Enter maximum possible random value: '))
    print(f'You have {delay} seconds to alt-tab... Wheeee!')
    time.sleep(delay)
    while not keyboard.is_pressed('q'):
        mouseX = (int)(random.randint(0,maxval))
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
        time.sleep(0.1)
