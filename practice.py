import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def transformation(A):
    '''simple linear transformation of matrix'''
    # playing around with simple geometric transformations
    pass

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

path = '/home/adam/Documents/kaggle/digits/data/'
train = pd.read_csv(path+'train.csv')

# save label
target = train['label']
train = train.drop('label', axis=1)

# get single number
big_list = []
for i in range(10):
    big_list.append(to_matrix(train.iloc[i].tolist()))
    plt.imshow(big_list[i], cmap='gray')
    name = 'image_{}.png'.format(i)
    plt.savefig(path+name, format='png')
