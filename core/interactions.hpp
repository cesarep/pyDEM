#ifndef INTER_H
#define INTER_H

#include "includes.hpp"
#include "elements.hpp"
#include "laws.hpp"

namespace pyDEM {
	class Interaction {
		public:
			std::string groupA, groupB;
			virtual double verify(Element *elemA, Element *elemB) { return 0; };
			virtual vct2d getNormal(Element *elemA, Element *elemB) { return {vct0, vct0}; };
			virtual void applyF(Element *elemA, Element *elemB, vct2d N, double F) {};
			Interaction(std::string ga, std::string gb, Law &law);
			Law *law;
	};

	class Circle_Circle : public Interaction {
		public:
			Circle_Circle(Law law);
			double verify(Circle *elemA, Circle *elemB);
			vct2d getNormal(Circle *elemA, Circle *elemB);
			void applyF(Circle *elemA, Circle *elemB, vct2d N, double F);
	};
	
	class Circle_Wall : public Interaction {
		public:
			Circle_Wall(Law law);
			double verify(Circle *circle, Wall *wall);
			double verify(Wall *wall, Circle *circle);
			vct2d getNormal(Circle *circle, Wall *wall);
			vct2d getNormal(Wall *wall, Circle *circle);
			void applyF(Circle *circle, Wall *wall, vct2d N, double F);
			void applyF(Wall *wall, Circle *circle, vct2d N, double F);
	};

}

#endif