# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import vtk



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pyDEM
else:
    import _pyDEM

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyDEM.delete_SwigPyIterator

    def value(self):
        return _pyDEM.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pyDEM.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pyDEM.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pyDEM.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pyDEM.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pyDEM.SwigPyIterator_copy(self)

    def next(self):
        return _pyDEM.SwigPyIterator_next(self)

    def __next__(self):
        return _pyDEM.SwigPyIterator___next__(self)

    def previous(self):
        return _pyDEM.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pyDEM.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pyDEM.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pyDEM.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pyDEM.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pyDEM.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pyDEM.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pyDEM.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pyDEM:
_pyDEM.SwigPyIterator_swigregister(SwigPyIterator)

class Material(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    density = property(_pyDEM.Material_density_get, _pyDEM.Material_density_set)

    def __init__(self, d):
        _pyDEM.Material_swiginit(self, _pyDEM.new_Material(d))
    __swig_destroy__ = _pyDEM.delete_Material

# Register Material in _pyDEM:
_pyDEM.Material_swigregister(Material)

class Rigid(Material):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, d):
        _pyDEM.Rigid_swiginit(self, _pyDEM.new_Rigid(d))
    __swig_destroy__ = _pyDEM.delete_Rigid

# Register Rigid in _pyDEM:
_pyDEM.Rigid_swigregister(Rigid)

