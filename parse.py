# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:05:25 2019

@author: 1234qwer
"""

import os
import logging

inputPath = "a_resized/"
outputPath = "output/"
modelPath = "pretrained/YtoX.pb"

def exec(filenames):
    for cmd in filenames:
        logging.info(cmd)
        l = os.popen(cmd)
        #l.wait()
    #cmd = "python inference.py --model " +modelPath + " --input " + inputPath + filename + " --output " + outputPath + filename + " --image_size 256"
    
    
def getAllFile():
    file_list = os.listdir(inputPath)
    l = []
    for filename in file_list:
        cmd = "python inference.py --model " +modelPath + " --input " + inputPath + filename + " --output " + outputPath + filename + " --image_size 256"
        l.append(cmd)
        exec(l)
    logging.info("success")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    getAllFile()
