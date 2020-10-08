#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Gerados de Cenas

@author: César Eduardo Petersen

"""

import vtk, math, numpy as np

class Cena:
    """
    Classe para construção de cenas.
    Inclui a configuração inicial para renderização pelo VTK
    """
    
    def __init__(self, nome = '', campoA = np.zeros(2)):
        """
        Construtor da classe Cena. Configura o VTK para renderização.

        Args:
            nome (string): Opcional, nomeia a cena.

        """
        
        self.elementos = []
        self.interacao = []
        self.nome = nome
        self.campoA = campoA
        
        # Setup inicial VTK
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground((.1, .2, .4))
        
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
            
    def addCampoAcel(self, a):
        """
        Adiciona um campo de aceleração para a cena.

        Args:
            a (float[2]): Vetor de aceleração na cena. Ex: gravidade = [0, -9.81]

        """
        self.campoA  = np.array(a)
            
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
        self.renWin.SetWindowName(self.nome)
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
        self.v0 = np.zeros(2)
        self.F0 = np.zeros(2)
        self.vt = lambda t: np.zeros(2)
        self.Ft = lambda t: np.zeros(2)
        self.massa = float('nan')
        
        
    def atualizaMov(self, *args):
        pass
    
    def aplicaF(self, *args):
        pass
    
    def vtk_anim(self, step):
        pass
        

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


    def CondInicial(self, vel = [0.,0.], forca = [0.,0.]):
        """
        Define a velocidade e/ou forca iniciais do Elemento.

        Args:
            vel (float[]): vetor com a velocidade inicial do corpo [x,y].
            forca (float[]): vetor com a força inicial do corpo [x,y.]

        """
        self.v0 = np.array(vel, dtype='float64')
        self.F0 = np.array(forca)
        self.movimento['vel'][0] = self.v0
        self.movimento['F'][0] = self.F0
        
    
    def CondConst(self, vel = lambda t: [0.,0.], forca = lambda t: [0.,0.]):
        """
        Defina a velocidade ou Força em um elemento ao longo da simulação.
        Pode ser uma função de t ou valor constante.

        Args:
            vel (function(t) | float[2]): Função ou vetor com velocidade do Elemento.
            forca (function(t) | float[2]): Função ou vetor com força do Elemento.

        """
        if(isinstance(vel, list)):
            vel = lambda t: np.array(vel)
        if(isinstance(forca, list)):
            forca = lambda t: np.array(forca)
        self.vt = np.vectorize(vel)
        self.Ft = np.vectorize(forca)
        

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
        self.raio = raio
        self.centro = np.array(centro)
        self.mat = material
        self.area = math.pi*raio**2
        self.massa = self.mat.den * self.area
        
        # lista de todas as variaveis do elemento ao decorrer da simulação, pos, vel...
        self.movimento = {'pos': [centro], 'vel': [self.v0], 'F': [self.F0]}
        
        # config para VTK
        self.disk = vtk.vtkRegularPolygonSource()
        self.disk.SetNumberOfSides(50)
        self.disk.SetRadius(raio)
        #self.disk.SetCenter(centro[0], centro[1], 0)
        self._set_vtk(self.disk, cor)
        self.actor.SetPosition(centro[0], centro[1], 0)
        
    def aabb(self):
        """
        Retorna a caixa de contorno do elemento, axis-aligned bounding box
        """
        c = self.pos()
        r = self.raio
        return {'x': [c[0]-r, c[0]+r],
                'y': [c[1]-r, c[1]+r]}
    
    def pos(self):
        """
        Retorna um vetor com a ultima posição do elemento
        """
        return np.array(self.movimento['pos'][-1])
    
    def aplicaF(self, F):
        """
        Aplica um vetor de forças no corpo

        Args:
            F (float[2]): vetor de forças.

        """
        self.movimento['F'][-1] += F
        
    def atualizaMov(self, t, dt, campoa):
        """
        Atualiza a posição do corpo
        
        Args:
            t (float): tempo atual na simulação.
            dt (float): incremento de tempo.
            campoa (float[2]): vetor de campo de aceleração da cena.
            
        """
        # aplica as condições de contorno
        self.movimento['vel'][-1] += self.vt(t)
        self.movimento['F'][-1] += self.Ft(t)
        
        # aceleração atual
        a  = self.movimento['F'][-1]/self.massa
        # aplica o campo de aceleração da cena
        a += campoa
        
        # proxima vel
        vn = self.movimento['vel'][-1] + a*dt
        self.movimento['vel'].append(vn)
        
        # proxima posicao
        pn = self.movimento['pos'][-1] + vn*dt
        self.movimento['pos'].append(pn)
        
        # proxima força
        self.movimento['F'].append(np.zeros(2))
        
    def vtk_anim(self, step):
        """
        Faz a animação para o VTK

        Args:
            step (int): passo atual.

        """
        pos = self.movimento['pos'][step]
        self.actor.SetPosition(pos[0], pos[1], 0)
    
        
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
        # transforma os vetores 2d em 3d com z=0 para utilização no VTK
        self.p1 = np.pad(p1, (0,1), 'constant')
        self.p2 = np.pad(p2, (0,1), 'constant')
        u = self.p2 - self.p1
        self.L = np.linalg.norm(u)
        
        N = np.array([-u[1], u[0]])

        self.eqreta = np.array([N[0], N[1], np.cross(p1, p2) ])
        self.normal = N
        
        print("eq reta: %.3fx %+.3fy %+.3f "% (self.eqreta[0], self.eqreta[1], self.eqreta[2]) )
        
        
        self.C  = (self.p1+self.p2)/2
        
        #vtk
        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1(self.p1)
        lineSource.SetPoint2(self.p2)
        
        self._set_vtk(lineSource, cor)
        
    def aabb(self, margin=0.1):
        """
        Retorna a caixa de contorno do elemento, axis-aligned bounding box
        """
        p1, p2 = self.p1, self.p2
        return {'x': [min(p1[0], p2[0])-margin*self.L, max(p1[0], p2[0])+margin*self.L], 
                'y': [min(p1[1], p2[1])-margin*self.L, max(p1[1], p2[1])+margin*self.L]}




# --------------------------------- INTERAÇÃO -------------------------------- #

class LeiContato:
    """
    Classe base para as Leis de Contato
    """
    pass

class LeiK(LeiContato):
    """
    Lei de Contato Simples com coeficiente de rigidez k
    """
    def __init__(self, k):
        """
        Construtor da classe LeiK. Toma como paremetro um coeficiente de rigidez k.

        Args:
            k (float): Coeficiente de rigizez em unidade de força/comprimento.

        """
        self.k = k
        
    def calcForca(self, elemA, elemB, gap):
        """
        Calcula, a partir do gap, a força atuante em em par de elementos

        Args:
            elemA, elemB (Elemento): Par de elementos.
            gap (float): gap do contato entre o par de elementos.
            
        Returns:
            float: magnitude da força do contato

        """
        return self.k*gap
    

class Interacao:
    """
    Classe base para Interação entre elementos
    """
    def __init__(self, lei, grupo, grupo2):
        self.lei = lei
        self.grupo = grupo
        self.grupo2 = grupo2
        self.grupos = sorted([grupo, grupo2])

        
class Disco_Disco(Interacao):
    """
    Subclasse para Interação entre Discos
    """
    def __init__(self, lei, grupo='disco', grupo2='disco'):
        """
        Construtor da classe Disco_Disco.

        Args:
            lei (LeiContato): Lei de Contato.
            grupo, grupo2 (string): Nome do grupo de elementos. Padrão 'disco'.

        """
        Interacao.__init__(self, lei, grupo, grupo2)
    
    def verifica(self, elemA, elemB):
        """
        Verifica o contato entre dois elementos.
        
        Retorna a caixa de contorno do elemento, axis-aligned bounding box
        Args:
            elemA, elemB (Elemento): Par de elementos testados.
 
        Returns:
            gap (float) entre os elementos ou False caso não esteja em contato.

        """
        ca = elemA.pos()
        ra = elemA.raio
        
        cb = elemB.pos()
        rb = elemB.raio
        
        d = np.linalg.norm(ca-cb)
        
        return d-ra-rb if d <= ra+rb else False
    
    def normal(self, elemA, elemB):
        """
        Retorna o vetor normal do contato

        Args:
            elemA, elemB (Elemento): Par de elementos.

        Returns:
            float[2][2]: vetores normais do par de elementos do contato.

        """
        ca = elemA.pos()
        cb = elemB.pos()
        d = np.linalg.norm(ca-cb)
        # vetor normal de A->B
        na = np.array(cb-ca)/d
        # vetor normal de B->A
        nb = -na
        return na, nb
    

class Disco_Parede(Interacao):
    """
    Subclasse para Interação entre Disco e Parede
    """
    def __init__(self, lei, grupo='disco', grupo2='parede'):
        """
        Construtor da classe Disco_Parede.

        Args:
            lei (LeiContato): Lei de Contato.
            grupo (string): Nome do grupo de elementos. Padrão 'disco'.
            grupo2 (string): Nome do grupo de elementos. Padrão 'parede'.

        """
        Interacao.__init__(self, lei, grupo, grupo2)
    
    def verifica(self, elemA, elemB):
        """
        Verifica o contato entre dois elementos.

        Args:
            elemA, elemB (Elemento): Par de elementos testados.

        Returns:
            gap (float) entre os elementos ou False caso não esteja em contato.

        """
        if elemA._tipo == "Parede":
            par, esf = elemA, elemB
        else:
            par, esf = elemB, elemA        
        
        eqreta = par.eqreta
        c = np.pad(esf.pos(), (0,1), 'constant', constant_values=1)
        r = esf.raio
        
        d = abs(np.dot(eqreta, c))/np.linalg.norm(par.normal)
        
        return d-r if d <= r else False
        
        
    def normal(self, elemA, elemB):
        """
        Retorna o vetor normal do contato

        Args:
            elemA, elemB (Elemento): Par de elementos.

        Returns:
            float[2][2]: vetores normais do par de elementos do contato.

        """
        if elemA._tipo == "Parede":
            par, esf = elemA, elemB
        else:
            par, esf = elemB, elemA
        
        eqreta = par.eqreta
        c = np.pad(esf.pos(), (0,1), 'constant', constant_values=1)
        
        d = np.dot(eqreta, c)
        # se d > 0 então o normal da parede aponta para a esfera        
        N = np.sign(d)*par.normal/np.linalg.norm(par.normal)
        
        print(N)
        
        if elemA._tipo == "Parede":
            return N, -N
        else:
            return -N, N

