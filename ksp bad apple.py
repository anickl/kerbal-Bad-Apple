import krpc
import numpy as np
import cv2
import os
import pyautogui
import win32gui
from PIL import Image
#screenshot for the video, not entirely necessary but i didnt want a 9 hour video
def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im


#connect and control active vessel

conn = krpc.connect()
vessel = conn.space_center.active_vessel
#get a list of all engines
engines=vessel.parts.engines
#initialize the engine array
#CHANGE NUMBERS TO THE ARRAY OF ENGINES
engarray=[[0 for j in range(26)] for i in range(26)]
#build the engine array
for e in engines:
    name=e.part.tag.split(',')
    engarray[int(name[1])][int(name[0])]=e
    #turn off all engines, useful if program stopped 
    e.active=False
print('engines loaded')
#load video into memory
dir_frames = 'thing2'
filenames = []
filesinfo = os.scandir(dir_frames)
filenames = [f.path for f in filesinfo if f.name.endswith(".jpg")]
filenames.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
frameCount = len(filenames)
frameHeight, frameWidth, frameChannels = cv2.imread(filenames[0]).shape
frames2 = np.zeros((frameCount, frameHeight, frameWidth),dtype=np.uint8)
for idx, file_i in enumerate(filenames):
    t = cv2.imread(file_i)
    frames2[idx] = cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
#assume all off initially. white pixels denote a change
print('video loaded')
currentStates=np.full((frameHeight, frameWidth),False)
for i in range(frameCount):
    now=np.greater(frames2[i],128)
    #get index of where changes need to occur
    change=np.argwhere(now==True)
    for j in change:
        #swappable if required
        x=25-j[0]
        y=j[1]
        if(currentStates[x][y]):
            engarray[x][y].active=False
            currentStates[x][y]=False
        else:
            engarray[x][y].active=True
            currentStates[x][y]=True
    #save data
    im = screenshot('Kerbal Space Program')
    im.save("1fin "+str(i)+".jpg")
    print("frame: " + str(i) + " finished")


