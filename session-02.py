# pillow
# pip install pillow
from PIL import Image
import numpy as np

img = Image.open("images/3702795048.png")
print(type(img))

# img.show()
print(img.format)

img1 = np.asarray(img)
print(img.size) #(width, height)
############################################

# matplotlib
# pip install matpotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img2 = mpimg.imread("images/3702795048.png")
print(type(img2))
print(img2.shape[:2])

plt.imshow(img2)
############################################
# pip install scikit-image
from skimage import io, img_as_float
import matplotlib.pyplot as plt

img3 = io.imread("images/3702795048.png")
plt.imshow(img3)
img3_float = img_as_float(img3)
############################################

# pip install opencv-python
import cv2
img4 = cv2.imread("images/3702795048.png", 0)
img4_color = cv2.imread("images/3702795048.png", 1)

cv2.imshow("Grey Image",img4)
cv2.imshow("color Image",img4_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################

import cv2
import glob
path = "images/*"

fig, axes = plt.subplots(nrows=1, ncols=4)
for indx, img_path in enumerate(glob.glob(path)):
    if img_path.split(".")[1] == "png":
        img = cv2.imread(img_path)
        img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        axes[indx].imshow(img_)
    