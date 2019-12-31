import cv2
import numpy as np
import os
import time

def findSmallImage(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(small_image, large_image, method)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc

    trows,tcols = small_image.shape[:2]

    boundingRect = cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    #cv2.imshow("largeim", large_image)
    #cv2.waitKey(0)
    return (MPx, MPy)

def checkIfImageExists(small_image, large_image):
    res = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    print(cv2.minMaxLoc(res))
    threshold = 0.4
    flag = False
    if np.amax(res) > threshold:
        flag = True
        return True
    else:
        return False

print(checkIfImageExists(cv2.imread("./Items/ClubCrackers.png"), cv2.imread("./TestImg.JPG")))