# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:55:19 2023

@author: pilow
"""
while True:
    x,y = map(int, input().split())
    if (x == 0) or (y ==0 ):
        break
    
    if (x>0) and (y>0):
        print('primeiro')
        
    if (x>0) and (y<0):
        print('quarto')
    
    if (x<0) and (y<0):
        print('terceiro')
        
    if (x<0) and (y>0):
        print('segundo')

