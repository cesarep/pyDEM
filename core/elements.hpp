#ifndef ELEM_H
#define ELEM_H

#include "includes.hpp"
#include "material.hpp"

namespace pyDEM {
	class Element {
		private: 
			vct v0, F0;
		public:
			double area;
			std::string group;
			std::string type;
			Element(std::string group, std::string type, Material &mat);
			void setInit(vct V, vct F);
			void applyF(vct F);
			virtual void move(double dt, vct acc_f, double disp = 0.1) {};
			virtual vct2d aabb() { return {vct0, vct0}; };
			Material *material;
			void updtMA(double a);
			vct2d coords, velocities, forces;
			double mass;
			vct view(size_t i = 0) {
				return coords[i];
			};
	};

	class Circle : public Element {
		public:
			vct center;
			double radius;
			Circle(vct c, double r, Material mat, std::string group = "circles");
			void move(double dt, vct acc_f, double disp = 0.1);
			vct2d aabb();
	};

	class Wall : public Element {
		public:
			Wall(vct p1, vct p2, std::string group = "walls");
			vct2d aabb();
			vct p1, p2, C, normal, eq;
			double length;
	};
}

#endif