# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:34:21 2021

@author: RezaKurniawan
"""
def index_ganjil(karakter):
    kata = [karakter[i]
             for i in range(len(karakter)) 
             if i%2==1]
    print('Karakter Index Ganjil: ',''.join(kata))
    
bacavalidinput=input('Masukan sebuah kata: ')
index_ganjil(bacavalidinput)
