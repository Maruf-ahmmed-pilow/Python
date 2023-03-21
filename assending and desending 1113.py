# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:27:39 2023

@author: pilow
"""

while True:
    x,y = map(int, input().split())
    
    if x == y:
        break
    
    
    elif x > y:
        print('Decrescente')
        
    else:
        print('Crescente')
            
        