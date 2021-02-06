#include "laws.hpp"

namespace pyDEM {
	Law::Law(double k) : k(k) {};

	// LINEAR ELASTIC

	LinearElastic::LinearElastic(double k) : Law(k) {};

	double LinearElastic::calcF(Element *elemA, Element *elemB, double gap) {
		return k*gap;
	};
}