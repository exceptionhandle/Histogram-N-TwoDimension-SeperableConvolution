# -*- coding: utf-8 -*-
import os,cv2
import matplotlib.pyplot as plt
import numpy as np
os.getcwd()
os.chdir('/Users/keshavsharma/Desktop/1st Sem Courses/Computer Vision/Computer Vision HomeWork')
def plot(dict):
    plt.bar([i for i in range(256)],dict.values(),1,color='green')
    plt.ylabel('Cumulative Frequency')
    plt.xlabel('Pixel Intensity')
    plt.title('Cumulative Histogram of the Original Image')
    plt.show()

def histo(img):
    height = img.shape[0];
    width = img.shape[1];
    i = 0;
    j = 0;
    H={1:0}
    maxLevel = 0
    #### create histogram of the original image
    for i in range(0,height):
   	for j in range(0,width):
		if(img[i,j] in H):
  		    H[img[i,j]] = H[img[i,j]] + 1;
                else:
                    H[img[i,j]] = 1;
                    if(img[i,j]>maxLevel):
                        maxLevel = img[i,j];
    
    if(0 in H):
        Hc={0:H[0]};
        tp={0:round(H[0]*(maxLevel-1)/(height*width))}
    else:
        Hc={0:0};
        tp={0:0};
    for i in range(0,maxLevel):
        if(i in H):
            Hc[i+1] = Hc[i] + H[i+1];
        else:
            Hc[i+1] = Hc[i];
        tp[i+1] = round(Hc[i+1]*maxLevel/(height*width));
    

    numBins = 200

    i = 0;
    j = 0;
    for i in range(0,height):
        for j in range(0,width):
            img[i,j]=tp[img[i,j]];
    enhanced_H={1 :0}
    for i in range(1,256):
        enhanced_H[i]=0
    #### create histogram of the image with enhanced contrast
    for i in range(0,height):
   	for j in range(0,width):
		if(img[i,j] in enhanced_H):
  		    enhanced_H[img[i,j]] = enhanced_H[img[i,j]] + 1;
                else:
                    enhanced_H[img[i,j]] = 1;
    plot(Hc);
    return img
    
img = cv2.imread('Roger_gray.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL);
img = histo(img);
cv2.imwrite('Roger_contrast.jpg',img);