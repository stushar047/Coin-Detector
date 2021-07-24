#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np

#Parameter
a=20;

b=10;


#Read Image
cimg = cv2.imread('input.jpg',1)
cimg_1=cimg.copy()

img_hsv = cv2.cvtColor(cimg,cv2.COLOR_BGR2HSV)


_,_,img = cv2.split(img_hsv)

r,c=img.shape[0],img.shape[1]

blur = cv2.GaussianBlur(img,(9,9),0)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20, param1=80,param2=30,minRadius=int(r/a),maxRadius=int(r/b))

try:

    Sq_Circles=np.squeeze(circles)
    Center=Sq_Circles[:,:2]
    try:
        for i in Sq_Circles.astype(np.int16):
            cv2.circle(cimg_1,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(cimg_1,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('detected circles',cimg_1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    except:
        pass

    N=np.arange(len(circles[0]))
    for i in range(len(Center)):
        if N[i]==i:
            N[np.where((np.sqrt(np.sum((Center-Center[i])**2,axis=1)))<=int(r/a)*0.7)[0]]=i  
        else:
            pass

    Val=[];
    NU=np.unique(N);
    for i in NU:  
        Val.append(np.where(N==i)[0])
    New=np.zeros((len(Val),3),np.uint16)
    for j in range(len(Val)):
        try:
            for k in range(len(Val[j])):
                New[j,:]+=Sq_Circles[Val[j][k]]
        except:
            New[j,:]=Sq_Circles[Val[j][0]]

    try:
        cv2.putText(cimg, "The Number of coints:"+str(len(New)), (30,20), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0,100,255), 2, cv2.LINE_AA)
        for i in New:
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),4)
            #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            cv2.putText(cimg, str(i[2]*2), (i[0]-i[2]//2,i[1]), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0,100,255), 2, cv2.LINE_AA)

        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    except:
        pass
except:
    print("Choose correct a and b value")


# In[ ]:




