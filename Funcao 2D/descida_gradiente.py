import matplotlib.pyplot as plt
import numpy as np

from func2D_incognito import func2D_incognito as function
from func2D_incognito import grad_func2D_incognito as gradient_function

def descida_gradiente(current_value,function,gradient_function):
    #Inicializacao dos parametros
    #-----------------------------
    learning_rate = 0.04
    precision = 1e-21
    gap = current_value
    #-----------------------------

    max_iterations = 7500
    iter = 1
    generated_values = []

    #Processo Iterativo da Descida de Gradiente
    while(abs(gap[0])>precision and abs(gap[1])>precision and iter<=max_iterations):
        #Armazenar valores gerados
        generated_values.append([current_value,function(current_value)])

        #Valor anterior
        previous_value = current_value

        #Descida do gradiente
        current_value = current_value - learning_rate*(gradient_function(current_value))

        #Obter novo gap
        gap[0] = abs(previous_value[0] - current_value[0])
        gap[1] = abs(previous_value[1] - current_value[1])

        #Proxima iteracao
        iter = iter + 1
    print(generated_values[-1][0])
    return generated_values