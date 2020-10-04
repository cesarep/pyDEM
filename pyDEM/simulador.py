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
    def __init__(self, elemA, elemB, inter):
        """
        Construtor da classe Contato. Chamada 

        Args:
            elemA, elemB (Elemento): Par de elementos em contato
            inter (Interacao): Tipo de interação entre os elementos.

        """
        self.ElA = elemA
        self.ElB = elemB
        self.inter = inter
    
    def verifica(self):
        """
        Verifica se os dois elementos realmente estão contatando

        Returns:
            True|False se o contato ocorre ou nao.

        """
        self.inter.verifica(self.ElA, self.ElB)


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
        
        
    def calcular(self):
        """
        Realiza o ciclo de calculo
        """
        for i in range(0, self.N):
            pass

        
    def dect_grossa(self):
        """
        Realiza a detecção simplificada de possiveis contatos, antes da 
        detecção detalhada: 

        """
        pre_contatos = []
        
        self.dect_fina(pre_contatos)
        
        
    def dect_fina(self, pre_contatos):
        """
        Realiza a detecção fina dos contatos
        """
        
        contatos = []
        
        self.calc_F_contatos(contatos)
        
        
    def calc_F_contatos(self, contatos):
        """
        Atualiza a força nos contatos

        """
        
        forcas = []
        
        
    def updt_movimento(self, forcas):
        """
        Movimenta os elementos
        """
        
        
    
    
        
        
        