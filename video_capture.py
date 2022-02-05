import cv2
import numpy as np
import os
import datetime

date = datetime.datetime.now().strftime('%y%m%d')
dir_name = date + str('-image')

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) 
i = 0

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    cv2.imwrite(dir_name + str(i).zfill(5) + '.jpg', frame)
    i = i + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