class Element(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    area = property(_pyDEM.Element_area_get, _pyDEM.Element_area_set)
    group = property(_pyDEM.Element_group_get, _pyDEM.Element_group_set)
    type = property(_pyDEM.Element_type_get, _pyDEM.Element_type_set)

    def __init__(self, group, type, mat):
        _pyDEM.Element_swiginit(self, _pyDEM.new_Element(group, type, mat))

    def setInit(self, V, F):
        return _pyDEM.Element_setInit(self, V, F)

    def applyF(self, F):
        return _pyDEM.Element_applyF(self, F)

    def move(self, dt, acc_f, disp=0.1):
        return _pyDEM.Element_move(self, dt, acc_f, disp)

    def aabb(self):
        return _pyDEM.Element_aabb(self)
    material = property(_pyDEM.Element_material_get, _pyDEM.Element_material_set)

    def updtMA(self, a):
        return _pyDEM.Element_updtMA(self, a)
    coords = property(_pyDEM.Element_coords_get, _pyDEM.Element_coords_set)
    velocities = property(_pyDEM.Element_velocities_get, _pyDEM.Element_velocities_set)
    forces = property(_pyDEM.Element_forces_get, _pyDEM.Element_forces_set)
    mass = property(_pyDEM.Element_mass_get, _pyDEM.Element_mass_set)

    def view(self, i=0):
        return _pyDEM.Element_view(self, i)

    def _set_vtk(self, source):
    	self.mapper = vtk.vtkPolyDataMapper()
    	self.mapper.SetInputConnection(source.GetOutputPort())
    	self.actor = vtk.vtkActor()
    	self.actor.SetMapper(self.mapper)

    __swig_destroy__ = _pyDEM.delete_Element

# Register Element in _pyDEM:
_pyDEM.Element_swigregister(Element)

class Circle(Element):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    center = property(_pyDEM.Circle_center_get, _pyDEM.Circle_center_set)
    radius = property(_pyDEM.Circle_radius_get, _pyDEM.Circle_radius_set)

    def __init__(self, *args):
        _pyDEM.Circle_swiginit(self, _pyDEM.new_Circle(*args))

        print("_set_vtk configuração dos atores")
        print(args[1])
        self.disk = vtk.vtkRegularPolygonSource()
        self.disk.SetNumberOfSides(50)
        self.disk.SetRadius(args[1])
        self._set_vtk(self.disk)




    def move(self, dt, acc_f, disp=0.1):
        return _pyDEM.Circle_move(self, dt, acc_f, disp)

    def aabb(self):
        return _pyDEM.Circle_aabb(self)
    __swig_destroy__ = _pyDEM.delete_Circle

# Register Circle in _pyDEM:
_pyDEM.Circle_swigregister(Circle)

class Wall(Element):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _pyDEM.Wall_swiginit(self, _pyDEM.new_Wall(*args))

        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1(self.p1 + [0])
        lineSource.SetPoint2(self.p2 + [0])
        self._set_vtk(lineSource)




    def aabb(self):
        return _pyDEM.Wall_aabb(self)
    p1 = property(_pyDEM.Wall_p1_get, _pyDEM.Wall_p1_set)
    p2 = property(_pyDEM.Wall_p2_get, _pyDEM.Wall_p2_set)
    C = property(_pyDEM.Wall_C_get, _pyDEM.Wall_C_set)
    normal = property(_pyDEM.Wall_normal_get, _pyDEM.Wall_normal_set)
    eq = property(_pyDEM.Wall_eq_get, _pyDEM.Wall_eq_set)
    length = property(_pyDEM.Wall_length_get, _pyDEM.Wall_length_set)
    __swig_destroy__ = _pyDEM.delete_Wall

# Register Wall in _pyDEM:
_pyDEM.Wall_swigregister(Wall)

class Law(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    k = property(_pyDEM.Law_k_get, _pyDEM.Law_k_set)

    def calcF(self, elemA, elemB, gap):
        return _pyDEM.Law_calcF(self, elemA, elemB, gap)

    def __init__(self, k):
        _pyDEM.Law_swiginit(self, _pyDEM.new_Law(k))
    __swig_destroy__ = _pyDEM.delete_Law

# Register Law in _pyDEM:
_pyDEM.Law_swigregister(Law)

class LinearElastic(Law):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, k):
        _pyDEM.LinearElastic_swiginit(self, _pyDEM.new_LinearElastic(k))

    def calcF(self, elemA, elemB, gap):
        return _pyDEM.LinearElastic_calcF(self, elemA, elemB, gap)
    __swig_destroy__ = _pyDEM.delete_LinearElastic

# Register LinearElastic in _pyDEM:
_pyDEM.LinearElastic_swigregister(LinearElastic)

class Interaction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    groupA = property(_pyDEM.Interaction_groupA_get, _pyDEM.Interaction_groupA_set)
    groupB = property(_pyDEM.Interaction_groupB_get, _pyDEM.Interaction_groupB_set)

    def verify(self, elemA, elemB):
        return _pyDEM.Interaction_verify(self, elemA, elemB)

    def getNormal(self, elemA, elemB):
        return _pyDEM.Interaction_getNormal(self, elemA, elemB)

    def applyF(self, elemA, elemB, N, F):
        return _pyDEM.Interaction_applyF(self, elemA, elemB, N, F)

    def __init__(self, ga, gb, law):
        _pyDEM.Interaction_swiginit(self, _pyDEM.new_Interaction(ga, gb, law))
    law = property(_pyDEM.Interaction_law_get, _pyDEM.Interaction_law_set)
    __swig_destroy__ = _pyDEM.delete_Interaction

# Register Interaction in _pyDEM:
_pyDEM.Interaction_swigregister(Interaction)

class Circle_Circle(Interaction):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, law):
        _pyDEM.Circle_Circle_swiginit(self, _pyDEM.new_Circle_Circle(law))

    def verify(self, elemA, elemB):
        return _pyDEM.Circle_Circle_verify(self, elemA, elemB)

    def getNormal(self, elemA, elemB):
        return _pyDEM.Circle_Circle_getNormal(self, elemA, elemB)

    def applyF(self, elemA, elemB, N, F):
        return _pyDEM.Circle_Circle_applyF(self, elemA, elemB, N, F)
    __swig_destroy__ = _pyDEM.delete_Circle_Circle

# Register Circle_Circle in _pyDEM:
_pyDEM.Circle_Circle_swigregister(Circle_Circle)

class Circle_Wall(Interaction):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, law):
        _pyDEM.Circle_Wall_swiginit(self, _pyDEM.new_Circle_Wall(law))

    def verify(self, *args):
        return _pyDEM.Circle_Wall_verify(self, *args)

    def getNormal(self, *args):
        return _pyDEM.Circle_Wall_getNormal(self, *args)

    def applyF(self, *args):
        return _pyDEM.Circle_Wall_applyF(self, *args)
    __swig_destroy__ = _pyDEM.delete_Circle_Wall

# Register Circle_Wall in _pyDEM:
_pyDEM.Circle_Wall_swigregister(Circle_Wall)

