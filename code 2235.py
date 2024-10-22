# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 03:49:59 2024

@author: pilow
"""

class Solution(object):
    def sum(self, num1, num2):
        result = num1+num2
        print('The final result is :', result)
    
n1 = int(input('Enter the number here: '))
n2 = int(input('Enter the number here: '))

solution = Solution()

solution.sum(n1,n2)