import cv2
import numpy as np

img1=cv2.imread("Edge_detection_4/input/building.png",cv2.IMREAD_GRAYSCALE)


rows,cols=img1.shape
result=np.zeros((rows,cols),dtype=np.uint8)


filter=np.array([[-1 ,-1, -1],
                 [0, 0, 0],
                 [1, 1 ,1]])

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small=img1[i-1:i+2,j-1:j+2]
        average=np.abs(np.sum(small*filter))
        result[i,j]=average

cv2.imwrite("Edge_detection_4/output/result2.png",result)