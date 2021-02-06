#include "simulation.hpp"

namespace pyDEM {

	Contact::Contact(Element *elemA, Element *elemB, Interaction *inter) :
		elemA(elemA), elemB(elemB), inter(inter) {};

	void Contact::verify() {
		if(inter)
			gap = inter->verify(elemA, elemB);					
	};
	void Contact::applyF() {
		if(gap > 0. and inter){
			vct2d N = inter->getNormal(elemA, elemB);
			double F = inter->law->calcF(elemA, elemB, gap);
			inter->applyF(elemA, elemB, N, F);
		};
	};

	// SIMULATION

	Simulation::Simulation(Scene &scene, size_t steps, double dt) :
		scene(&scene), N(steps), dt(dt) {
			/*
			auto minmass = *std::min_element(scene.elements.begin(), scene.elements.end(), [](Element *A, Element *B){
				return A->mass < B->mass;
			});
			auto maxk = *std::min_element(scene.interactions.begin(), scene.interactions.end(), [](Interaction *A, Interaction *B){
				return A->law->k < B->law->k;
			});
			//std::cout << "min mass: " << minmass->mass << ", max k: " << maxk->law->k << std::endl;
			double dtc = 2*std::sqrt(minmass->mass/maxk->law->k);
			if(dt > dtc){
				std::cout << dtc << std::endl;
				//throw std::domain_error("time step bigger than critical!");
			}
			*/
		};
	void Simulation::calculate() {
		for(step=0; step < N; step++){
			double progress = (double) (step+1)/N;
			std::cout.flush();
			std::cout << "[" << std::setw(40) << std::left
				<< std::string((int) 40*progress, '#') << "] "
				<< std::setprecision(3) << std::setw(4) << 100*progress << "%\r";
			_step();
		};
		std::cout << std::endl;
	};
	void Simulation::_step() {
		_init_detec();
		_fine_detec();
		_calcF();
		_upd_move();
	};
	void Simulation::_init_detec(){

		contacts.clear();
		candidates.clear();
		axis.clear();

		for(auto &v : scene->elements){
			axis.push_back({v->aabb()[0][0], -1, v, false});
			axis.push_back({v->aabb()[0][1], 1, v, false});
		};
		std::sort(axis.begin(), axis.end(), [](candidate &a, candidate &b){
			return (a.pos < b.pos);
		});

		for(size_t i = 0; i < axis.size(); i++){
			if(axis[i].type < 0){
				Element *ref = axis[i].ref;
				size_t j=i+1, c=0;
				while (axis[j].ref != ref){
					if(axis[j].type < 0 and !axis[j].included){
						candidates.push_back(
							{axis[j].ref->aabb()[1][0], -1, axis[j].ref, false}
						);
						candidates.push_back(
							{axis[j].ref->aabb()[1][1], 1, axis[j].ref, false}
						);
						axis[j].included = true;
						c++;
					};
					j++;
				};
				if(c>0){
					candidates.push_back({
						ref->aabb()[1][0], -1, ref, false
					});
					candidates.push_back({
						ref->aabb()[1][1], 1, ref, false
					});
				}
			};
		}

		std::sort(candidates.begin(), candidates.end(), [](candidate &a, candidate &b){
			return (a.pos < b.pos);
		});

		for(size_t i = 0; i < candidates.size(); i++){
			if(candidates[i].type < 0){
				Element* ref = candidates[i].ref;
				size_t j=i+1;
				while (candidates[j].ref != ref){
					if(candidates[j].type < 0 and !candidates[j].included){
						auto inter = _dect_inter(candidates[i].ref, candidates[j].ref);
						if(inter)
							contacts.push_back(
								Contact(candidates[i].ref, candidates[j].ref, inter)
							);
						candidates[j].included = true;
					};
					j++;
				};
			};
		}
		

	};

	Interaction *Simulation::_dect_inter(Element *elA, Element *elB) {
		auto inter = *std::find_if(scene->interactions.begin(), scene->interactions.end(),
			[&](Interaction *a){
				return (elA->group == a->groupA and elB->group == a->groupB) 
				or (elB->type == a->groupA and elA->type == a->groupB);
			});
		return inter;
	};

	void Simulation::_fine_detec(){
		for(auto &cont : contacts)
			cont.verify();
		/*
		std::remove_if(contacts.begin(), contacts.end(), [](Contact *c){
			c->verify();
			return c->gap < 0;
		});
		*/
	};
	void Simulation::_calcF(){
		for(auto &cont : contacts)
			cont.applyF();
	};
	void Simulation::_upd_move(){
		for(auto &el : scene->elements)
			el->move(dt, scene->acc_field);
	};
	
}