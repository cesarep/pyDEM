#ifndef LAWS_H
#define LAWS_H

#include "includes.hpp"
#include "elements.hpp"

namespace pyDEM {
	class Law {
		public:
			double k;
			virtual double calcF(Element *elemA, Element *elemB, double gap) { return 0; };
			Law(double k);
	};

	class LinearElastic : public Law {
		public:
			LinearElastic(double k);
			double calcF(Element *elemA, Element *elemB, double gap);
	};
}

#endif