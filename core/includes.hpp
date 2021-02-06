#ifndef INCLUDES_H
#define INCLUDES_H
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <valarray>
#define _USE_MATH_DEFINES
#include <cmath>

using vct = std::valarray<double>;
using vct2d = std::vector<vct>;
const vct vct0 = {0., 0.}; 

double norm(vct v);
double sgn(double x);
vct dir(vct v);

#endif