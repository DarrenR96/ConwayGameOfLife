import numpy as np 
import cv2 
from skimage.util.shape import view_as_windows

canvasShape = (64,64)
thres = 0.85

canvas = np.random.uniform(size=canvasShape)
canvas = np.where(canvas >= thres, 1, 0)



def conwayRules(center, _sum):
    sumSurrounding = _sum
    if ((center == 1) and ((sumSurrounding == 2) or (sumSurrounding == 3))):
        return 1 
    if ((center == 0) and (sumSurrounding == 3)):
        return 1 
    return 0 

rulesVectorized = np.vectorize(conwayRules)


def updateCanvas(x):
    x = np.pad(x,((1,1),(1,1)),'constant',constant_values=0)
    test = view_as_windows(x, (3,3),1)
    test = np.reshape(test,(-1,3,3))
    _center = test[:,1,1].copy()
    test[:,1,1] = 0
    _sum = np.sum(test, axis=(1,2))
    xOut = rulesVectorized(_center,_sum)
    xOut = np.reshape(xOut, canvasShape)
    return xOut 

while True:
    canvas = updateCanvas(canvas).astype(np.float32)
    canvasInfo = np.zeros((64,49))
    canvasToShow = np.concatenate([canvas,canvasInfo],-1)
    canvasToShow = np.repeat(canvasToShow, 8, axis=1).repeat(8, axis=0)
    cv2.putText(canvasToShow, "Conway's Game of Life", (560,100), 1, 1.5, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "Created by Prof. J. H. Conway (1937-2020)", (530,130), 1, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "Implemented by SigMedia with <3", (570,155), 1, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "Rules of Life:", (640,210), 1, 1.25, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "1 - Any cell with fewer than two neighbours dies (underpopulation)", (520,240), 1,0.57, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "2 - Any cell with 2 or 3 live neighbours survives a generation", (520,270), 1,0.57, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "3 - Any cell with more than 3 live neighbours dies (overpopulation)", (520,300), 1,0.57, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "4 - Any dead cell with exactly 3 live neighbours becomes alive (reproduction)", (520,330), 1,0.57, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(canvasToShow, "Tap 'R' key to reset", (620,380), 1,1, (255,255,255), 1, cv2.LINE_AA)

    cv2.putText(canvasToShow, "(Darren R.) ramsookd@tcd.ie", (760,500), 1,0.5, (255,255,255), 1, cv2.LINE_AA)



    cv2.imshow('Conways Game of Life',canvasToShow)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    if cv2.waitKey(25) & 0xFF == ord('r'):
        canvas = np.random.uniform(size=canvasShape)
        canvas = np.where(canvas >= thres, 1, 0)
        # canvasInfo = np.zeros((64,49))
        # canvas = np.concatenate([canvas,canvasInfo],-1)
