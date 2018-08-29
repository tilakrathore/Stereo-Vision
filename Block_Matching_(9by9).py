######################                  Stereo Vision                         #######################  
######################     1.1 Disparity estimation using block matching (9*9)     #######################

import cv2                             
import numpy as np


left_img = cv2.imread('C:\Users\SONY\Desktop\sview1.png',0)                        
right_img = cv2.imread('C:\Users\SONY\Desktop\sview5.png',0)
disp1_img = cv2.imread('C:\Users\SONY\Desktop\disp1.png',0)
disp5_img = cv2.imread('C:\Users\SONY\Desktop\disp5.png',0)

pad_img_l = cv2.copyMakeBorder(left_img, 4,4,4,4, cv2.BORDER_CONSTANT, value = 0)         
pad_img_r = cv2.copyMakeBorder(right_img, 4,4,4,4, cv2.BORDER_CONSTANT, value = 0)          
disp1_img = cv2.copyMakeBorder(disp1_img, 4,4,4,4, cv2.BORDER_CONSTANT, value = 0)  
disp5_img = cv2.copyMakeBorder(disp5_img, 4,4,4,4, cv2.BORDER_CONSTANT, value = 0) 

height, width=pad_img_l.shape

array_disp1 = np.zeros((height,width))
array_disp5 = np.zeros((height,width))
array_consist1 = np.zeros((height,width))
array_consist5 = np.zeros((height,width))
consist_1 = []
consist_5 = []
  

for i in range (4,height-4):                                      
    for j in range (4,width-4):
        array_chk = []
        array_l= pad_img_l[i-4:i+5,j-4:j+5]
     
        for k in range(j-75,j):
            if (k<4):
                k=4
            array_r=pad_img_r[i-4:i+5,k-4:k+5]
            array_sub = np.subtract(array_l,array_r)               
            array_sqre = np.square(array_sub)
            add = np.sum(array_sqre)
            array_chk.append([add,k])
        minimum = min(array_chk)
        a = minimum
        index = a[1]
        disp = j-index
        array_disp1[i][j] = disp        


array_image1 = array_disp1/array_disp1.max()  
cv2.imshow('disp_image1',array_image1)             ##########     Disparity map of view 1 ############

error1 = disp1_img - array_disp1
error_sq1 = (error1)**2           
mse1 = np.mean(error_sq1)

print 'mse1',mse1                                   ##########    MSE for disparity map of view 1 ############



'''for i in range (4,height-4):                                      
    for j in range (4,width-4):
        array_chk = []
        array_r= pad_img_r[i-4:i+5,j-4:j+5]
        b = width-5
        for k in range(j,j+76):
            if (k>b):
                k=b
            array_l=pad_img_l[i-4:i+5,k-4:k+5]
            array_sub = np.subtract(array_l,array_r)               
            array_sqre = np.square(array_sub)
            add = np.sum(array_sqre)
            array_chk.append([add,k])
        minimum = min(array_chk)
        a = minimum
        index = a[1]
        disp = j-index
        disp = abs(disp)
        array_disp5[i][j] = disp        


array_image5 = array_disp5/array_disp5.max()  
cv2.imshow('disp_image5',array_image5)                 ##########    Disparity map of view 5 ############

error5 = disp5_img - array_disp5
error_sq5 = (error5)**2          
mse5 = np.mean(error_sq5)

print 'mse5',mse5                                     ##########    MSE for disparity map of view 5 ############



#############     1.2 code for consistency check    ###############


for i in range (4,height-4):                                      
    for j in range (4,width-4):
        a1=int(array_disp1[i][j])
        b1=abs(j-a1)
        a2=int(array_disp5[i][j])
        b2=abs(j+a2)
        if b1>=0:
            if array_disp1[i][j] != array_disp5[i][b1]:
                array_consist1[i][j]=0
            else: 
                array_consist1[i][j]=array_disp1[i][j]    
        if b2>=0:
            if array_disp5[i][j] != array_disp1[i][b2]:
                array_consist5[i][j]=0
            else: 
                array_consist5[i][j]=array_disp5[i][j] 
            
array_image1_chk=array_consist1/array_consist1.max()
cv2.imshow('disp_image1_chk',array_image1_chk)            #####   Disparity map for view1 after consistency check   #####

array_image5_chk=array_consist5/array_consist5.max()
cv2.imshow('disp_image5_chk',array_image5_chk)           #####   Disparity map for view5 after consistency check   #####

for i in range (4,height-4):                                      
    for j in range (4,width-4):
        if (array_consist1[i][j]!=0)and(array_consist5[i][j]!=0) and (i < 370 and j <463):
            consist_1.append(disp1_img[i][j]-array_consist1[i][j])
            consist_5.append(disp5_img[i][j]-array_consist5[i][j])

consist_1 = np.array(consist_1)
consist_5 = np.array(consist_5)

mse_cons1 = (np.sum((consist_1)**2))/(height*width)
mse_cons5 = (np.sum((consist_5)**2))/(height*width)


print ('mse_cons1',mse_cons1,'mse_cons5',mse_cons5)'''      ##  MSE for disparity maps of view1 and view5 after cosistency check ## 

