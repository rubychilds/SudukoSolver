# http://stackoverflow.com/questions/10196198/how-to-remove-convexity-defects-in-sudoku-square/11366549#11366549

import numpy as np
import cv2

class Grid:

	def __init__(self, im):
				
		image = cv2.imread(im)
		preprocessed = preprocessing(image)
		removed = areaRemoval(preprocessed)
		horImage, verImage = lines(removed)
		grid = findGrid(horImage, verImage)
		b, bm = Correction(grid, image)
		output = createBoard(b, bm)
		output.save("board.JPEG" )

	def preprocessing(self, im):

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

		return res2

	def areaRemoval(self, image):

		thresh = cv2.adaptiveThreshold(res,255,0,1,19,2)

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


	def  lines(self, res):
		
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

		ret,closex = cv2.threshold(dx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		ret,closey = cv2.threshold(dy,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


		closex = cv2.morphologyEx(closex,cv2.MORPH_DILATE,kernelx,iterations = 1)
		closey = cv2.morphologyEx(closey,cv2.MORPH_DILATE,kernely,iterations = 1)

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
			    if w/h > 5:
			        cv2.drawContours(close,[cnt],0,255,-1)
			    else:
			        cv2.drawContours(close,[cnt],0,0,-1)
		
		closey = cv2.morphologyEx(closey,cv2.MORPH_CLOSE,None,iterations = 2)

		return closex, closey

	def findGrid(self, horImage, verImage):
		return cv2.bitwise_and(horImage, verImage)

	def correction(self, grid, img):

		contour, hier = cv2.findContours(grid,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		centroids = []
		for cnt in contour:
			mom = cv2.moments(cnt)
			(x,y) = int(mom['m10']/mom['m00']), int(mom['m01']/mom['m00'])
			cv2.circle(img,(x,y),4,(0,255,0),-1),centroids.append((x,y))

		centroids = np.array(centroids,dtype = np.float32)
		c = centroids.reshape((100,2))
		c2 = c[np.argsort(c[:,1])]

		b = np.vstack([c2[i*10:(i+1)*10][np.argsort(c2[i*10:(i+1)*10,0])] for i in xrange(10)])
		bm = b.reshape((10,10,2))

		return b, bm

	def createBoard(self, btemp, bmtemp):

		output = np.zeros((450,450,3),np.uint8)
		for i,j in enumerate(btemp):
			ri = i/10
			ci = i%10
			if ci != 9 and ri!=9:
				src = bmtemp[ri:ri+2, ci:ci+2 , :].reshape((4,2))
				dst = np.array( [ [ci*50,ri*50],[(ci+1)*50-1,ri*50],[ci*50,(ri+1)*50-1],[(ci+1)*50-1,(ri+1)*50-1] ], np.float32)
				retval = cv2.getPerspectiveTransform(src,dst)
				warp = cv2.warpPerspective(res2,retval,(450,450))
				output[ri*50:(ri+1)*50-1 , ci*50:(ci+1)*50-1] = warp[ri*50:(ri+1)*50-1 , ci*50:(ci+1)*50-1].copy()

		return output