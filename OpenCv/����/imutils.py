import cv2
import numpy as np
import matplotlib.pyplot as plt


def show(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()
def imread(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image