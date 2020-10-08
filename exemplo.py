#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de cena

@author: cesar
"""
import numpy as np

from pyDEM import gerador as ger
from pyDEM import simulador as sim

mat = ger.Rigido(2500)   

esf = ger.Disco(0.2, (-0.2, 1), mat, cor=(0,128,255))
esf.CondInicial(vel=[2, -1])

esf2 = ger.Disco(0.1, (0.25, 0.8), mat, cor=(128,128,0))
par = ger.Parede((-1,.2), (1, .1))
#par2 = ger.Parede( (0, 0.5), (1, 1))

lei = ger.LeiK(50e6)

inter_d_d = ger.Disco_Disco(lei)
inter_d_p = ger.Disco_Parede(lei)

cena = ger.Cena('teste', [0, -9.81])
cena.addElem([esf, esf2])
cena.addElem(par)
#cena.addElem(par2)

cena.addInter([inter_d_d, inter_d_p])

simu = sim.Simulacao(cena, 1000, dt=1e-3)

cena.show()

simu.calcular()


def teste():
    simu.anim(1)
         
if __name__ == '__main__':
    teste()