## EQUIPE ##
# Claro Henrique
# Letícia Saraiva

from estado import *
from random import randint
from random import random


class TemperaSimulada:
    def __init__(self,e_0,t_0=12, d_t=1):
        self.t = t_0 #define a temperatura inicial
        self.e = e_0 #defineo estado inicial
        self.euler = 2.718281828459045235360287 #define numero de euler
        self.d_t = d_t #define o decremento(por padrao 1)
    
    def probability_to_move(self,delta,temperatura):
        #funcao que calcula a probabilidade de escolher o vizinho
        if delta < 0:
            return 1 #se o estado vizinho e melhor a chance deve ser 100%
        else:
            return self.euler**(-delta/temperatura) #criterio de aceitacao de Botzmann
            
    
    def solve(self):
        #algoritmo tempera simulada
        while(self.t > 0): #executa enquanto a temperatura for positiva
            e_viz = sucessor_aleatorio(self.e)  #gera um vizinho aleatorio
            delta_energy = avaliacao(e_viz) - avaliacao(self.e)  #calcula a variacao de energia
            prob = self.probability_to_move(delta_energy,self.t)
            
            was_choosen = False    #flag que indica se o estado vizinho foi escolhido
            if prob >= random():  #verifica se deve alterar o estado
                self.e = e_viz   #atualiza o estado atual
                was_choosen = True
            self.t -= self.d_t  #atualiza temperatura

            print('energia atual:', avaliacao(self.e), ',   energia vizinho:', avaliacao(e_viz))
            print('variacao de energia:', delta_energy, ',   probabilidade: ', prob, ',   foi escolhido? ', was_choosen)
            imprime_estado(e_viz)
            print()
        return self.e #retorna o estado encontrado    