# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16SrKjRNQIPjlLjbNmXysQnkj7dLC2IEb
"""

from google.colab import files


uploaded=files.upload()

import csv
import io
import numpy as np
from numpy import genfromtxt 

arry=np.genfromtxt(r'work.csv',delimiter=',',dtype=int)
menu = {}
menu['1']="Compute correlation" 
menu['2']="Ranked list of 30 largest Shipments(by warehouse block"
menu['3']="List of 30 Orders with lowest Cost/Weight ratios"
menu['4']="Exit"
print(menu)
n=input("enter the selection")
if n == "1":
 def corre_index (i,j):
      
   i= int(input("enter the number for the first quantity"))
   j= int(input("enter the number for the second quantity"))
   k= np.corrcoef(arry[i],arry[j])
 print(k)
 print(menu)
  
elif n == "2":
        k = int(input("enter the warhouse block number"))
        print(np.sort(arry))
        print(menu)      
    
elif n == "3":
        
        arry= arry[5]/arry[10]
        
        
        print(arry[0:10])
        print(menu)
else :
        print(quit)
        quit()