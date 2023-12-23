import pyautogui
import time

pesquisa = input("digite o que voce quer pesquisa: ")

pyautogui.press("win")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("google")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(f"{pesquisa}")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)

