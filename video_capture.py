import cv2
import numpy as np
import os
import datetime

date = datetime.datetime.now().strftime('%y%m%d-%H%M')
dir_name = date + str('-image')
os.mkdir(dir_name)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) 
i = 0
j = 0

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    i += 1
    if i % 10 == 0:
        cv2.imwrite(os.path.join(dir_name, str(j).zfill(5) + '.jpg'), frame)
        j += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

