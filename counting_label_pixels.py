import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt
import os

def extracting_name_list(suffix, path=os.getcwd()):
    img_name_list = []
    with os.scandir(path) as it:
        for idx, entry in enumerate(it):
            if entry.name.split(".")[1] == suffix:
                img_name_list.append(entry.name)
    return img_name_list


def num_of_label_pixels(img_name_list, num_of_classes):
    my_list = np.empty((num_of_classes,len(img_name_list)))

    for indx, image_name in enumerate(img_name_list):
        
        fname = os.path.join("images", image_name)
        image = skimage.io.imread(fname, as_gray=True)
        c, _ = np.histogram(image, bins=9)
        my_list[:, indx] = c
    return my_list

img_name_list = extracting_name_list("png", path="images/")
my_list = num_of_label_pixels(img_name_list, 9)


# for root, dirs, files in os.walk(os.getcwd()):
#     print(files)