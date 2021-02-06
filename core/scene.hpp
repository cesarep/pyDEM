#ifndef SCENE_H
#define SCENE_H

#include "includes.hpp"
#include "elements.hpp"
#include "interactions.hpp"

namespace pyDEM {
	class Scene {
		public:
			Scene();
			void setAccField(vct acc);
			void addElem(Element &elem);
			void addInter(Interaction &inter);
			std::vector<Element *> elements;
			std::vector<Interaction *> interactions;
			vct acc_field;
	};
}

#endif