## EQUIPE ##
# Claro Henrique
# Letícia Saraiva

from estado import *
from random import randint
from random import random




class AlgoritmoGenetico:
    def __init__(self,tam_populacao=40,qtd_geracoes=120,prob_mutacao=.05,porc_elitismo=.25):
        self.population_size = tam_populacao 
        self.generation_numb = qtd_geracoes
        self.prob_mutation = prob_mutacao
        self.porc_elitism= porc_elitismo
    
    def create_population(self):
        #gerar uma lista de estados (cromossomo) aleatórios
        return [gerar_estado_aleatorio() for i in range(self.population_size)]
    
    def fitness(self,e):
        #calcula o quao bem o cromossomo 'e' se adapta
        #quanto menor a penalidade, maior a fitness. por isso o valor retornado é negativo  
        return -avaliacao(e)
    
    def mutation(self, population):
        #aplica uma mutacao em todos os cromossomos da população
        for cromossomo in population:
            if random() <= self.prob_mutation:            #sorteia se cromossomo vai ser mutado
                i_aleatorio = randint(0,len(cromossomo)-1) #seleciona uma posicao aleatoria para alterar
                cromossomo[i_aleatorio] = (cromossomo[i_aleatorio] + 1)%2 #altera bit do cromossomo
    
    def selection(self, population):
        #seleciona os individuos que melhor se adaptam
        parents = []
        parents_size = int(self.population_size*self.porc_elitism) #calcula a quantidade de pais
        
        #criaremos uma lista de tuplas onde o primeiro elemento é o fitness e o segundo é o cromossomo
        #usaremos essa lista para ordenar e depois selecinar os melhores
        candidates = [(self.fitness(e),e) for e in population]
        candidates = sorted(candidates, reverse=True) #ordena de forma não-crescente em relação a fitness
        
        #selecionaremos os candidatos com maior fitness
        for i in range(0, parents_size):
            parents.append(candidates[i][1])
        
        #ao final, iremos embaralhar os possíveis pais, para aumentar a diversidade
        return parents
    
    def crossover(self, a, b):
        #funcao calcula o crossover entre dois cromossomos A e B
        #para isso, usaremos o 'crossover em dois pontos'

        parent2_start = randint(1,len(a)-1) #seleciona indice aleatorio para dividir os cromossomos
        if randint(0,1) == 1: #sorteia qual cromossomo vai dar o primeiro e segundo pedaço
            return a[0:parent2_start] + b[parent2_start:]
        else:
            return b[0:parent2_start] + a[parent2_start:]
    
    def imprime_geracao(self, g):
        #imprime todos os cromossomos da geracao g
        s = '-' * 90 + '\n'
        for (i,cromossomo) in enumerate(g):
            s += str(hex(int("".join(str(x) for x in cromossomo), 2))) #converte o binario para hexadecimal
            s += ' | fitness: ' + str(self.fitness(cromossomo)) + '  |  ' + 'indice: ' + str(i) + '\n'
        print(s)

    def generate_new_population(self, parents):
        new_population = []
        for i in range(self.population_size):
            parent1 = parents[i%len(parents)]      #seleciona o 1 pai
            parent2 = parents[(i+1)%len(parents)]  #seleciona o 2 pai
            son = self.crossover(parent1,parent2)  #gera um filho atraves do cruzamento dos 2 pais
            new_population.append(son)             #adiciona o filho para proxima geracao
        return new_population         #retorna a nova geracao
    
    def solve(self):
        
        population = self.create_population() #cria a populacao inicial
        it = self.generation_numb #define o numero de passos
        
        while it > 0:
            self.imprime_geracao(population)
            parents = self.selection(population)
            population = self.generate_new_population(parents)
            self.mutation(population)
            it -= 1
        
        for i in population:
            print(avaliacao(i))
        return population[0]
        