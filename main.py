import genMapList
import initImage
import biomsStruct
import utils
import numpy as np
from PIL import Image
import random

width = 1024
heigth =720
seed = random.randint(40,1001)
scale = 0.0025
myMap = genMapList.Map(width,heigth,seed=seed, scale= scale)
myMap.genMapStats()
myMap.genColoredArray(biomsStruct.bioms)
image = initImage.genImage(myMap.coloredArray)
image.show()