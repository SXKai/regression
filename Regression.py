# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:31:13 2017

@author: Q
"""
import numpy as np
from numpy import *

def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = np.mean(inMat,0)   #calc mean then subtract it off
    inVar = np.var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
def rssError(yArr,yHatArr):
    return (yArr-yHatArr).T*(yArr-yHatArr)

    
def stageWise(xArr,yArr,eps=0.001,numIt=5000):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat,0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m,n = np.shape(xMat)
    ws = np.zeros((n,1))
    returnMat = np.zeros((numIt,n))
    

    for i in range(numIt):
#        print (ws.T)
        lowestError = np.inf
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] += + sign*eps
                yTest = xMat * wsTest
                rssE = float(rssError(yMat,yTest))
                if rssE < lowestError:
                    wsMax = wsTest.copy()
                    lowestError = rssE
        ws = wsMax.copy()
        returnMat[i,:] = ws.T
    return returnMat

data,label = loadDataSet('abalone.txt')
returnMatrix = stageWise(data,label)
print(returnMatrix)