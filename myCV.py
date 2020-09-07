import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

def myImshow(img=None):
    # パスを与えた場合は，imread
    if type(img) is str:
        img = cv2.imread(img)
    # numpy配列だったらpass
    elif type(img) is np.ndarray:
        pass
    # それ以外の型だったらエラー出してreturn
    else:
        print('type error ->',type(img))
        return
    
    # RGB画像だったらBGRに変換して表示
    if img.ndim == 3:
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        plt.imshow(img)

    # グレースケール画像だったらcmap='gray'と設定して表示
    elif img.ndim == 2:
        plt.imshow(img, cmap='gray')
        
    else :
        print('ndim error ->',img.ndim)
        
def showMultipleImages(images,col,row, label_set=True, scale=(4,3)):
    rcParams['figure.figsize'] = scale[0] * col, scale[1] * row
    for i in range(row):
        for j in range(col):
            plt.subplot(row,col,col * i + j + 1)
            plt.tick_params(labelbottom=label_set,labelleft=label_set)
            myImshow(images[col * i + j])
    
