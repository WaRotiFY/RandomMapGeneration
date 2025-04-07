from perlin import  SimplexNoise
import utils
import numpy as np



class Generation(SimplexNoise):
    def genHeightMap(self,width,height,maxHeight = 1,seed = 324, scale = 0.004):
        Generation.randomize(self,seed)
        genMapList = []
        for i in range(height):
            genMapList.append([])
        for y in range(height):
            print(y)
            for x in range(width):
                genMapList[y].append(Generation.noise2(self,x*scale,y*scale)*maxHeight)
        return np.array(genMapList)

    def genTemperatureMap(self,width,height, minusPlusHeightMap, maxTemp = 20, scaleTempWithHeith = 20, seed = 324, scale = 0.004):
        Generation.randomize(self,seed)
        genTempList = []
        for i in range(height):
            genTempList.append([])
        for y in range(height):
            print(y)
            for x in range(width):
                genTempList[y].append(Generation.noise2(self,x*scale,y*scale)*maxTemp)
                genTempList[y][x]-=abs(minusPlusHeightMap[y][x])*scaleTempWithHeith

        return np.array(genTempList)

    def genHumidityMap(self,width,height,seed = 324, scale = 0.004):
        Generation.randomize(self,seed)
        humidityToProcent = 50
        genHumidityList = []
        for i in range(height):
            genHumidityList.append([])
        for y in range(height):
            print(y)
            for x in range(width):
                genHumidityList[y].append((Generation.noise2(self,x*scale,y*scale)+1)*humidityToProcent)
        return np.array(genHumidityList)

class Map(Generation):
    def __init__(self,width,height,seed = 324, scale = 0.004, maxHeight = 1, maxTemp = 20, scaleTempWithHeith = 20):
        self.width = width
        self.height = height
        self.seed = seed
        self.scale = scale
        self.maxHeight = maxHeight
        self.maxTemp = maxTemp
        self.scaleTempWithHeith = scaleTempWithHeith
        self.seed = seed
    def genMapStats(self):
        self.heightMap = Map.genHeightMap(self,self.width,self.height,maxHeight=self.maxHeight,seed=self.seed, scale=self.scale)
        self.tempMap = Map.genTemperatureMap(self,self.width,self.height,utils.minusPlusNormilize(self.heightMap),maxTemp=self.maxTemp, scaleTempWithHeith=self.scaleTempWithHeith, seed=self.seed, scale=self.scale)
        self.humidityMap = Map.genHumidityMap(self,self.width,self.height,seed=self.seed, scale=self.scale)
        self.heightMap = utils.normilize(np.array(self.heightMap))
        self.tempMap = utils.normilize(np.array(self.tempMap))
        self.humidityMap = utils.normilize(np.array(self.humidityMap))
    def genColoredArray(self,bioms):
        self.coloredArray = []
        for y in range(self.height):
            self.coloredArray.append([])
            print(y)
            for x in range(self.width):
                for biom in bioms:
                    if utils.inRange(self.heightMap[y][x],biom.heightRange) and\
                            utils.inRange(self.tempMap[y][x],biom.tempRange) and\
                            utils.inRange(self.humidityMap[y][x],biom.humidityRange):

                        self.coloredArray[y].append(biom.color)
                        break

        self.coloredArray = np.array(self.coloredArray)






class Biom:
    def __init__(self,name,heightRange, tempRange, humidityRange, color = [0,0,0], texture = None):
        self.name = name
        self.heightRange = heightRange
        self.tempRange = tempRange
        self.humidityRange = humidityRange
        self.color = color
        self.texture = texture