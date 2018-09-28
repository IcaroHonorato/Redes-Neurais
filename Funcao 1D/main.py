# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from descida_gradiente import descida_gradiente
from func1D_incognito import func1D_incognito as function
from func1D_incognito import grad_func1D_incognito as gradient_function

# Determinar uma faixa de valores para plotar (função, gradiente da função, Descida de Gradiente)
# ________________________________________________________________________________________________
initial_value_int = 0
final_value_int = 2000
step = 0.01
interval = list ( range ( initial_value_int, final_value_int ) )
interval = [ interval[ i ] * step for i in range ( initial_value_int, final_value_int ) ]

# Valores da Função e Gradiente da Função no intervalo determinado
# ________________________________________________________________________________________________
values_function = [ ]
values_gradient = [ ]
for i in interval:
    values_function.append ( function ( i ) )
    values_gradient.append ( gradient_function ( i ) )

# Limites constituintes do gráfico
# ___________________________________________________________________________________
mins_f_gf = [ min ( values_function ), min ( values_gradient ) ];
maxs_f_gf = [ max ( values_function ), max ( values_gradient ) ];

# Imprimir função e gradiente da função, no intervalo definido
# ___________________________________________________________________________________
plt.figure(1)

plt.plot ( interval, values_function, 'k-', color='blue' )
plt.plot ( interval, values_gradient, 'k--', color='orange' )
# Limites dos eixos vertical e horizontal
plt.axis ( [ initial_value_int, final_value_int * step, min ( mins_f_gf ), max ( maxs_f_gf ) ] );
# Título e legenda
plt.suptitle ( "Function and Gradiente Values in Interval" )
plt.title ( '[Blue - Function]\n[Orange - Gradient Function]' )
# Configurações da Grade
plt.grid ( True )
plt.xlabel ( "Intervalo de Analise x = [0,20]" )
plt.ylabel ( "f(x)" )

plt.show ()

# Descida de gradiente com vários valores iniciais e os respectivos mínimos locais encontrados
# ________________________________________________________________________________________________
# Parâmetros e variáveis do loop
# ___________________________________________________________________________________
grad_descent_values = [ ]
values_x = [ [ ] ]
values_f_x = [ [ ] ]
local_minimum = [ ]
f_x_minimum = [ ]
range_limit = 16
colors = [ 'b', 'g', 'r', 'c', 'm', 'y', 'k' ]
# Descida de gradiente aplicada a todos os valores no range determinado
# ___________________________________________________________________________________
for i in range (1, range_limit ):  # type: int
    #Valores x -> i e f(x) -> f(i), gerados pela descida de gradiente
    grad_descent_values = descida_gradiente ( i, function, gradient_function )
    style_list = [ 'default', 'classic' ] + sorted ( style for style in plt.style.available if style != 'classic' )

    # Separando os valores de x e f(x) gerados a partir de i
    for j in range ( len ( grad_descent_values ) ):
        values_x[i-1].append ( grad_descent_values[ j ][ 0 ] )
        values_f_x[i-1].append ( grad_descent_values[ j ][ 1 ] )

    if grad_descent_values != [ ]:

        local_minimum.append ( grad_descent_values[ -1 ][ 0 ] )
        f_x_minimum.append ( grad_descent_values[ -1 ][ 1 ] )

        print('Local Minimum in i =', i, ':', grad_descent_values[ -1 ][ 0 ])

    #Obter próximo vetor de x e f(x) para o próximo i
    values_x.append ([])
    values_f_x.append ([])


# Impressões finais

# 1) Impressão dos valores gerados f(x) para cada x aplicado à função
# ___________________________________________________________________________________
n_cols = 3
n_rows = len(values_x)/n_cols

style_label = style_list[ 7 ]
(fig_width, fig_height) = plt.rcParams[ 'figure.figsize' ]
fig_size = [ fig_width * 4, fig_height / 1.2 ]
fig, axes = plt.subplots ( ncols=n_cols, nrows=n_rows, num=style_label,figsize=fig_size, squeeze=True )
index = 0

for it_col in range(n_cols):
    for it_row in range(n_rows):
        # Valores de x e f(x) gerados para o valor i do intervalo aplicado a função
        axes[ it_row ][it_col].plot ( values_x[index], values_f_x[index], '*' )
        # Mínimo local resultante da descida de gradiente para o valor i
        axes[ it_row ][ it_col ].plot ( local_minimum, f_x_minimum, 'o', color='red' )
        # Função
        axes[ it_row ][ it_col ].plot ( interval, values_function, 'k-', color='blue' )
        # Configurações da Grade
        axes[ it_row ][ it_col ].grid ( True )
        if it_row == n_rows-1:
            axes[ it_row ][ it_col ].set_xlabel ( "x value" )
        if it_col == 0:
            axes[ it_row ][ it_col ].set_ylabel ( "f(x) value" )
        index +=1

plt.suptitle("Behavior of the function for each value 'x' sampled")
plt.show()
# ___________________________________________________________________________________
plt.figure(3)
plt.subplot(1,1,1)
# Plotar cada relação x-f(x) na descida de gradiente, para todos os x determinados no intervalo
for i in range(len(values_x)):
    plt.plot( values_x[i], values_f_x[i], '*' )
    plt.plot(local_minimum, f_x_minimum, 'o')

# Plotar gráfico da função
plt.plot ( interval, values_function, 'k-', color='blue' )

# Limites dos eixos vertical e horizontal
plt.axis ( [ initial_value_int - 0.5, final_value_int * step, min ( mins_f_gf ), max ( maxs_f_gf ) + 0.5 ] );

# Título e legenda
plt.suptitle ( "Gradiente Descent Data" )
plt.title ( '[Blue - Function] -- [Orange - Convergence] -- [Red - Local Minimum]' )

# Configurações da Grade
plt.grid ( True )
plt.xlabel ( "x value" )
plt.ylabel ( "f(x) value" )
plt.show ()
# ________________________________________________________________________________________________
