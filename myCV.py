import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def myImshow(img=None):
    # パスを与えた場合は，imread
    if type(img) is str:
        img = cv2.imread(img)
    # numpy配列だったらpass
    elif type(img) is np.ndarray:
        pass
    # それ以外の型だったらエラー出してreturn
    else:
        print('type error')
        return
    
    # RGB画像だったらBGRに変換して表示
    if img.ndim == 3:
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        plt.imshow(img)

    # グレースケール画像だったらcmap='gray'と設定して表示
    elif img.ndim == 2:
        plt.imshow(img, cmap='gray')
    
