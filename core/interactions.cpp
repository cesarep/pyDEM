#include "interactions.hpp"

namespace pyDEM {
	Interaction::Interaction(std::string ga, std::string gb, Law &law) :
				groupA(ga), groupB(gb), law(&law) {};

	// CIRCLE - CIRCLE
	Circle_Circle::Circle_Circle(Law law) : Interaction("CIRCLE", "CIRCLE", law) {};
	
	double Circle_Circle::verify(Circle *elemA, Circle *elemB) {
		vct ca = elemA->coords.end()[-1], cb = elemB->coords.end()[-1];
		double ra = elemA->radius, rb = elemB->radius;
		double d = norm(ca-cb);
		return d <= ra+rb ? ra+rb-d : -1; 
	};
	
	vct2d Circle_Circle::getNormal(Circle *elemA, Circle *elemB) {
		vct ca = elemA->coords.end()[-1], cb = elemB->coords.end()[-1];
		vct na = dir(ca-cb);
		return vct2d {na, -na};
	};
	
	void Circle_Circle::applyF(Circle *elemA, Circle *elemB, vct2d N, double F){
		elemA->applyF(N[0]*F);
		elemB->applyF(N[1]*F);
	};

	// CIRCLE - WALL

	Circle_Wall::Circle_Wall(Law law) : Interaction("CIRCLE", "WALL", law) {};
	
	double Circle_Wall::verify(Circle *circle, Wall *wall){
		vct c = circle->coords.end()[-1];
		vct cc = {c[0], c[1], 1.};
		double d = std::abs((cc*wall->eq).sum()),
				r = circle->radius;
	
		return d <= r ? r-d : -1;
	};

	double Circle_Wall::verify(Wall *wall, Circle *circle) {
		return verify(circle, wall);
	};

	vct2d Circle_Wall::getNormal(Circle *circle, Wall *wall) {
		vct c = circle->coords.end()[-1];
		vct cc = {c[0], c[1], 1.};
		double d = (cc*wall->eq).sum();

		vct N = sgn(d)*wall->normal;

		return vct2d {-N, N};
	};

	vct2d Circle_Wall::getNormal(Wall *wall, Circle *circle) {
		vct2d Ns = getNormal(circle, wall);
		return {Ns[1], Ns[0]};
	};

	void Circle_Wall::applyF(Circle *circle, Wall *wall, vct2d N, double F){
		circle->applyF(N[0]*F);			
	};

	void Circle_Wall::applyF(Wall *wall, Circle *circle, vct2d N, double F){
		applyF(circle, wall, N, F);
	};
}