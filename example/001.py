#--------------------------------------------------------------------------------- Location
# examle/001.py

#--------------------------------------------------------------------------------- Description
# change picture

#--------------------------------------------------------------------------------- Import
import cv2
import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------- Class
#-------------------------- [Data]
sharpen_kernel = np.array([[ 0, -1,  0],
                           [-1,  5, -1],
                           [ 0, -1,  0]])

sharpen_kernel_strong = np.array([[ 0, -1,  0],
                                  [-1,  9, -1],
                                  [ 0, -1,  0]])

#-------------------------- [Action]
img = cv2.imread("./file/001.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#--------------a
plt.imshow(img)
plt.show()
#--------------b
img_sharpen = cv2.filter2D(img, -1, sharpen_kernel)
plt.imshow(img_sharpen)
plt.show()
#--------------c
img_sharpen = cv2.filter2D(img, -1, sharpen_kernel_strong)
plt.imshow(img_sharpen)
plt.show()


# # Apply filter using cv2.filter2D
# sharpened = cv2.filter2D(img, -1, sharpen_kernel)

# # Save or show result
# cv2.imwrite("sharpened.jpg", sharpened)




#-------------------------- [Add]