import pyautogui
import random
import winsound
import os
from datetime import datetime

X_BELLOSOM = 888
Y_BELLOSOM = 597
RGB_BELLOSOM = (130, 3, 0)

USE_POKEBALL = True

POKE_DEAD_POSITION = (878, 534) 
BP_LOOT_POSITION = (1747, 1002)

LIST_ATACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
LIST_OCEAN_POSITION = [(1254, 487), (1243, 631), (1104, 637), (1043, 726)]

BATTLE_REGION = (1727, 579, 166, 96)

LIST_MSG = ['sua net esta boa?', 'nossa, minha internet esta horrivel', 'aew', '????', 'opa', 'eaee', 'que saco da minha internet', 'ta caindo sua internet?']

def check_battle():
    battle = pyautogui.locateOnScreen('battle.PNG', confidence=0.8, region=BATTLE_REGION)
    if battle is not None:
        return True
    return False

def send_msg():
    msg = random.choice(LIST_MSG)
    pyautogui.write(msg)
    pyautogui.press('enter')

def beep():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

def print_screen():
    now = datetime.now().strftime('%d-%m-%Y-%H-%M')
    file_name = now + '.png'
    pyautogui.screenshot(file_name)
    return file_name

def click_fish(x_fish, y_fish):
    pyautogui.moveTo(x_fish, y_fish)
    pyautogui.click()

def poke_atack():
    pyautogui.press(LIST_ATACK)

def get_loot():
    pyautogui.moveTo(POKE_DEAD_POSITION)
    pyautogui.click(button='right')
    pyautogui.sleep(0.8)
    pyautogui.moveTo(BP_LOOT_POSITION)
    pyautogui.click(clicks=5)

def use_pokeball():
    if USE_POKEBALL:
        pyautogui.moveTo(POKE_DEAD_POSITION)
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click()


def check_poke_position():
    poke = pyautogui.pixelMatchesColor(X_BELLOSOM, Y_BELLOSOM, RGB_BELLOSOM)
    if not poke:
        pyautogui.press('f11')
        pyautogui.sleep(0.8)
        pyautogui.moveTo(X_BELLOSOM, Y_BELLOSOM)
        pyautogui.click()

def use_fishing_rod():
    ocean_position = random.choice(LIST_OCEAN_POSITION)
    pyautogui.press('delete')
    pyautogui.moveTo(ocean_position)
    pyautogui.click()

def close_game():
    pyautogui.moveTo(1892, 8)
    pyautogui.click()
    pyautogui.moveTo(832, 577)
    pyautogui.click()

def turn_off():
    os.system('shutdown /s /t 1')