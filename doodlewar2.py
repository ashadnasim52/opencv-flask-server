# -*- coding: utf-8 -*-
"""doodlewar2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b3beLLBAuH1GatxpKzbGhYfU-JXEhZrH
"""

# from google.colab.patches import cv2_imshow
import cv2 as cv2

# img = cv2.imread('./dhoni.jpg', 1)


# cv2_imshow(img)

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2_imshow(img_gray)

# img_invert = cv2.bitwise_not(img_gray)

# cv2_imshow(img_invert)

# img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)

# cv2_imshow(img_smoothing)


# cv2_imshow(final_img)

def generate_sketch(img):
    img = cv2.imread(img, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    print(final_img)
    return final_img


def dodgeV2(x, y):

    return cv2.divide(x, 255 - y, scale=256)


if __name__ == "__main__":
    img = cv2.imread('./dhoni.jpg', 1)
    generate_sketch(img)