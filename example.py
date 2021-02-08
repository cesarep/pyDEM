from pyDEM import *

cena = Scene()
cena.setAccField((0, -9.81))

mat = Rigid(2500)

esf = Circle((1,1), .15, mat)
esf.setInit((1.5, -.5), (0,0))
cena.addElem(esf)

esf2 = Circle((1.5,1.2), .2, mat)

par = Wall((0,0), (3,0))


cena.addElem(esf2)
cena.addElem(par)

lei = LinearElastic(50e6)

inter1 = Circle_Circle(lei)
inter2 = Circle_Wall(lei)

cena.addInter(inter1)
cena.addInter(inter2)

simu = Simulation(cena, 2000, 1e-3)

simu.calculate()

coords1 = [esf.view(x) for x in range(0, 2000)]
coords2 = [esf2.view(x) for x in range(0, 2000)]

import matplotlib.pyplot as plt
x1, y1 = zip(*coords1)
x2, y2 = zip(*coords2)

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.savefig("plot.png")