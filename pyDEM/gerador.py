#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Gerados de Cenas

@author: César Eduardo Petersen

"""

import vtk, math

class Cena:
    """
    Classe para construção de cenas.
    Inclui a configuração inicial para renderização pelo VTK
    """
    
    def __init__(self, nome = ''):
        """
        Construtor da classe Cena. Configura o VTK para renderização.

        Args:
            nome (string): Opcional, nomeia a cena.

        """
        
        self.elementos = []
        self.interacao = []
        
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
        
    def addElem(self, elementos):
        """
        Adiciona elementos à cena e ao renderizador VTK.

        Args:
            elem (Elemento[]): Um ou mais elementos a serem acrescentados.
            
        """
        # se entrar com lista de objetos, intear, se nao adicionar diretamente
        if isinstance(elementos, (tuple, list)):
            for elem in elementos:
                self.ren.AddActor(elem.actor)
                self.elementos.append(elem)
        else:
            self.ren.AddActor(elementos.actor)
            self.elementos.append(elementos)
            
    def addInter(self, interacao):
        """
        Adiciona Interações à cena.

        Args:
            interacao (Interacao[]): Uma ou mais Interações a serem acrescentadas.

        """
        if isinstance(interacao, (tuple, list)):
            for inter in interacao:
                self.interacao.append(inter)
        else:
            self.interacao.append(interacao)
            
            
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
    Classe base para Materiais
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

# TODO: Passar a cor do elemento como parametro

class Elemento:
    """
    Classe base para Elementos
    """
    def __init__(self, grupo):
        """
        Construtor da classe Elemento.
        Define um grupo para o elemento.

        Args:
            grupo (string): O grupo do elemento.

        """
        self.grupo = grupo
        self.v0 = [0,0]
        self.F0 = [0,0]
        self.vt = lambda t: [0,0]
        self.Ft = lambda t: [0,0]
        
        
    def _set_vtk(self, source, color):
        """
        Configuração inicial do mapper, actor e cor para utilização no VTK.

        Args:
            source (vtkLineSource): objeto do VTK fonte da geometria.
            color (int[3]): tupla as componentes RBG 0-255.

        """
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(source.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        
        self.actor.GetProperty().SetColor(tuple(cor/256 for cor in color))


    def CondInicial(self, vel = [0,0], forca = [0,0]):
        """
        Define a velocidade e/ou forca iniciais do Elemento.

        Args:
            vel (float[]): vetor com a velocidade inicial do corpo [x,y].
            forca (float[]): vetor com a força inicial do corpo [x,y.]

        """
        self.v0 = vel
        self.F0 = forca
        
    
    def CondConst(self, vel = lambda t: [0,0], forca = lambda t: [0,0]):
        """
        Defina a velocidade ou Força em um elemento ao longo da simulação.
        Pode ser uma função de t ou valor constante.

        Args:
            vel (function(t) | float[2]): Função ou vetor com velocidade do Elemento.
            forca (function(t) | float[2]): Função ou vetor com força do Elemento.

        """
        if(isinstance(vel, list)):
            vel = lambda t: vel
        if(isinstance(forca, list)):
            forca = lambda t: forca
        self.vt = vel
        self.Ft = forca
        

class Disco(Elemento):
    """
    Subclasse para Elemento do tipo Disco.
    """
    def __init__(self, raio, centro, material, grupo = "disco", cor = (255, 255, 255)):
        """
        Construtor da classe Disco.

        Args:
            raio (float): raio do disco.
            centro (float[2]): tupla da posição (x,y) do centro do disco.
            material (Material): Material do disco.
            grupo (string): Grupo desse elemento. Padrão "disco".
            cor (int[3]): tupla as 3 componentes RBG 0-255 para cor do elemento.

        """
        Elemento.__init__(self, grupo)
        self._tipo = "Disco"
        self.r = raio
        self.centro = centro
        self.mat = material
        self.area = math.pi*raio**2
        self.massa = self.mat.den * self.area
        
        #vtk
        self.disk = vtk.vtkRegularPolygonSource()
        self.disk.SetNumberOfSides(50)
        self.disk.SetRadius(raio)
        self.disk.SetCenter(centro[0], centro[1], 0)
        
        self._set_vtk(self.disk, cor)
        
class Parede(Elemento):
    """
    Subclasse para Elemento do tipo Parede
    """
    def __init__(self, p1, p2, grupo = "parede", cor = (128, 128, 128)):
        """
        Construtor da classe Parede.

        Args:
            p1 (int[2]): tupla com as posições [x,y] iniciais.
            p2 (int[2]): tupla com as posições [x,y] finais.
            grupo (string): Grupo desse elemento. Padrão "parede".
            cor (int[3]): tupla as 3 componentes RBG 0-255 para cor do elemento.

        """
        Elemento.__init__(self, grupo)
        self._tipo = "Parede"
        self.p1 = p1[:] + (0,0,0)[2:3]
        self.p2 = p2[:] + (0,0,0)[2:3]
        
        self.C  = tuple((a + b)/2 for a,b in zip(p1,p2))[:] + (0,0,0)[2:3] 
        
        #vtk
        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1(self.p1)
        lineSource.SetPoint2(self.p2)
        
        self._set_vtk(lineSource, cor)


# --------------------------------- INTERAÇÃO -------------------------------- #

class Interacao:
    """
    Classe base para Interação entre elementos
    """
    def __init__(self, grupo, grupo2):
        self.grupo = grupo
        self.grupo2 = grupo2


        
        
class Disco_Disco(Interacao):
    """
    Subclasse para Interação entre Discos
    """
    def verifica(self, elA, elB):
        """
        Verifica o contato entre dois elementos.

        Args:
            elA, elB (Elemento): Par de elementos testados.

        Returns:
            True|False se o contato ocorre ou nao.

        """
        xa, ya = elA.pos
        ra = elA.raio
        xb, yb = elB.pos
        rb = elB.raio
        d = math.sqrt( (xa-xb)**2 + (ya-yb)**2 )
        return True if d <= ra+rb else False
        
class Disco_Disco_k(Disco_Disco):
    """
    Subclasse para Interação entre Discos pela lei de Hooke.
    """
    def __init__(self, k, grupo = "disco", grupo2 = 'disco'):
        """
        Construtor da classe Disco_Disco.

        Args:
            k (float): coef rigidez do contato.
            grupo (string): Nome do grupo de elementos candidatos, padrão "disco".
            grupo2 (string): Nome de grupo antagonista, padrão "disco".

        """
        self.k = k
        Interacao.__init__(self, grupo, grupo2)




class Disco_Parede(Interacao):
    """
    Subclasse para Interação entre Disco e Parede
    """
    def verifica(self, elA, elB):
        """
        Verifica o contato entre dois elementos.

        Args:
            elA, elB (Elemento): Par de elementos testados.

        Returns:
            True|False se o contato ocorre ou nao.

        """
        # distancia ponto-reta
        
class Disco_Parede_k(Disco_Parede):
    """
    Subclasse para Interacao entre Disco e Parede pela lei de Hooke.
    """
    def __init(self, k, grupo = 'disco', grupo2 = 'parede'):
        """
        Construtor da classe Disco_Parede.

        Args:
            k (float): coef rigidez do contato.
            grupo (string): Nome do grupo de elementos candidatos, padrão "disco".
            grupo2 (string): Nome de grupo antagonista, padrão "parede".

        """
        self.k = k
        Interacao.__init__(self, grupo, grupo2)
    