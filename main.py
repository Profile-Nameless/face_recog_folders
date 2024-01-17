import os
import cv2
Facecascade = cv2.CascadeClassifier('face.xml')
root = "D:\python\pycharm\pythonProject3\images face recognition\\"
listoffolders=os.listdir("D:\python\pycharm\pythonProject3\images face recognition")
for folders in listoffolders:
    path = root+folders
    imagepath=""
    for photo in os.listdir(path):
        # print(folders,photo)
        imagepath = path+"\\"+photo
        image = cv2.imread(imagepath)
        if image.any():
             #Coordinates
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = Facecascade.detectMultiScale(grayImage, scaleFactor=1.1, minSize=(30, 30))
            # to get coordinates print(faces)
            if len(faces)>=1:
                  #rectangle
                  x,y,w,h =  faces
                  num = len(faces)
                  cv2.putText(image,f'Number of faces detected: {num}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                  cv2.imwrite("NewImage.jpg",image)
            else:
               print("No face detected")
