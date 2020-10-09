#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Simulador

@author: César Eduardo Petersen

"""

import math, numpy as np, sys
import matplotlib.pyplot as plt

class Contato:
    """
    Classe para os contatos
    """
    def __init__(self, elemA, elemB, inter):
        """
        Construtor da classe Contato.

        Args:
            elemA, elemB (Elemento): Par de elementos em contato.
            inter (Interacao): O tipo de interacao entre os elementos.

        """
        self.elemA = elemA
        self.elemB = elemB
        self.inter = inter
    
    def verifica(self):
        """
        Verifica se os dois elementos realmente estão contatando

        Returns:
            True|False se o contato ocorre ou nao.

        """
        self.gap = self.inter.verifica(self.elemA, self.elemB)
        
    def aplicaForca(self):
        """
        Se o contato passou na verifição fina, ento calcula e aplica as forças nos elementos
        """
        if(self.gap):
            na, nb = self.inter.normal(self.elemA, self.elemB)
            F = self.inter.lei.calcForca(self.elemA, self.elemB, self.gap)
            self.elemA.aplicaF(F*na)
            self.elemB.aplicaF(F*nb)


class Simulacao:
    """
    Classe para simulação
    """
    def __init__(self, cena, passos, dt = 1e-3, diss = 0.1):
        """
        Construtor da classe Simulação.

        Args:
            cena (Cena): Cena a ser simulada.
            passos (int): Número de passos.
            dt (float): Incremento de Tempo. padrão 1e-3.
            diss (float): Parametro de dissipação de energia entre 0-1. padrão 0.1.

        """
        self.cena = cena
        self.elementos = cena.elementos
        self.interacoes = cena.interacao
        self.N = passos
        self.passo = 0
        self.diss = diss

        # incremento de tempo critico
        mmn = min(self.elementos, key = lambda i: i.massa).massa # menor massa
        kmx = max(self.interacoes, key= lambda i: i.lei.k).lei.k # maior rigidez
        self.dtc = 2*math.sqrt(mmn/kmx)
        
        if(dt > self.dtc):
            #raise ValueError('O incremento de tempo maior que o crtico! defina um dt menor que %g' % self.dtc)
            print('incremento maior que crítico')
        else:
            self.dt = dt
        
    def calcular(self):
        """
        Realiza o ciclo de calculo
        """
        for i in range(0, self.N+1):
            self.passo = i
            prog = i/self.N
            #print('step ', i)
            # imprime barra de progresso
            sys.stdout.write('\r[%-50s] %d/%d' % ( "#"*int(50*prog) , i, self.N))
            self.step()
        
        
        
    def step(self):
        """
        Executa um passo da simulação
        """
        self._dect_grossa()
        self._dect_final()
        self._calc_F_contatos()
        self._updt_movimento()
                
    
    def _dect_grossa(self):        
        """
        Realiza a detecção simplificada de possiveis contatos e cria objetos
        do tipo Contato para todos os possiveis pares.
        Método sweep and prune: transversa todos os elementos no eixo X
        marcando o inicio e fim das caixas de contorno (aabb).
        Ordena a lista marcando todas os possiveis cruzamentos
        e então faz a eliminação final pelo eixo Y criando os objetos de contato
        """
        
        self.contatos = []
    
        eixoX = []
        for elem in self.elementos:
            eixoX.append({'x': elem.aabb()['x'][0],   # coord
                          't': 'i',                 # inicio
                          'e': elem})               # elemento
            
            eixoX.append({'x': elem.aabb()['x'][1],   # coord
                          't': 'f',                 # fim
                          'e': elem})               # elemento
        
        eixoX.sort(key = lambda i: i['x'])
        
        candidatos = []
        
        for i in range(0, len(eixoX)):
            if( eixoX[i]['t'] == 'i'): # se for elemento de inicio
                ref = id(eixoX[i]['e']) # ref para elemento de parada
                j = i + 1
                # candidatos
                c = 0
                # enquanto nao chega no elemento de parada 
                while(id(eixoX[j]['e']) != ref):
                    # se algum elemento iniciar
                    if(eixoX[j]['t'] == 'i'):
                        # acrescenta à lista de candidatos
                        candidatos.append(eixoX[j]['e'])  
                        c += 1
                    j += 1
                # se algum candidato foi acrescentado, entao adiciona também este objeto
                if c > 0:
                    candidatos.append(eixoX[i]['e'])  
                        
        eixoY = []
                
        for elem in candidatos:
            eixoY.append({'y': elem.aabb()['y'][0],   # coord
                          't': 'i',                 # inicio
                          'e': elem})               # elemento
            
            eixoY.append({'y': elem.aabb()['y'][1],   # coord
                          't': 'f',                 # fim
                          'e': elem})               # elemento
        
        eixoY.sort(key = lambda i: i['y'])
        
        for i in range(0, len(eixoY)):
            if( eixoY[i]['t'] == 'i'): # se for elemento de inicio
                ref = id(eixoY[i]['e']) # ref para elemento de parada
                j = i + 1
                # enquanto nao chega no elemento de parada 
                while(id(eixoY[j]['e']) != ref):
                    # se algum elemento iniciar
                    if(eixoY[j]['t'] == 'i'):
                        # detecta a interacao entre os elementos
                        try:
                            inter = self._dect_inter(eixoY[i]['e'], eixoY[j]['e'])
                            # acrescenta lista de contatos
                            self.contatos.append(Contato(eixoY[i]['e'], eixoY[j]['e'], inter))
                        except IndexError:
                            print('\n Contato nao suportado: %s x %s' % (eixoY[i]['e'].grupo, eixoY[j]['e'].grupo))
                    j += 1
                            
        
    def _dect_inter(self, elemA, elemB):
        """
        Detecta qual a interação entre um par de elementos.
        
        Args:
            elemA, elemB (Elemento): Par de elementos.

        Returns:
            Interacao para o par de elementos.

        """
        grupos = sorted([elemA.grupo, elemB.grupo])
        
        # seleciona a interação que corresponde aos grupos do par de elementos
        return [inter for inter in self.interacoes if inter.grupos == grupos][0]
        
        
    def _dect_final(self):
        """
        Faz a verifição fina entre todos os pares de contatos.
        """
        for cont in self.contatos:
            cont.verifica()
        
    def _calc_F_contatos(self):
        """
        Atualiza a força nos elementos para os pares em contato.
        """
        for cont in self.contatos:
            cont.aplicaForca()
        
        
    def _updt_movimento(self):
        """
        Movimenta os elementos.
        """
        for elem in self.elementos:
            elem.atualizaMov(self.passo*self.dt, self.dt, self.cena.campoA, self.diss)
            
            
    def anim(self, pps = 50):
        """
        Anima a simulação

        Args:
            pps (float): passos por segundo para a animação, padrão 50.

        """            
        self.cena._configRen()
        self.cena.iren.AddObserver('TimerEvent', self._anim_step)
        self.cena.iren.CreateRepeatingTimer(pps)
        self._anim_step = 0
        self.cena._startRen()
        
    def _anim_step(self, iren, event):
        """
        Atualiza a posição dos elementos na janela de renderização

        Args:
            iren (vtkXRenderWindowInteractor): Interação do VTK
            event (TimerEvent): evento do timer

        """
        for elem in self.elementos:
            elem.vtk_anim(self._anim_step)
        self.cena.renWin.Render()
        self._anim_step = 0 if self._anim_step == self.N-1 else self._anim_step + 1
        
    def energiaCinetica(self):
        """
        Plota o gráfico da energia cinética total do sistema ao longo do tempo.

        """
        K = np.zeros(self.N+1)
        for elem in self.elementos:
            #print(elem.enerK())
            K += elem.energia()
        
        t = np.linspace(0, self.N*self.dt, self.N+1)
        
        plt.plot(t, K, label='Energia Cinética')
        plt.xlabel('t')
        plt.ylabel('K')
        plt.title('Evolução da energia cinética no tempo')
    
    
        
        
        