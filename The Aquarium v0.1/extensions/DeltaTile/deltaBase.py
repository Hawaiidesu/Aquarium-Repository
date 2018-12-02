import pygame
pygame.init()
tileLoc = "tilepacks/pfc/"
def drawTiles(screenn,mapp,x,y,size,folder):
    # deltaView.screen.blit(pygame.image.load("tilepacks/pfc),(x2*size,y2*size))
    mappList = getMapList(mapp)
    mappData = getMapData(mapp)
    y2 = 0
    while (y2 < getMapSize(mapp)[1]):
        x2 = 0
        while (x2 < getMapSize(mapp)[0]):
            char = getMapCoords(mapp,x2,y2)
            img = getDataSprite(char,mapp)
            screenn.blit(pygame.transform.scale(pygame.image.load(folder + img),(size,size)),((x2*size)+x,(y2*size)+y))
            x2 += 1
        y2 += 1
        
    
def getMapList(mapp):
    return (mapp.split(': ')[0]).split('; ')

def getMapListRaw(mapp):
    return mapp.split(': ')[0]

def getMapData(mapp):
    return (mapp.split(': ')[1]).split('; ')

def getMapDataRaw(mapp):
    return mapp.split(': ')[1]

def convertMap(listt,data):
    return listt + ": " + data

def convertMapList(listt):
    newList = ""
    i = 0
    while i < len(listt):
        newList += listt[i]
        if i != len(listt) - 1:
            newList += "; "
        i += 1
    return newList


def addMapCoord(mapp,x,y,char):
    mappList = getMapList(mapp)
    # mappList[y][x] = chr(char)
    mappList[y] = mappList[y][0:x] + char + mappList[y][x+1:len(mappList[y])]
    newList = convertMapList(mappList)
    return convertMap(newList,getMapDataRaw(mapp))

def getMapCoords(mapp,x,y):
    mappList = (mapp.split(': ')[0]).split('; ')
    return mappList[y][x]

def getMapSize(mapp):
    mappList = (mapp.split(': ')[0]).split('; ')
    returnVal = [len(mappList[0]),len(mappList)]
    return returnVal

def getDataSprite(char,mapp):
    mappData = (mapp.split(': ')[1]).split('; ')
    returnVal = "pfc_stone.png"
    i = 0
    while(i < len(mappData)-1):
        if (char == mappData[i].split(', ')[1]):
            returnVal = mappData[i].split(', ')[0]
        i += 1
    return returnVal

"""
getMapCoords(mapp1,1,1)
print(getMapSize(mapp1)) 
"""
