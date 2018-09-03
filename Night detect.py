import cv2

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)
 
cam = cv2.VideoCapture(0)
 
winName = "Night Motion Detector"
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
 

t1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
 
while True:
  cv2.imshow( winName, diffImg(t1, t, t2) )
 
  
  t1 = t
  t = t2
  t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
 
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break
 

