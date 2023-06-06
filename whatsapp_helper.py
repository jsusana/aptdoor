import pywhatkit
import time
import pyautogui
import keyboard as k


def SendAlertMessage(phone, message):
    pywhatkit.sendwhatmsg_instantly(phone, message)
    pyautogui.click(1050, 950)
    time.sleep(2)
    k.press_and_release('enter')

def SendAlertImage(phone, path):
    pywhatkit.sendwhats_image(phone, path, 'attachment')
    pyautogui.click(1050, 950)
    time.sleep(2)
    k.press_and_release('enter')
