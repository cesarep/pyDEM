#include "scene.hpp"

namespace pyDEM {
	Scene::Scene() :
		acc_field(vct0) { };

	void Scene::setAccField(vct acc) {
		acc_field = acc;
	};

	void Scene::addElem(Element &elem) {
		elements.push_back(&elem);
	};

	void Scene::addInter(Interaction &inter) {
		interactions.push_back(&inter);
	};
}