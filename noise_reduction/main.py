import cv2
import numpy as np

# img1=cv2.imread("noise_reduction/input/board_noisy.png",cv2.IMREAD_GRAYSCALE)
# img1=cv2.imread("noise_reduction/input/image_noisy.png",cv2.IMREAD_GRAYSCALE)
img1=cv2.imread("noise_reduction/input/xray_noisy.png",cv2.IMREAD_GRAYSCALE)


rows,cols=img1.shape
result=np.zeros((rows,cols),dtype=np.uint8)


# filter=np.ones((3,3))/9
# for i in range(1,rows-1):
#     for j in range(1,cols-1):
#         small=img1[i-1:i+2,j-1:j+2]
#         average=np.sum(small*filter)
#         result[i,j]=average


# filter=np.ones((5,5))/25
# for i in range(2,rows-2):
#     for j in range(2,cols-2):
#         small=img1[i-2:i+3,j-2:j+3]
#         average=np.sum(small*filter)
#         result[i,j]=average


filter=np.ones((15,15))/225
for i in range(7,rows-8):
    for j in range(7,cols-8):
        small=img1[i-7:i+8,j-7:j+8]
        average=np.sum(small*filter)
        result[i,j]=average

cv2.imwrite("noise_reduction/output/result9.png",result)