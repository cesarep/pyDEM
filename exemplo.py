#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de cena

@author: cesar
"""

from pyDEM import gerador as ger
        
def teste():
    cena = ger.Cena('teste')
    esf = ger.Esfera(0.2, [0, 1])
    cena.addElem(esf)
    
    esf2 = ger.Esfera(0.1, [0.3, 0.8])
    cena.addElem(esf2)
    
    par = ger.Linha((-1,0), (1, 0))
    cena.addElem(par)
    
    cena.show()

if __name__ == '__main__':
    teste()