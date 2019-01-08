import csv
import time

from neupy import algorithms, environment  # Funções Neupy
from normalizacao import *  # Função de normalização dos dados das características
from SOM_imagem import * # Função que plota o gráfico com as características analisadas [com e sem falha]
from dadosSOM import *


plt.style.use ( 'ggplot' )
environment.reproducible ()

ggplot_colors = plt.rcParams[ 'axes.prop_cycle' ]
colors = np.array ( [ c[ 'color' ] for c in ggplot_colors ] )

matriz_caracteristicas = [ ]
rotulos = [ ]

# Obter as características para análise e seus respectivos rótulos
with open ( 'all.csv', 'r' ) as planilha:
    leitor = csv.reader ( planilha, delimiter='\t' )

    for linha in leitor:
        matriz_caracteristicas.append ( [ float ( linha[ caracteristica1 ] ), float ( linha[ caracteristica2 ] ) ] )

        if ('1' in linha[ -1 ]):  # rotulo com falha
            rotulos.append ( 1 )
        else:
            rotulos.append ( 0 )

# Conversão do tipo 'list' em 'array'
matriz_caracteristicas = np.array ( matriz_caracteristicas )
rotulos = np.array ( rotulos )

# Normalização dos dados da matriz de características
normalizacao ( matriz_caracteristicas )


sofm = algorithms.SOFM (
    n_inputs=2,
    features_grid=(grid_x, grid_y),

    verbose=True,
    shuffle_data=True,

    # O neurônio vencedor (UMC - Unidade de Melhor Correspondência ou BMU - Best Matching Unit) é selecionado mediante sua distância euclidiana dos dados de entrada
    distance='euclid',

    # Raio de aprendizagem: learning_radius : Referente ao compartilhamento do neurônio vencedor com sua vizinhança (neurônios vizinhos)
    # Redução do raio de aprendizagem: reduce_radius_after: O raio de aprendizagem será reduizdo para 1 após 20 épocas
    learning_radius=2,
    reduce_radius_after=20,

    # Desvio padrão: std
    # Redução do desvio padrão: reduce_std_after: após 20 épocas
    std=1.45,
    reduce_std_after=20,

    # Taxa de aprendizagem : step
    # Redução da taxa de aprendizagem: reduce_step_after
    step=0.30,
    reduce_step_after=40,
)

# Exibição gráfica do treinamento da rede:
# Nesta exibição pode-se perceber o ajuste dos pesos entre os neurônios até que se atinja o número de épocas determinado

for epoca in range ( epocas ):
    sofm.train ( matriz_caracteristicas, epochs=1)

    SOM( matriz_caracteristicas, rotulos, sofm)

    plt.draw ()

    plt.pause ( 1e-20 )

    time.sleep ( 0.01 )

    plt.clf ()

SOM( matriz_caracteristicas, rotulos, sofm )

plt.show ()