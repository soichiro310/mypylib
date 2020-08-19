import os
import sys
import warnings
import glob
warnings.simplefilter('ignore')

def makeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(path,'created')
        
def getFileList(dir_path):
    return sorted(glob.glob(dir_path + '/*'))

