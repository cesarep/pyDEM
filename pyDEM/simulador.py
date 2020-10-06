#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Simulador

@author: César Eduardo Petersen

"""

import math, numpy


class Contato:
    """
    Classe para os contatos
    """
    def __init__(self, elemA, elemB):
        """
        Construtor da classe Contato.

        Args:
            elemA, elemB (Elemento): Par de elementos em contato.

        """
        self.ElA = elemA
        self.ElB = elemB
        #DETECTAR O TIPO DE CONTATO ENTRE os elementos
        #self.inter = inter
    
    def verifica(self):
        """
        Verifica se os dois elementos realmente estão contatando

        Returns:
            True|False se o contato ocorre ou nao.

        """
        self.inter.verifica(self.ElA, self.ElB)
        
    def aplicaForca(self):
        self.inter.aplicaForca(self.ElA, self.ElB)


class Simulacao:
    """
    Classe para simulação
    """
    def __init__(self, cena, passos, dt = 1e-3):
        """
        Construtor da classe Simulação.

        Args:
            cena (Cena): Cena a ser simulada.
            passos (int): Número de passos.
            dt (float): Incremento de Tempo. padrão 1e-3

        """
        self.cena = cena
        self.elementos = cena.elementos
        self.dt = dt
        self.N = passos
        self.passo = 0
        
    def calcular(self):
        """
        Realiza o ciclo de calculo
        """
        for i in range(0, self.N):
            self.passo = i
            self.step()
        
        
    def step(self):
        """
        Executa um passo da simulação
        """
        self.dect_grossa()
        self.dect_fina()
        self.calc_F_contatos()
        self.updt_movimento()
        
    
    def dect_grossa(self):        
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
            eixoX.append({'x': elem.aabb['x'][0],   # coord
                          't': 'i',                 # inicio
                          'e': elem})               # elemento
            
            eixoX.append({'x': elem.aabb['x'][1],   # coord
                          't': 'f',                 # fim
                          'e': elem})               # elemento
        
        eixoX.sort(key = lambda i: i['x'])
        
        candidatos = []
        
        for i in range(0, len(eixoX)):
            if( eixoX[i]['t'] == 'i'): # se for elemento de inicio
                ref = id(eixoX[i]['e']) # ref para elemento de parada
                j = i + 1
                # enquanto nao chega no elemento de parada 
                while(id(eixoX[j]['e']) != ref):
                    # se algum elemento iniciar
                    if(eixoX[j]['t'] == 'i'):
                        # acrescenta à lista de candidatos
                        candidatos.append(eixoX[j]['e'])  
                    j += 1
                        
        eixoY = []
        for elem in candidatos:
            eixoY.append({'y': elem.aabb['y'][0],   # coord
                          't': 'i',                 # inicio
                          'e': elem})               # elemento
            
            eixoY.append({'y': elem.aabb['y'][1],   # coord
                          't': 'f',                 # fim
                          'e': elem})               # elemento
        
        eixoY.sort(key = lambda i: i['y'])
                
        for i in range(0, len(eixoX)):
            if( eixoX[i]['t'] == 'i'): # se for elemento de inicio
                ref = id(eixoY[i]['e']) # ref para elemento de parada
                j = i + 1
                # enquanto nao chega no elemento de parada 
                while(id(eixoY[j]['e']) != ref):
                    # se algum elemento iniciar
                    if(eixoY[j]['t'] == 'i'):
                        # acrescenta à lista de contatos
                        self.contatos.append(Contato(eixoY[i]['e'], eixoY[j]['e']))
                    j += 1
        
        
    def dect_fina(self):
        """
        Faz a verificação fina entre todos os pares de contatos. 
        Remove os pares desnecessários
        """
        for cont in self.contatos:
            cont.verifica()

        
    def calc_F_contatos(self):
        """
        Atualiza a força nos contatos
        """
        for cont in self.contatos:
            cont.aplicaForca()
        
        
    def updt_movimento(self):
        """
        Movimenta os elementos
        """
        for elem in self.elementos:
            elem.atualizaMov()
        
    
    
        
        
        