%module pyDEM
%include <std_string.i>
%include <std_vector.i>
%include "std_valarray.i"
%{
/* Includes the header in the wrapper code */
#include "../core/material.hpp"
#include "../core/elements.hpp"
#include "../core/laws.hpp"
#include "../core/interactions.hpp"
#include "../core/scene.hpp"
#include "../core/simulation.hpp"

%}

/* Parse the header file to generate wrappers */

%include "../core/material.hpp"
%include "../core/elements.hpp"
%include "../core/laws.hpp"
%include "../core/interactions.hpp"
%include "../core/scene.hpp"
%include "../core/simulation.hpp"
