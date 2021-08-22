import os
import cv2
import PIL
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

def cvImshow(img):
    # RGB画像だったらBGRに変換して表示
    if img.ndim == 3:
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        plt.imshow(img)

    # グレースケール画像だったらcmap='gray'と設定して表示
    elif img.ndim == 2:
        plt.imshow(img, cmap='gray')

    else :
        print('ndim error ->',img.ndim)

    return

def pilImshow(img):
    plt.imshow(img)
    return

def myImshow(img=None, title=None, scale=(6,4)):
    rcParams['figure.figsize'] = scale[0], scale[1]
    
    if title is not None:
        plt.title(title)

    # パスを与えた場合は，imread
    if type(img) is str:
        img = cv2.imread(img)
        cvImshow(img)
        return
    # numpy配列だったらpass
    elif type(img) is np.ndarray:
        cvImshow(img)
        return
    elif type(img) is PIL.PngImagePlugin.PngImageFile:
        pilImshow(img)
        return
    # それ以外の型だったらエラー出してreturn
    else:
        print('type error ->',type(img))
        return
        
def showMultipleImages(images,col=7,row=None, label_set=True, scale=(4,3)):
    if row is None:
        row = int(len(images)/col)
    
    rcParams['figure.figsize'] = scale[0] * col, scale[1] * row
    for i in range(row):
        for j in range(col):
            plt.subplot(row,col,col * i + j + 1)
            plt.tick_params(labelbottom=label_set,labelleft=label_set)
            myImshow(images[col * i + j])
    
def concatSamePILImages(img_list,col=7,row=None):
    if row is None:
        row = len(img_list) // col
        
        if len(img_list) % col > 0:
            row += 1
    
    sum_w = img_list[0].width * col
    sum_h = img_list[0].height * row
    dst = PIL.Image.new('RGB',(sum_w,sum_h))

    for i,img in enumerate(img_list):
        paste_w = img_list[0].width * (i % col)
        paste_h = img_list[0].height * (i // col)
        dst.paste(img,(paste_w,paste_h))
        
    return dst