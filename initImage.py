import genMapList
import utils
import numpy as np
from PIL import Image
import random



def genImage(colorArray):
    return Image.fromarray(colorArray.astype(np.uint8))