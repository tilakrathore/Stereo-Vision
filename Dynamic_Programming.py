################    1.3 Disparity estimation using dynamic programming  ##############

import cv2
import numpy as np


left_img = cv2.imread('C:\Users\SONY\Desktop\sview1.png', 0)
right_img = cv2.imread('C:\Users\SONY\Desktop\sview5.png', 0)

size = left_img.shape
DisparityMatrix_l=np.zeros(size,np.uint8)
DisparityMatrix_r=np.zeros(size,np.uint8)

OcclusionCost =20


#For Dynamic Programming you have build a cost matrix. Its dimension will be num_of_cols x num_of_cols
coloumn=int(left_img.shape[1])
#CostMatrix = np.zeros((num_of_cols,num_of_cols),dtype=float)
#DirectionMatrix = np.zeros((num_of_cols,num_of_cols),dtype=float)
SolnMatrix = np.zeros((coloumn,coloumn))

#We first populate the first row and column values of Cost Matrix
 #for i in range(left_img.shape[0]):
CostMatrix = np.zeros((coloumn,coloumn))
DirectionMatrix = np.zeros((coloumn,coloumn))
for i in range(coloumn):
    CostMatrix[i,0] = i*OcclusionCost
    CostMatrix[0,i] = i*OcclusionCost

for rownum in range(size[0]):    
    for i in range(coloumn):
        for j in range(coloumn):
            first_min=CostMatrix[i-1,j-1]+np.abs((left_img[rownum,i]-right_img[rownum,j]))
            second_min=CostMatrix[i-1,j]+OcclusionCost
            third_min=CostMatrix[i,j-1]+OcclusionCost
            CostMatrix[i,j]=cmin=np.min((first_min,second_min,third_min))
            if(first_min==cmin):
                DirectionMatrix[i,j]=1
            if(second_min==cmin):
                DirectionMatrix[i,j]=2
            if(third_min==cmin):
                DirectionMatrix[i,j]=3

    p=q=coloumn-1

    while(p != 0 and q!=0) :
        if(DirectionMatrix[p,q]==1):
            DisparityMatrix_l[rownum,p]=p-q
            DisparityMatrix_r[rownum,q]=p-q
            p=p-1
            q=q-1
        elif(DirectionMatrix[p,q]==2):
            p=p-1
        elif(DirectionMatrix[p,q]==3):
            q=q-1


cv2.imshow('DisparityImage_l',DisparityMatrix_l)           ######    Disparity map for image left   #######
cv2.waitKey(0)
cv2.imshow('DisparityImage_r',DisparityMatrix_r)           ######    Disparity map for image right  #######
cv2.waitKey(0)

 
