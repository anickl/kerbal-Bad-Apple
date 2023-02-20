import cv2
import os
import ffmpeg
import numpy as np
video_path="schlechtem apfel.mp4"
dir_path="things"
basename="f"
ext='jpg'
'''
cap = cv2.VideoCapture()
cap.open(input_file)
if not cap.isOpened():
    print("Failed to open input video")
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

frame_idx = 0
while frame_idx < frame_count:
    ret, frame = cap.read()
    if not ret:
        print ("Failed to get the frame {}".format(frame_idx))
        continue
    out_name = os.path.join(output_path, 'f{:04d}.jpg'.format(frame_idx+1))
    ret = cv2.imwrite(out_name, frame)
    if not ret:
        print ("Failed to write the frame {}".format(frame_idx))
        continue
    frame_idx += 1
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

'''
cap = cv2.VideoCapture(video_path)


os.makedirs(dir_path, exist_ok=True)
base_path = os.path.join(dir_path, basename)

digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

n = 0

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
        n += 1
    else:
        print(n)
