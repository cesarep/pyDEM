#include "elements.hpp"

namespace pyDEM {
	Element::Element(std::string group, std::string type, Material &mat) :
		v0(vct0), F0(vct0), group(group), type(type), material(&mat) {
			velocities.push_back(v0);
			velocities.push_back(v0);
			forces.push_back(F0);
		};

	void Element::setInit(vct V, vct F) {
		v0 = V;
		F0 = F;
		forces[0] = F0;
		velocities[0] = v0;
		velocities[1] = v0;
	};

	void Element::applyF(vct F){
		forces.end()[-1] += F;
	};

	void Element::updtMA(double a) {
		area = a;
		mass = area*material->density;
	};

	// CIRCLE

	Circle::Circle(vct c, double r, Material mat, std::string group) 
		: Element(group, "CIRCLE", mat), center(c), radius(r) {
		updtMA(M_PI*radius*radius);
		coords.push_back(center);
	};
	
	void Circle::move(double dt, vct acc_f, double disp) {
		vct a = forces.end()[-1]/mass + acc_f;
		
		vct vn = (velocities.end()[-1] + velocities.end()[-2])/2. + a*dt;
		velocities.push_back(vn);
		
		vct cn = coords.end()[-1] + vn*dt;
		coords.push_back(cn);

		forces.push_back(vct0);
	};
	vct2d Circle::aabb(){
		vct C = coords.end()[-1], 
			r = {-radius, radius};
		return vct2d {{C[0]+r, C[1]+r}};
	};

	// WALL

	Material _nullmat = Material(0);


	Wall::Wall(vct p1, vct p2, std::string group)
		: Element(group, "WALL", _nullmat), p1(p1), p2(p2) {
		updtMA(0);
		C = (p1 + p2)/2.;
		vct L = p2 - p1, u = dir(L);
		length = norm(L);
		normal = {-u[1], u[0]};
		eq = {normal[0], normal[1], 
				p1[0]*p2[1]-p1[1]*p2[0]};
	};
	vct2d Wall::aabb(){
		auto x = std::minmax(p1[0], p2[0]),
			 y = std::minmax(p1[1], p2[1]);
		return vct2d {{x.first - 0.1*length, x.second + 0.1*length}, 
					  {y.first - 0.1*length, y.second + 0.1*length}};
	};
}