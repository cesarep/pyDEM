from pyDEM import *

cena = Scene()
cena.setAccField((0, -9.81))
mat = Rigid(2500)
esf = Circle((1,1), .15, mat)
esf2 = Circle((1.5,1.2), .2, mat)
par = Wall((0,0), (2,0))

cena.addElem(esf)
cena.addElem(esf2)
cena.addElem(par)

lei = LinearElastic(50e6)

inter1 = Circle_Circle(lei)
inter2 = Circle_Wall(lei)

cena.addInter(inter1)
cena.addInter(inter2)

simu = Simulation(cena, 2000, 1e-3)

simu.calculate()