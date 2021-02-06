%typemap(out) vct{
  $result = PyList_New($1.size());
  for (size_t i = 0; i < $1.size(); i++) {
    PyObject *o = PyFloat_FromDouble((double) $1[i]);
    PyList_SetItem($result, i, o);
  }
}

%typecheck(SWIG_TYPECHECK_DOUBLE_ARRAY) vct {
  $1 = PySequence_Check($input) ? 1 : 0;
}

%typemap(in) vct (vct temp){
  if (!PySequence_Check($input)) {
    PyErr_SetString(PyExc_TypeError, "Expecting a sequence");
    SWIG_fail;
  }
  size_t l = PySequence_Length($input);
  temp.resize(l);
  for (size_t i = 0; i < l; i++) {
    PyObject *o = PySequence_GetItem($input, i);
    if (PyNumber_Check(o)) {
      temp[i] = (double) PyFloat_AsDouble(o);
    } else {
      PyErr_SetString(PyExc_ValueError, "Sequence elements must be numbers");      
      SWIG_fail;
    }
  }
  $1 = temp;
}