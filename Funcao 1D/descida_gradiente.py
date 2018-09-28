import matplotlib.pyplot as plt
import numpy as np

from func1D_incognito import func1D_incognito as function
from func1D_incognito import grad_func1D_incognito as gradient_function

def descida_gradiente(current_value,function,gradient_function):

    #Inicializacao dos parametros
    #-----------------------------
    learning_rate = 0.01
    precision = 0.000000000001
    gap = current_value
    #-----------------------------

    max_iterations = 10000
    iter = 1
    generated_values = []

    #Processo Iterativo da Descida de Gradiente
    while(gap>precision and iter<=max_iterations):
        #Armazenar valores gerados
        generated_values.append([current_value,function(current_value)])

        #Valor anterior
        previous_value = current_value

        #Descida do gradiente
        current_value = current_value - learning_rate*(gradient_function(current_value))

        #Obter novo gap
        gap = abs(previous_value - current_value)

        #Proxima iteracao
        iter = iter + 1
    return generated_values