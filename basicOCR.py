# http://stackoverflow.com/questions/10196198/how-to-remove-convexity-defects-in-sudoku-square/11366549#11366549

import numpy as np
import cv2

class Grid:

	def __init__(im):
				
		im = cv2.imread( )
		
		preprocessed = preprocessing(image)
		removed = areaRemoval(preprocessed)
		linedImage = lines(removed)

	def preprocessing(im):

		image = im.copy()
		# translates image to Gray scale
		gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
			# applies gaussian blur
		blur = cv2.GaussianBlur(gray,(5,5),0)
		# gets threshold
		thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

		kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

		close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel1)
		div = np.float32(gray)/(close)

		res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))
		res2 = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)

		return image

	def areaRemoval(image):

		contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		samples =  np.empty((0,100))
		responses = []

		keys = [i for i in range(48,58)]

		area = 0

		for cnt in contours:
			# finds larget areas
			area = cv2.contourArea(cnt)
		    if area > 1000:
		    	if area > max_area:
		    		max_area = area
		    		max_cont = cnt


		cv2.drawContours(mask, [max_count], 0,255,-1)
		cv2.drawContours(mask, [max_count], 0,0,2)
		
		return cv2.bitwise_and(res,mask)


	def  lines():
		
		# KERNELS
		kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(2,10))
		kernely = cv2.getStructuringElement(cv2.MORPH_RECT,(10,2))

		# vertical
		dx = cv2.Sobel(res,cv2.CV_16S,1,0)
		dx = cv2.convertScaleAbs(dx)
		# horizontal
		dy = cv2.Sobel(res,cv2.CV_16S,0,2)
		dy = cv2.convertScaleAbs(dy)

		cv2.normalize(dx,dx,0,255,cv2.NORM_MINMAX)
		cv2.normalize(dy,dy,0,255,cv2.NORM_MINMAX)

		ret,close = cv2.threshold(dx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

		closex = cv2.morphologyEx(close,cv2.MORPH_DILATE,kernelx,iterations = 1)
		closey = cv2.morphologyEx(close,cv2.MORPH_DILATE,kernely,iterations = 1)

		contourx, hierx = cv2.findContours(closex,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		contoury, hiery = cv2.findContours(closey,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		
		for cnt in contourx:
		    x,y,w,h = cv2.boundingRect(cnt)
		    if h/w > 5:
		        cv2.drawContours(closex,[cnt],0,255,-1)
		    else:
		        cv2.drawContours(closex,[cnt],0,0,-1)
		
		closex = cv2.morphologyEx(closex,cv2.MORPH_CLOSE,None,iterations = 2)
	
		for cnt in contoury:
			    x,y,w,h = cv2.boundingRect(cnt)
			    if w/h >5:
			        cv2.drawContours(close,[cnt],0,255,-1)
			    else:
			        cv2.drawContours(close,[cnt],0,0,-1)
		
		closey = cv2.morphologyEx(close,cv2.MORPH_CLOSE,None,iterations = 2)

		return closex, closey

	def findGrid(horImage, verImage):
		return cv2.bitwise_and(horImage, verImage)





