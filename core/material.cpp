#include "material.hpp"

namespace pyDEM {
	Material::Material(double d) : density(d) {};

	Rigid::Rigid(double d) : Material(d) {};
}