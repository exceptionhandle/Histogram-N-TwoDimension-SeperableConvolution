Histogram-N-TwoDimension-SeperableConvolution
=============================================

1. Contrast Enhancement using Histogram Equalization technique.

2. Two Dimensional and One Dimensional convolutions derived from two dimensional filters are used to find edges in the image.

3. Time taken in both the convolutions are returned showing that convolution using One Dimensional filters takes less time than in case of Two dimensional filters.


Following kernels are used as Filters for the edge detection in the Image

Kernel1 = 

          [[-1,0,1],

           [-2,0,2],

           [-1,0,1]]

Kernel2 = 

          [[-1,-2,-1],

           [0,0,0],

           [1,2,1]]


Following Seperable Kernels made from above kernels are then used for edge detection in the Image

From 

Kernel1 = 

          [[-1,0,1],

           [-2,0,2],

           [-1,0,1]]

Seperable Filters are

Kernel11 = 

          [[-1,  0,  1]]

Kernel12 =

          [[1] , [2] , [1]]


From 

Kernel2 = 

          [[-1,-2,-1],

           [0,0,0],

           [1,2,1]]

Seperable Filters are

Kernel21 = 

          [[-1] , [0] , [1]]

Kernel22 = 

          [[1 , 2 , 1]]


usage: Histo_Convolution.py -i <inputfile> -o <outputfile>
