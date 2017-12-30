# -*- coding: utf8 -*-
import cv2
import numpy as np
	
img = cv2.imread('0.png')
res=cv2.resize(img,(360,640),interpolation=cv2.INTER_CUBIC)
bg = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

img = cv2.imread('092117.png')
res=cv2.resize(img,(360,640),interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0)
canny = cv2.Canny(gray, 30, 150)
canny = np.uint8(np.absolute(canny))
cv2.imshow("Canny", canny)

frameDelta = cv2.absdiff(bg, gray)
thresh = cv2.threshold(frameDelta, 15, 255, cv2.THRESH_BINARY)[1]

thresh = cv2.dilate(thresh, None, iterations=1)
_, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
	if cv2.contourArea(c) < 360:
		continue
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(res, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
(x, y, w, h) = cv2.boundingRect(cnts[-5])
cv2.rectangle(res, (x, y), (x + w, y + h), (255, 0, 0), 2)	
	
cv2.imshow("img", res)
cv2.imshow("Thresh", thresh)
cv2.imshow("Frame Delta", frameDelta)  
cv2.waitKey(0)  