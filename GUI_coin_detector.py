#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog


# In[2]:


def coin_detection(path): 
    
    # a=4.5
    a = slider1.get()
    
    # b=3;
    b = slider2.get()
    
    img_main = cv2.imread(path,1) 
    
    cimg = img_main.copy() 
    
    img_hsv = cv2.cvtColor(cimg,cv2.COLOR_BGR2HSV)
    
    _,_,img = cv2.split(img_hsv)
    
    #img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY);
    
    r,c=img.shape[0],img.shape[1]

    blur = cv2.GaussianBlur(img,(9,9),0)

    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20, param1=80,param2=30,minRadius=int(r/a),maxRadius=int(r/b))

    Sq_Circles=np.squeeze(circles)

    Center=Sq_Circles[:,:2]

    N=np.arange(len(circles[0]))
    for i in range(len(Center)):
        if N[i]==i:
            N[np.where((np.sqrt(np.sum((Center-Center[i])**2,axis=1)))<=int(r/a)*0.70)[0]]=i  
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
    except:
        pass
    return img_main,cimg


# In[26]:


def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    path = filedialog.askopenfilename()
    if len(path) > 0:
    # # load the image from disk, convert it to grayscale, and detect
    # # edges in it
        image,detector=coin_detection(path)
        W,H,_=image.shape
        print(W,H)
        image = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGB),(400,int(400*(W/H))))
        detector = cv2.resize(cv2.cvtColor(detector, cv2.COLOR_BGR2RGB),(400,int(400*(W/H))))
        # convert the images to PIL format...
        image = Image.fromarray(image)
        detector = Image.fromarray(detector)
        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        detector = ImageTk.PhotoImage(detector)
        if panelA is None or panelB is None:
        # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10,expand=True)
            # while the second panel will store the edge map
            panelB = Label(image=detector)
            panelB.image = detector
            panelB.pack(side="right", padx=10, pady=10,expand=True)
        # otherwise, update the image panels
        else:
        # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=detector)
            panelA.image = image
            panelB.imaroot = Tk()


# In[27]:


root = Tk()

panelA = None
panelB = None


# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI

label1 = Label(root, text = "a", font=("Arial", 10, "bold"), width=20)
label1.pack(padx="10", pady="10")
slider1 = Scale(root,from_=1, to=25, resolution=0.5, orient=HORIZONTAL)
slider1.pack(padx="10", pady="10")

label2 = Label(root, text = "b", font=("Arial", 10, "bold"), width=20)
label2.pack(padx="10", pady="10")
slider2 = Scale(root, from_=1, to=15, resolution=0.1, orient=HORIZONTAL)
slider2.pack(padx="10", pady="10")

btn = Button(root, text="Select an image", command=select_image)

btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()    


# In[ ]:




