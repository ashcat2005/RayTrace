#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:00:07 2018
Main Module

  

@author: ashcat
"""
import numpy as np
from photon import Photon
from initialConditions import initCond 
from metrics import minkowski as m  
from geodesicIntegration import geoInt     
 

########## Screen Definition ##########

# Number of X and Y pixels
screenX = 2
screenY = 2

if screenX & 1:
    alphaMax = screenX - 1
else:
    alphaMax = screenX

if screenY & 1:
    betaMax = screenY - 1
else:
    betaMax = screenY 
    
alphaRange = np.arange(-alphaMax/2, alphaMax/2 +1)
betaRange = np.arange(-betaMax/2, betaMax/2 +1)

print ("Size of the screen in Pixels:", alphaMax+1, "X", betaMax+1)
print ("Number of Pixels: ", (alphaMax+1)*(betaMax+1))

# Distance to the Black hole 
D = 100.

# Inclination of the image plane
i = np.pi/4

#######################################


rDataArray = np.zeros(((alphaMax+1),(betaMax+1)))

print(rDataArray)

# Define a photon       
p = Photon(Alpha = 1., Beta = 0., D = D, i = i)    

# Initial position and momentum of the photon
# p.xin
# p.kin


# Build the initial conditions needed to solve the geodesic equations
# [t, r, theta, phi, k_t, k_r, k_theta, k_phi] and stores in the variable
# p.iC of the Photon class

p.initConds(initCond(p.xin, p.kin, m.g(p.xin)))


finalPos, j = geoInt(m.geodesics, p.iC)

p.finalPosition(finalPos)


print(" Number of Steps to reach the Equatorial Plane:",j)
print()
print("t  ", p.iC[0], "  ", p.fP[0])
print("r  ", p.iC[1], "  ", p.fP[1])
print("th ", p.iC[2], "  ", p.fP[2])
print("ph ", p.iC[3], "  ", p.fP[3])
print("E ", p.iC[4], "  ", p.fP[4])
print("L ", p.iC[7], "  ", p.fP[7])


