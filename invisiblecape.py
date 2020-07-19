import cv2
import numpy as np
import time


fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0, (640,480))

video_capture = cv2.VideoCapture(0)

time.sleep(4)  
count = 0 
background = 0 

for i in range(60):
	retrn,background = video_capture.read()
	if retrn == False:
		continue


background = np.flip(background, axis = 1)


while(video_capture.isOpened()):
	retrn , image = video_capture.read()
	if not retrn:
		break
	count+=1
	image = np.flip(image, axis =1)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	

	lower_green = np.array([40,158,16])
	upper_green = np.array([250,180,110])
	mask1 = cv2.inRange(hsv , lower_green , upper_green)
	
	lower_green = np.array([98,110,25])
	upper_green = np.array([112,255,255])
	mask2 = cv2.inRange(hsv , lower_green , upper_green)

	mask1= mask1 + mask2

	mask1= cv2.morphologyEx(mask1, cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8)) 
	mask2 = cv2.bitwise_not(mask1)
	
	res1 = cv2.bitwise_and(background,background,mask=mask1)
	res2 = cv2.bitwise_and(image , image , mask = mask2)
	
	finalOutput = cv2.addWeighted(res1,1,res2,1,0)
	out.write(finalOutput)
	cv2.imshow("BABA INVISIBLE",finalOutput)
	cv2.waitKey(12)
	
video_capture.release()
out.release()
cv2.destroyAllWindows()


  


