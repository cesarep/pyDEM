#ifndef MATERIAL_H
#define MATERIAL_H

namespace pyDEM {
	class Material {
		public:
			double density;
			Material(double d);
	};

	class Rigid : public Material {
		public:
			Rigid(double d);
	};
}

#endif