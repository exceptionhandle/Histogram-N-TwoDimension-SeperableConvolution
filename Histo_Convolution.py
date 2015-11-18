# -*- coding: utf-8 -*-
import time
import numpy as np
from scipy import signal as sg
import cv2
import math
import Histogram
def pad(img):
    [height,width]=img.shape
    newImg = np.array([[0 for x in range(height+2)] for x in range(width+2)])
    for i in range(1,height+1):
        for j in range(1,width+1):
            newImg[i,j] = img[i-1,j-1]
    return newImg
    
def convolution(image,kernel,i,j):
    [h,w]=kernel.shape
    sum = 0
    for x in range(h):
        for y in range(w):
            sum = sum + image[x+i,y+j]*kernel[x,y]
    return sum
    
def mirror(ker):
    [h,w]=ker.shape
    newKernel = np.array([[0 for x in range(w)] for y in range(h)])
    Kernel1 = np.array([[0 for x in range(w)] for y in range(h)])
    for x in range(h):
        for y in range(w):
            Kernel1[x,y] = ker[y,x]
    for x in range(h):
        for y in range(w/2+1):
            newKernel[x,y] = Kernel1[x,w-y-1]
            newKernel[x,w-y-1] = Kernel1[x,y]
    for x in range(h):
        for y in range(w):
            Kernel1[x,y] = newKernel[y,x]
    for x in range(h):
        for y in range(w/2+1):
            newKernel[x,y] = Kernel1[x,w-y-1]
            newKernel[x,w-y-1] = Kernel1[x,y]
    return newKernel
    
def preprocessing(image,kernel):
    newImg = pad(image)
    [height,width]=newImg.shape
    [h,w]=kernel.shape
    witer = width-2
    hiter = height-2
    x = 0
    y = 0
    if(h!=1 and w!=1):
        kernel = mirror(kernel)
    elif(h == 1):
        x = -1
        hiter = height-1
        for y in range(w/2):
            kernel[0,y]=kernel[0,w-y-1]^kernel[0,y]
            kernel[0,w-y-1]=kernel[0,w-y-1]^kernel[0,y]
            kernel[0,y]=kernel[0,w-y-1]^kernel[0,y]
    elif(w == 1):
        y = -1 
        witer = width-1
        for x in range(h/2):
            kernel[x,0]=kernel[h-x-1,0]^kernel[x,0]
            kernel[h-x-1,0]=kernel[h-x-1,0]^kernel[x,0]
            kernel[x,0]=kernel[h-x-1,0]^kernel[x,0]
    return h,w,x,y,hiter,witer,newImg,kernel
    
def convolve(image,kernel,newImage):
    [h,w,x,y,hiter,witer,newImg,kernel] = preprocessing(image,kernel)
    sum = 0
    for i in range(-x,hiter):
        for j in range(-y,witer):
            sum = 0
            for q in range(h):
                for t in range(w):
                    sum = sum + newImg[q+i,t+j]*kernel[q,t]
            newImage[i + x,j + y] = sum
    return newImage
def convolveSperateFilters(image,kernel1,kernel2,newImage):
    image = convolve(image,kernel1,newImage)
    image = convolve(image,kernel2,newImage)
    return image

def absoluteSum(im1,im2):
    [h,w] = im1.shape
    for x in range(h):
        for y in range(w):
            im1[x,y] = math.sqrt(math.pow(abs(im1[x,y]),2)+math.pow(abs(im2[x,y]),2));
            im1[x,y]=im1[x,y]/255;
    return im1

if __name__ == "__main__":
    filename = sys.argv[1:];
    ##filename = 'lena_gray.jpg';
    img = cv2.imread(filename,0)
    histoImage = Histogram.histo(img);
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    
    [h,w] = img.shape
    newImage = np.array([[0 for x in range(w)] for y in range(h)]) #####empty image
    
    conv1Kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    conv2Kernel = np.array([[-1,-2,-1], [0,0,0],[1,2,1]])
    t1 = time.clock()
    image1 = convolve(img,conv1Kernel,newImage)
    
    image2 = convolve(img,conv2Kernel,newImage)
    
    image = absoluteSum(image1,image2)
    t2 = time.clock()
    tx = t2-t1
    cv2.imwrite('Q1AbsoluteGradient.jpg',image);
    
    ###################### Seperated filters
    
    OuterKernel1 = np.array([[-1,  0,  1]])
    InnerKernel1 = np.array([[1] , [2] , [1]])
    OuterKernel2 = np.array([[-1] , [0] , [1]])
    InnerKernel2 = np.array([[1 , 2 , 1]])
    t1 = time.clock()
    image1 = convolveSperateFilters(img,OuterKernel1,InnerKernel1,newImage)
    
    image2 = convolveSperateFilters(img,OuterKernel2,InnerKernel2,newImage)
    
    image = absoluteSum(image1,image2)
    t2 = time.clock()

    print tx, t2 - t1
    cv2.imwrite('Q2AbsoluteGradient.jpg',image);

    cv2.imwrite('imagenew.jpg',image)
    image = cv2.imread('imagenew.jpg')

    cv2.imshow('image',image)