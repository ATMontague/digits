import pandas as pd
import numpy as np

path = '/home/adam/Documents/kaggle/digits/data/'
train = pd.read_csv(path+'train.csv')

# save label
target = train['label']
train = train.drop('label', axis=1)

print(train.shape)
print(train.head(5))
