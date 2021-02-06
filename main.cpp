#include "core/core.hpp"

using namespace pyDEM;

int main(){
	std::cout << "Iniciando simulação" << std::endl;
	Scene cena;
	cena.setAccField({0, -9.81});

	Material mat = Rigid(2500.);

	Circle esf = Circle({-0.2, .3}, 0.2, mat);
	esf.setInit({2, -1}, {0,0});

	Circle esf2 = Circle({0.25, .8}, 0.1, mat);

	Circle esf3 = Circle({0.3, 1.3}, 0.15, mat);

	cena.addElem(esf);
	cena.addElem(esf2);
	cena.addElem(esf3);

	auto par = Wall({-1, 0}, {1, 0});

	cena.addElem(par);

	auto lei = LinearElastic(50e6);

	auto inter_dd = Circle_Circle(lei);
	auto inter_dp = Circle_Wall(lei);

	cena.addInter(inter_dd);
	cena.addInter(inter_dp);

	auto simu = Simulation(cena, 2000, 1e-3);

	simu.calculate();

	std::cout << "Simulação concluida" << std::endl;

	return 0;
}