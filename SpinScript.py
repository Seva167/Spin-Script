import win32api, win32con, keyboard, time, math, random

print('Press Q to quit')
rottype = input('Select rotation type (available types: rot, sin, tan, sinabs, rand): ')

delay = (float)(input('Enter starting delay: '))

pause = False

if not rottype == 'rand':
    multiplier = (float)(input('Set speed: '))
    print(f'You have {delay} seconds to alt-tab... Wheeee!')
    time.sleep(delay)

if rottype == 'rot':
    while not keyboard.is_pressed('q'):
        if not pause:
            mouseX = (int)(time.time()*0.000000001* multiplier)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
            time.sleep(0.01)
        if keyboard.is_pressed('p'):
            time.sleep(0.1)
            pause = not pause
elif rottype == 'sin':
    while not keyboard.is_pressed('q'):
        if not pause:
            mouseX = (int)(math.sin(time.time())* multiplier)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
            time.sleep(0.01)
        if keyboard.is_pressed('p'):
            time.sleep(0.1)
            pause = not pause
elif rottype == 'tan':
    while not keyboard.is_pressed('q'):
        if not pause:
            mouseX = (int)(math.tan(time.time())* multiplier)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
            time.sleep(0.01)
        if keyboard.is_pressed('p'):
            time.sleep(0.1)
            pause = not pause
elif rottype == 'sinabs':
    while not keyboard.is_pressed('q'):
        if not pause:
            mouseX = (int)(math.fabs(math.sin(time.time())* multiplier))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
            time.sleep(0.01)
        if keyboard.is_pressed('p'):
            time.sleep(0.1)
            pause = not pause
elif rottype == 'rand':
    maxval = (int)(input('Enter maximum possible random value: '))
    randdelay = (float)(input('Enter delay between values: '))
    print(f'You have {delay} second to alt-tab... Wheeee!')
    time.sleep(delay)
    while not keyboard.is_pressed('q'):
        if not pause:
            mouseX = (int)(random.randint(0,maxval))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouseX, 0, 0, 0)
            time.sleep(randdelay)
        if keyboard.is_pressed('p'):
            time.sleep(0.1)
            pause = not pause
