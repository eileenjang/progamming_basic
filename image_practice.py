import cv2
pimg="./data/bus_people.jpg"
img=cv2.imread(pimg)
img2=cv2.imread(pimg,0)
cv2.imshow("Cat color", img)
cv2.imshow("Cat grayscale", img2)

cv2.waitKey()
cv2.destroyWindow()