import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_alt2.xml')

image = cv2.imread('friends.PNG')

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grayImage)

print("Number of faces in the photo: " + str(faces.shape[0]))

for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.rectangle(image, (x,y), (x+w,y+h), (255, 255, 255), 1)

        cv2.putText(image, "Number of faces : " + str(faces.shape[0]), (100,300),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (116, 254, 86), 2)

    
cv2.imshow('Image with faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()