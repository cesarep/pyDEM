#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Gerados de Cenas

@author: César Eduardo Petersen

"""

import vtk
import math

class Cena:
    """
    Classe para construção de cenas.
    Inclui
    """
    
    def __init__(self, nome = ''):
        """
        Construtor da classe Cena. Configura o VTK para renderizaçao.

        Args:
            nome (string): Opcional, nomeia a cena.

        """
        # Setup inicial VTK
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground((.102, .2, .4))
        self.renWin = vtk.vtkRenderWindow()
        self.renWin.AddRenderer(self.ren)
        self.renWin.SetSize(600, 600)
        self.renWin.SetWindowName(nome)
        self.iren = vtk.vtkRenderWindowInteractor()
        self.iren.SetRenderWindow(self.renWin)
        self.style = vtk.vtkInteractorStyleImage()
        self.iren.SetInteractorStyle(self.style)
        
    def addElem(self, elem):
        """
        Adiciona elemento à cena.

        Args:
            elem (Elemento): Objeto de tipo Elemento.
            
        """
        self.ren.AddActor(elem.actor)
           
    def show(self):
        """
        Renderiza a cena numa janela interativa.
        """
        self.iren.Initialize()
        self.renWin.Render()
        self.iren.Start()

# --------------------------------- MATERIAIS -------------------------------- #

class Material:
    """
    Classe para Materiais
    """
    pass
    
class Rigido(Material):
    """
    Subclasse para Materiais do tipo Rígido.
    Tem como parametros apenas a densidade de massa por unidade de área.
    """
    def __init__(self, densidade):
        """
        Construtor da classe Rigido.

        Args:
            densidade (float): Densidade de massa por unidade de área.

        """
        self.den = densidade
        
# --------------------------------- ELEMENTOS -------------------------------- #

class Elemento:
    """
    Classe para Elementos
    """
    def _set_vtk(self, source):
        """
        Configuração inicial do mapper e actor para utilização no VTK.

        Args:
            source (vtkLineSource): objeto do VTK fonte da geometria.

        """
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(source.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)


class Esfera(Elemento):
    """
    Subclasse para Elemento do tipo Esfera.
    """
    def __init__(self, raio, centro, material = None):
        self._tipo = "Esfera"
        self.r = raio
        self.centro = centro
        self.mat = material
        self.area = math.pi*raio**2
        #self.massa = self.mat.massa(self.area)
        
        #vtk
        self.disk = vtk.vtkRegularPolygonSource()
        self.disk.SetNumberOfSides(50)
        self.disk.SetRadius(raio)
        self.disk.SetCenter(centro[0], centro[1], 0)
        
        self._set_vtk(self.disk)
        
        #self.actor.SetPosition( v[0], centro[1], 0)
        self.actor.GetProperty().SetColor((1,1,1))
        
class Linha(Elemento):
    """
    Subclasse para Elemento do tipo Linha
    """
    def __init__(self, p1, p2):
        """
        Construtor da classe Linha.

        Args:
            p1 (int[]): vetor com as posições [x,y] iniciais.
            p2 (int[]): vetor com as posições [x,y] finais.

        """
        self._tipo = "Linha"
        self.p1 = p1[:] + (0,0,0)[2:3]
        self.p2 = p2[:] + (0,0,0)[2:3]
        
        #vtk
        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1(self.p1)
        lineSource.SetPoint2(self.p2)
        
        self._set_vtk(lineSource)
        self.actor.GetProperty().SetColor((.5,.5,.5))

