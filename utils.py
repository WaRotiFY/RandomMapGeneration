import numpy as np
import math


def normilize(values):
    minVal = np.min(values)
    maxVal = np.max(values)
    return (values - minVal)/(maxVal-minVal)

def minusPlusNormilize(values):

    return (normilize(values))*2-1

def blackAndWhiteFromList(values):
    colorArr = []
    for y in range (np.shape(values)[0]):
        colorArr.append([])
        for x in range (np.shape(values)[1]):
            colorArr[y].append([math.floor(values[y][x]*255),math.floor(values[y][x]*255),math.floor(values[y][x]*255)])
    return np.array(colorArr)

def inRange(x,myRange):
    if myRange[0]<=x<=myRange[1]:
        return True
    else:
        return False