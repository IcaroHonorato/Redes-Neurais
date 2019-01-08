# Normalização dos dados para fins de exibição.
# Os dados das características escolhidas para treinamento e exibição do SOM
# são normalizados para reduzir a discrepância na magnitude dos vetores de entrada

# Duas características foram escolhidas para treinamento e exibição do SOM resultando
# em uma matriz de n x 2 em que 'n' representa o numero de amostras do processo para
# as duas características escolhidas. Assim sendo o processo de normalização consiste em:

# 1. Obter os 2 menores valores presentes na matriz e os 2 maiores valores;
# 2. Para cada linha (amostra) das características:
#    2.1 - Subtrair de seu valor o menor valor correspondente;
#    2.2 - Dividir o valor resultante de 2.1 pela diferença entre os valores de máx e min correspondentes.
# 3. O resultado da normalização é um valor no intervalo [0,1]

def normalizacao(matriz_dados):

    menores_valores = matriz_dados.min(axis = 0)
    maiores_valores = matriz_dados.max(axis = 0)

    for amostra in matriz_dados:
        amostra[0] = (amostra[0] - menores_valores[0]) / (maiores_valores[0] - menores_valores[0])
        amostra[1] = (amostra[1] - menores_valores[1]) / (maiores_valores[1] - menores_valores[1])