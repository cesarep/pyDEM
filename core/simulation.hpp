#ifndef SIMULATION_H
#define SIMULATION_H

#include "includes.hpp"
#include "elements.hpp"
#include "interactions.hpp"
#include "scene.hpp"

namespace pyDEM {
	class Contact {
		public:
			Element *elemA, *elemB;
			Interaction *inter;
			double gap;
			Contact(Element *elemA, Element *elemB, Interaction *inter);
			void verify();
			void applyF();
	};

	struct candidate {
		double pos;
		int type;
		Element *ref;
		bool included;
	};

	class Simulation {
		public:
			Scene *scene;
			size_t N, step = 0;
			double dt;
			Simulation(Scene &scene, size_t steps, double dt = 1e-3);
			void calculate();
			void _step();
			void _init_detec();
			Interaction *_dect_inter(Element *elA, Element *elB);
			void _fine_detec();
			void _calcF();
			void _upd_move();
		private:
			std::vector<Contact> contacts;
			std::vector<candidate> axis;
			std::vector<candidate> candidates;
	};
};

#endif