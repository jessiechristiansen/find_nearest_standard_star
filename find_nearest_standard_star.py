#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:52:51 2023

@author: jessiec
"""

import sys
import pandas as pd
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord

thisRa = sys.argv[1]
thisDec = sys.argv[2]

#print(thisRa,thisDec)

c1 = SkyCoord(thisRa, thisDec, frame='icrs')

standards = pd.read_csv('standards.csv')
numStandards = standards.shape[0]
minSep = 360.
secondBestSep = 360.
thirdBestSep = 360.
currentBestStar = 0
secondBestStar = 0
thirdBestStar = 0

for i in range(numStandards):
    
    c2 = SkyCoord(standards['ra'][i], standards['dec'][i], frame='icrs')
    thisSep = c1.separation(c2)
    thisSepDegrees = thisSep.radian*180/3.14159
    if(thisSepDegrees<minSep):
        thirdBestSep = secondBestSep
        secondBestSep = minSep
        minSep = thisSepDegrees
        thirdBestStar = secondBestStar
        secondBestStar = currentBestStar
        currentBestStar = i
        
print(minSep, "deg: ", standards['hr'][currentBestStar], " Multiple flag: ", standards['multiple'][currentBestStar], ", SpT: ", standards['sptype'][currentBestStar], ", Vmag = ", standards['vmag'][currentBestStar])
print(secondBestSep, "deg: ", standards['hr'][secondBestStar], " Multiple flag: ", standards['multiple'][secondBestStar], ", SpT: ", standards['sptype'][secondBestStar], ", Vmag = ", standards['vmag'][secondBestStar])
print(thirdBestSep, "deg: ", standards['hr'][thirdBestStar], " Multiple flag: ", standards['multiple'][thirdBestStar], ", SpT: ", standards['sptype'][thirdBestStar], ", Vmag = ", standards['vmag'][thirdBestStar])