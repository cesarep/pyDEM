#include "includes.hpp"

double norm(vct v){
	return sqrt((v*v).sum());
};

double sgn(double x) {
	return (x < 0.) ? -1. : (x > 0.);
}

vct dir(vct v){
	return v/norm(v);
};