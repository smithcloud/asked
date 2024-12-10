import pyautogui
import time

def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def main():
    try:
        while True:
            pyautogui.hotkey('f5')
            time.sleep(10)
            for x in range(4):

                time.sleep(2)

                move_and_click(1234, 335)
                time.sleep(2)

                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)

                move_and_click(1246, 477)
                time.sleep(2)

                move_and_click(853, 759)
                time.sleep(1)
        

    except KeyboardInterrupt:
        print("프로그램이 사용자에 의해 중단되었습니다.")

if __name__ == "__main__":
    main()
