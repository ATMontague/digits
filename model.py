import pandas as pd
import numpy as np
from sklearn import svm, metrics

def threshold(x):
    if x < 160:
        return 0
    return 255

path = '/home/adam/Documents/kaggle/digits/data/'
train = pd.read_csv(path+'train.csv')

# save label
target = train['label']
train = train.drop('label', axis=1)

print(train.shape)
print(train.head(5))

# thresholding to cleanup image
train = train.applymap(threshold)
