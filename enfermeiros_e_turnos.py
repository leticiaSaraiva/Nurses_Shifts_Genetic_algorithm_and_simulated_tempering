
## EQUIPE ##
# Claro Henrique
# Letícia Saraiva


from AlgoritmoGenetico import AlgoritmoGenetico
from TemperaSimulada import TemperaSimulada
from estado import *

turnos = 21   #turnos precisa ser divisivel por 3
enferm = 10
metodo = 0
define_parametros(turnos,enferm)


#Função para ler um arquivo contendo um estado específico
def gerar_estado_arquivo():
    f = open('input.txt','r')
    global enferm
    estado_inicial = []
    enferm = -1
    for linha in f:
        enferm += 1
        for col in linha:
            if col != '\n':
                estado_inicial.append(int(col))
    define_parametros(turnos,enferm)
    return estado_inicial

#Função para resolver o problema a partir de um estado vazio
def resolver_estado_vazio_tempera():
    estado_inicial = [0]*enferm*turnos
    tempera = TemperaSimulada(estado_inicial,t_0= temperatura_inicial, d_t = .001)
    print('Estado final da busca: ')
    return tempera.solve()

#Função para resolver o problema a partir do estado lido do arquivo
def resolver_estado_arquivo_tempera():
    estado_inicial = gerar_estado_arquivo()
    tempera = TemperaSimulada(estado_inicial, t_0 = temperatura_inicial, d_t = .001)
    print('Estado final da busca: ')
    return tempera.solve()

#Função resolve utilizando o algoritmo genético,
#os estados iniciais são gerados de forma aleatória dentro do algoritmo
def resolver_genetico():
    genetico = AlgoritmoGenetico(tamanho_populacao,
                                quantidade_geracoes,
                                probabilidade_mutacao,
                                porcetagem_elitismo )
    return genetico.solve()

def limpar_tela():
    print('\n'*10)
    
def pressione_enter():
    print('Precione ENTER para continuar.')
    input()
    limpar_tela()


def menu_principal():
    
    while True:
        print('Bem vindo ao programa que resolve um problema de alocacao de enfermeiros em turnos! (✿❦ ͜ʖ ❦)\n')
        
        print('[1] - realizar Busca Têmpera no arquivo de texto (input.txt)')
        print('[2] - realizar Busca Têmpera em um estado vazio')
        print('[3] - resolver problema com Algoritmo Genético')
        print('[4] - mudar os parametros da Busca Têmpera')
        print('[5] - mudar os parametros do Algoritmo Genético')

        print()
        print('[0] - para encerrar o programa')

        op = input()
        if(op == '1'):
            resolver_estado_arquivo_tempera()
        if(op == '2'):
            imprime_estado(resolver_estado_vazio_tempera())
        if(op == '3'):
            imprime_estado(resolver_genetico())
        if(op == '4'):
            menu_parametros_tempera()
        if(op == '5'):
            menu_parametros_genetico()
        if(op == '0'):
            break
        pressione_enter()

temperatura_inicial = 12
def menu_parametros_tempera():
    while True:
        print('Bem vindo ao menu de mundanca de parametros! ( ͡~ ͜ʖ ͡°)\n')
        global enferm
        global temperatura_inicial
        print('Numero de enfermeiros atual:',enferm)
        print('Temperatura inicial atual:',temperatura_inicial)
        print()

        print('[1] - escolher numero de enfermeiros')
        print('[2] - escolher temperatura inicial')
        
        print()
        print('[0] - voltar ao menu principal')
        
        op = input()
        if(op == '0'):
            break
        if(op == '1'):
            print('Digite a quantidade de enfermeiros')
            enferm = int(input())
        if(op == '2'):
            print('Digite a temperatura inicial')
            temperatura_inicial = int(input())
    
    define_parametros(turnos,enferm)


tamanho_populacao = 40
quantidade_geracoes = 120
probabilidade_mutacao = .05
porcetagem_elitismo = .25

def menu_parametros_genetico():
    while True:
        print('Bem vindo ao menu de mundanca de parametros! ( ͡~ ͜ʖ ͡°)\n')
        global enferm
        global tamanho_populacao
        global quantidade_geracoes
        global probabilidade_mutacao
        global porcetagem_elitismo 

        print('Numero de enfermeiros atual:',enferm)
        print('Tamanho da população atual:',tamanho_populacao)
        print('Quantidade de gerações atual:',quantidade_geracoes)
        print('Probabilidade de mutação atual:',probabilidade_mutacao)
        print('Porcentagem de elitismo atual:',porcetagem_elitismo)
        

        print()

        print('[1] - escolher numero de enfermeiros')
        print('[2] - escolher tamanho da população')
        print('[3] - escolher quantidade de geracoes')
        print('[4] - escolher probabilidade de mutacao')
        print('[5] - escolher porcetagem de elitismo')
        
        print()
        print('[0] - voltar ao menu principal')
        
        op = input()
        if(op == '0'):
            break
        if(op == '1'):
            print('Digite a quantidade de enfermeiros')
            enferm = int(input())
        if(op == '2'):
            print('Digite o tamanho da população')
            tamanho_populacao = int(input())
        if(op == '3'):
            print('Digite a quantidade de geracoes')
            quantidade_geracoes = int(input())
        if(op == '4'):
            print('Digite a probabilidade de mutação')
            probabilidade_mutacao = float(input())
        if(op == '5'):
            print('Digite a porcentagem de elitismo')
            porcetagem_elitismo = float(input())
    
    define_parametros(turnos,enferm)


menu_principal()
