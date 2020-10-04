#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de cena

@author: cesar
"""

from pyDEM import gerador as ger 

mat = ger.Rigido(250)   
esf = ger.Disco(0.2, (0, 1), mat, cor=(0,128,255))
esf.CondInicial(vel=[1, 0])
esf2 = ger.Disco(0.1, (0.3, 0.8), mat, cor=(128,128,0))
par = ger.Parede((-1,0), (1, 0))
    
    
def teste():
    cena = ger.Cena('teste')
    cena.addElem([esf, esf2])
    cena.addElem(par)
    cena.show()

if __name__ == '__main__':
    teste()