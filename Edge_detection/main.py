import cv2
import numpy as np

img1=cv2.imread("Edge_detection/input/lion.png",cv2.IMREAD_GRAYSCALE)
img2=cv2.imread("Edge_detection/input/spider.png",cv2.IMREAD_GRAYSCALE)


rows_1,cols_1=img1.shape
rows_2,cols_2=img2.shape
lion_result=np.zeros((rows_1,cols_1),dtype=np.uint8)
spider_result=np.zeros((rows_2,cols_2),dtype=np.uint8)


lion_filter=np.array([[-1 ,-1, -1],
                 [-1, 8, -1],
                 [-1, -1 ,-1]])

for i in range(1,rows_1-1):
    for j in range(1,cols_1-1):
        small_1=img1[i-1:i+2,j-1:j+2]
        average_1=np.sum(small_1*lion_filter)
        lion_result[i,j]=average_1

cv2.imwrite("Edge_detection/output/result1.png",lion_result)

spider_filter=np.array([[-1 ,-1, -1],
                         [-1, 7, -1],
                            [-1, -1 ,-1]])


for i in range(1,rows_2-1):
    for j in range(1,cols_2-1):
        small_2=img2[i-1:i+2,j-1:j+2]
        average_2=np.abs(np.sum(small_2*spider_filter))
        spider_result[i,j]=average_2

cv2.imwrite("Edge_detection/output/result2.png",spider_result)
