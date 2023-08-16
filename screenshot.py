"""
region finding 3.(960,400,300,500) 2.(960,200,300,710)
red colour composition RGB: (220,  78,  55)
green colour composition RGB: ( 73, 183,  90)
if pyautogui.pixel(1134,range(200,710)[0]==73) and pyautogui.pixel(1134,range(200,710)[1]==183) and pyautogui.pixel(1134,range(200,710)[2]==90):
mouse moving:
win32api.SetCursorPos((1500,700)
sell:
click(1828,821)
buy:
click(1828,668)
single candle region=(1030,200,130,710)

or pyautogui.locateOnScreen(,region=(900,150,280,700),grayscale=True,confidence=0.6)!=None):



import pyautogui
import time
import keyboard
import win32api, win32con

while not keyboard.is_pressed('q'):
    if pyautogui.locateOnScreen('main1.png', region=(970, 150, 280, 700), grayscale=True, confidence=0.8) is not None:
        if pyautogui.locateOnScreen(['upperwikgnext.png', 'upperwiknext.png', 'uppergwik.png', 'red3.png'], region=(900, 150, 280, 700), grayscale=True, confidence=0.65) is not None:
            click0 = 0
        else:
            click0 = 1
        if pyautogui.locateOnScreen(['sell.png', 'redcot.png'], region=(870, 150, 350, 700), grayscale=True, confidence=0.7) is not None:
            click1 = 0
        else:
            click1 = 1
        if pyautogui.locateOnScreen('red2.png', region=(900, 150, 280, 700), grayscale=True, confidence=0.65) is not None:
            click2 = 0
        else:
            click2 = 1
        if click0 == 0 or click1 == 0 or click2 == 0:
            win32api.SetCursorPos((1828,800))
        else:
            win32api.SetCursorPos((1828,630))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(5)
                
"""
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
        if(pyautogui.locateOnScreen('img.png',region=(1800,500,100,150),grayscale=True,confidence=0.99)!=None):
                click(1828,610)
        if pyautogui.locateOnScreen('main1.png' ,region=(1000,400,300,350),grayscale=True,confidence=0.6)!=None:
                if (pyautogui.locateOnScreen('upperwikgnext.png' or 'upperwiknext.png' or 'uppergwik.png' or 'red3.png',region=(900,150,280,700),grayscale=True,confidence=0.4)!=None):
                        click0=0
                else:
                        click0=1
                if (pyautogui.locateOnScreen('sell.png' or 'redcot.png',region=(870,150,350,700),grayscale=True,confidence=0.5)!=None):
                        click1=0
                else:
                        click1=1
                if (pyautogui.locateOnScreen('red2.png',region=(900,150,280,700),grayscale=True,confidence=0.45)!=None):
                        click2=0
                else:
                        click2=1
                if(click0==0 or click1==0 or click2==0):
                        click(1828,800)
                else:
                        click(1828,630)
                time.sleep(7)
