import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

dir_frames = 'things'
filenames = []
filesinfo = os.scandir(dir_frames)
filenames = [f.path for f in filesinfo if f.name.endswith(".jpg")]
filenames.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
frameCount = len(filenames)
frameHeight, frameWidth, frameChannels = cv2.imread(filenames[0]).shape
frames2 = np.zeros((frameCount, frameHeight, frameWidth),dtype=np.uint8)
blank=np.zeros((frameHeight,frameWidth))
for idx, file_i in enumerate(filenames):
    t = cv2.imread(file_i)
    frames2[idx] = cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
frameChange=np.full((frameCount, frameHeight, frameWidth),False)
currentframe=np.greater(blank,1)
for i in range(frameCount):
    nextframe=np.greater(frames2[i],128)
    frameChange[i]=np.logical_xor(currentframe,nextframe)
    currentframe=nextframe
for i in range(frameCount):
    cv2.imwrite('thing2/f'+str(i)+'.jpg',frameChange[i]*255)
    


