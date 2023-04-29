import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("Histogram/input/R.jpg",cv2.IMREAD_GRAYSCALE)
rows,cols=img.shape
count=0
histogram=[]
height=[]
for m in range (256):
    for i in range(rows):
        for j in range(cols):
            if img[i][j]==m:
                count+=1
    histogram.append(count)
    count=0
    height.append(m)

# plt.plot(histogram)
# plt.hist(histogram)
plt.bar(height,histogram)

plt.show()
        
