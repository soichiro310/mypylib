import os
import sys
import warnings
import glob
import json
import pickle
warnings.simplefilter('ignore')

def makeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(path,'created')
        
def getFileList(dir_path):
    return sorted(glob.glob(dir_path + '/*'))

def json_load(path):
    return json.load(open(path,"r"))
    
def json_dump(obj,path):
    return json.dump(open(path,"w"))

def pickle_load(path):
    return pickle.load(open(path,"rb"))

def pickle_dump(obj,path):
    return pickle.dump(obj,open(path,"wb"))