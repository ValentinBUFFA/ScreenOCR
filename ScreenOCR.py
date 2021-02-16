import pytesseract
import pyautogui
import clipboard
import keyboard
from PIL import Image

while (True):
    keyboard.wait('²')
    ox, oy = pyautogui.position()
    keyboard.wait('²')

    x, y = pyautogui.position()
    scr = pyautogui.screenshot()
    scr = scr.crop((min(ox, x), min(oy, y), max(x, ox), max(y, oy)))
    text = pytesseract.image_to_string(scr)
    print(text, "\n")
    clipboard.copy(text)
