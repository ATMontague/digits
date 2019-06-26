import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/home/adam/Documents/kaggle/digits/data/'

def to_matrix(image_list):
    '''convert list to 2d matrix'''
    matrix = []
    counter = 0
    for i in range(0,28):
        x = []
        for j in range(0,28):
            x.append(image_list[counter])
            counter+=1
        matrix.append(x)
    return matrix

if __name__ == '__main__':
    train = pd.read_csv(path+'train.csv')
    # drop label
    train = train.drop('label', axis=1)
    for i in range(10):
        img = to_matrix(train.iloc[i].tolist())
        plt.imshow(img, cmap='gray')
        name = 'image_{}.png'.format(i)
        plt.savefig(path+name, format='png')
