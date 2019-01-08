import numpy as np
import matplotlib.pyplot as plt
#from UMC import *
from dadosSOM import *



ggplot_colors = plt.rcParams[ 'axes.prop_cycle' ]
colors = np.array ( [ c[ 'color' ] for c in ggplot_colors ] )


def SOM(matriz_caracteristicas, rotulos, sofm):

    plt.title ( 'Mapa Auto-Organizavel' )
    plt.xlabel ( 'Caracteristica ' + str ( caracteristica1 ) )
    plt.ylabel ( 'Caracteristica ' + str ( caracteristica2 ) )

    # Plotagem dos Neurônios

    linha = 0

    # Cores dos dados:
    # 1.Vermelho: dados sem falha
    # 2.Azul: Dados com falha

    vermelho ='#E24A33';
    azul = '#348ABD';

    sem_falha = [ ]
    com_falha = [ ]

    # Tratamento do vetor de rótulos:

    # 1. Separação em dois vetores: sem_falha e com_falha
    for dado in matriz_caracteristicas:
        if rotulos[ linha ] == 0:
            sem_falha.append ( dado )
        else:
            com_falha.append ( dado )
        linha += 1

    # 2. Transformação do tipo list em array
    sem_falha = np.array( sem_falha )
    com_falha = np.array( com_falha )

    # 3. Plotagem dos dados das características, agora separados em 'sem falha' e 'com falha'
    plt.scatter(*sem_falha.T, c=vermelho, s=100, alpha=1, label='Sem falha (SF)' )
    plt.scatter(*com_falha.T, c=azul, s=100, alpha=1, label='Com falha (CF)' )

    # Tratamento dos neurônios da rede treinada:
    plt.scatter ( *sofm.weight, s=300, alpha=0.6, c=colors[ 7 ], label='Neurônio' )

    # plotar as linhas - pesos entre os neurônios
    total_neuronios = grid_x * grid_y

    for neuronio in range ( total_neuronios ):
        neur_direita = neuronio + 1
        neur_baixo = neuronio + grid_x

        if neur_direita % grid_x != 0:
            plt.plot ( [ sofm.weight[ 0 ][ neuronio ], sofm.weight[ 0 ][ neur_direita ] ],
                       [ sofm.weight[ 1 ][ neuronio ], sofm.weight[ 1 ][ neur_direita ] ], 'k-' )
        if neur_baixo < total_neuronios:
            plt.plot ( [ sofm.weight[ 0 ][ neuronio ], sofm.weight[ 0 ][ neur_baixo ] ],
                       [ sofm.weight[ 1 ][ neuronio ], sofm.weight[ 1 ][ neur_baixo ] ], 'k-' )

    plt.legend ( loc='upper left' )
