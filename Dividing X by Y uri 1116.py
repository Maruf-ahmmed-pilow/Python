# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:10:51 2023

@author: pilow
"""

n=int(input())

for i in range(n):
    
    x,y = map(int, input().split())
    
    if y==0:
        print('divisao impossivel')
        
    else:
        ans = x/y
        print(f'{ans :.1f}')
        
    