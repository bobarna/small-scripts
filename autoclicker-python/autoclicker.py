import pyautogui
from pynput.keyboard import *
import numpy as np

#  ======== settings ========
delay = 0.02  # in seconds
jitter = 0.0

resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())

            curr_delay = np.random.uniform(
                delay-jitter,
                delay+jitter
            )
            print("Current delay " + str(curr_delay))
            pyautogui.PAUSE = curr_delay
    lis.stop()


if __name__ == "__main__":
    main()
