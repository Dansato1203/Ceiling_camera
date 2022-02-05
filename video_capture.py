import cv2
import numpy as np
import param
import os
import date

date = datetime.datetime.now().strftime('%y%m%d')
dir_name = date + str('-image')

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) 
i = 0

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    cv2.imwrite(dir_name + i.zfill(5) + '.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