class Scene(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _pyDEM.Scene_swiginit(self, _pyDEM.new_Scene())

        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground((.1, .2, .4))




    def setAccField(self, acc):
        return _pyDEM.Scene_setAccField(self, acc)

    def addElem(self, elem):
        val = _pyDEM.Scene_addElem(self, elem)

        self.ren.AddActor(elem.actor)


        return val


    def addInter(self, inter):
        return _pyDEM.Scene_addInter(self, inter)
    elements = property(_pyDEM.Scene_elements_get, _pyDEM.Scene_elements_set)
    interactions = property(_pyDEM.Scene_interactions_get, _pyDEM.Scene_interactions_set)
    acc_field = property(_pyDEM.Scene_acc_field_get, _pyDEM.Scene_acc_field_set)

    def show(self):
    	"""
    	Renderiza a cena numa janela interativa.
    	"""
    	self._configRen()  
    	self._startRen()        

    def _configRen(self):
    	"""
    	Configura o VTK para renderizar a cena
    	"""
    # janela de rendericação
    	self.renWin = vtk.vtkRenderWindow()
    	self.renWin.AddRenderer(self.ren)
    	self.renWin.SetSize(600, 600)
    # interação mouse-janela
    	self.iren = vtk.vtkRenderWindowInteractor()
    	self.iren.SetRenderWindow(self.renWin)
    # estilo de visualização de imagem 
    # scroll da zoom, e arrastar com scroll move a cena
    	self.iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())
    	self.iren.AddObserver('ExitEvent', self.hide)
    	self.iren.Initialize()

    def _startRen(self):
    	"""
    	Abre a janela de renderização
    	"""
    	self.renWin.Render()
    	self.iren.Start()

    def hide(self, iren = None, event = None):
    	"""
    	Fecha a janela
    	"""
    	self.renWin.Finalize()
    	self.iren.TerminateApp()
    	del self.renWin, self.iren

    __swig_destroy__ = _pyDEM.delete_Scene

# Register Scene in _pyDEM:
_pyDEM.Scene_swigregister(Scene)

class Contact(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    elemA = property(_pyDEM.Contact_elemA_get, _pyDEM.Contact_elemA_set)
    elemB = property(_pyDEM.Contact_elemB_get, _pyDEM.Contact_elemB_set)
    inter = property(_pyDEM.Contact_inter_get, _pyDEM.Contact_inter_set)
    gap = property(_pyDEM.Contact_gap_get, _pyDEM.Contact_gap_set)

    def __init__(self, elemA, elemB, inter):
        _pyDEM.Contact_swiginit(self, _pyDEM.new_Contact(elemA, elemB, inter))

    def verify(self):
        return _pyDEM.Contact_verify(self)

    def applyF(self):
        return _pyDEM.Contact_applyF(self)
    __swig_destroy__ = _pyDEM.delete_Contact

# Register Contact in _pyDEM:
_pyDEM.Contact_swigregister(Contact)

class candidate(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    pos = property(_pyDEM.candidate_pos_get, _pyDEM.candidate_pos_set)
    type = property(_pyDEM.candidate_type_get, _pyDEM.candidate_type_set)
    ref = property(_pyDEM.candidate_ref_get, _pyDEM.candidate_ref_set)
    included = property(_pyDEM.candidate_included_get, _pyDEM.candidate_included_set)

    def __init__(self):
        _pyDEM.candidate_swiginit(self, _pyDEM.new_candidate())
    __swig_destroy__ = _pyDEM.delete_candidate

# Register candidate in _pyDEM:
_pyDEM.candidate_swigregister(candidate)

class Simulation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    scene = property(_pyDEM.Simulation_scene_get, _pyDEM.Simulation_scene_set)
    N = property(_pyDEM.Simulation_N_get, _pyDEM.Simulation_N_set)
    step = property(_pyDEM.Simulation_step_get, _pyDEM.Simulation_step_set)
    dt = property(_pyDEM.Simulation_dt_get, _pyDEM.Simulation_dt_set)

    def __init__(self, scene, steps, dt=1e-3):
        _pyDEM.Simulation_swiginit(self, _pyDEM.new_Simulation(scene, steps, dt))

    def calculate(self):
        return _pyDEM.Simulation_calculate(self)

    def _step(self):
        return _pyDEM.Simulation__step(self)

    def _init_detec(self):
        return _pyDEM.Simulation__init_detec(self)

    def _dect_inter(self, elA, elB):
        return _pyDEM.Simulation__dect_inter(self, elA, elB)

    def _fine_detec(self):
        return _pyDEM.Simulation__fine_detec(self)

    def _calcF(self):
        return _pyDEM.Simulation__calcF(self)

    def _upd_move(self):
        return _pyDEM.Simulation__upd_move(self)
    __swig_destroy__ = _pyDEM.delete_Simulation

# Register Simulation in _pyDEM:
_pyDEM.Simulation_swigregister(Simulation)



