import pyautogui

from actions import beep, check_battle, check_poke_position, click_fish, close_game, get_loot, poke_atack, print_screen, send_msg, turn_off, use_fishing_rod, use_pokeball
from send import load_img, send_watsapp_msg 

X_FISH = 138
Y_FISH = 42
RGB_FISH = (66, 164, 50)

MAX_ATTEMPT = 800
attempt = 0

while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    attempt = attempt + 1
    print(attempt)
    if fish:
        click_fish(X_FISH, Y_FISH)
        pyautogui.sleep(1.5)
        poke_atack()
        pyautogui.sleep(2)
        get_loot()
        use_pokeball()
        check_poke_position()
        pyautogui.sleep(4)
        if not check_battle():
            poke_atack()
            if not check_battle():
                send_msg()
                beep()
                file_name = print_screen()
                url = load_img(file_name)
                send_watsapp_msg(url)
                close_game()
                # turn_off()
                break
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0
        