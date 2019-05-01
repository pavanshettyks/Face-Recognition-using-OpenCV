import cv2
import numpy as np
import os

video_frames = cv2.VideoCapture(0)

while True:
    #capture frame by frame
    retval, frame = video_frames.read()

    cv2.imshow('Face Detection', frame)
    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
       video_capture.release()
       cv2.destroyAllWindows()
