#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de cena
1 disco e uma parede horizontal

@author: cesar
"""
import numpy as np

from pyDEM import gerador as ger
from pyDEM import simulador as sim

cena = ger.Cena('teste', [0, -9.81])

mat = ger.Rigido(2500)   

esf = ger.Disco(0.2, (0, .5), mat, cor=(0,128,255))
esf.CondInicial(vel=[0,-2])
cena.addElem(esf)

par = ger.Parede((-.5,0), (.5, 0))
cena.addElem(par)

lei = ger.LeiK(50e6)

inter_d_p = ger.Disco_Parede(lei)

cena.addInter(inter_d_p)

simu = sim.Simulacao(cena, 1500, dt=1e-3, diss=0.4)

simu.calcular()

def teste():
    simu.anim(1)
         
if __name__ == '__main__':
    teste()
