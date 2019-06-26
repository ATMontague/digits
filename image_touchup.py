import os
from PIL import Image
import numpy as np

image_path = '/home/adam/Documents/kaggle/digits/generated_images/'
new_path = '/home/adam/Documents/kaggle/digits/cleaned_images/'

def threshold(pix):
    '''perform simple image segmentation'''
    black = (0,0,0)
    white = (255, 255, 255)
    threshold = (160, 160, 160) # how to determine threshold?
    if pix < threshold:
        return black
    return white

def convert():
    for filename in os.listdir(image_path):
        # open image and get pixels
        img = Image.open(image_path+filename).convert('LA')
        pixels = img.getdata()

        new_pixels = []
        for pixel in pixels:
            new_pixels.append(threshold(pixel))

        # create and save new image
        new = Image.new('RGB', img.size)
        new.putdata(new_pixels)
        name = new_path + filename
        new.save(name)

if __name__ == '__main__':
    convert()
