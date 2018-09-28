# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from descida_gradiente import descida_gradiente
from func2D_incognito import func2D_incognito as function
from func2D_incognito import grad_func2D_incognito as gradient_function

# Determinar uma faixa de valores para plotar (função, gradiente da função, Descida de Gradiente)
# ________________________________________________________________________________________________
# Definição do intervalo
initial_value_int = [-4.50,-4.50]
final_value_int = [4.50,4.50]
step = 0.15

# Agrupamento do intervalo para as variáveis constituintes da função 2D
interval = zip(np.arange(initial_value_int[0], final_value_int[0], step),np.arange(initial_value_int[1], final_value_int[1], step))
interval = [list(interval[i]) for i in range(len(interval))]
print(interval)
# Separação dos valores do intervalo para plotagem da função
x_axis = [interval[:][i][0] for i in range(len(interval))]
y_axis = [interval[:][i][1] for i in range(len(interval))]

# Grid referente aos valores do intervalo
X_axis,Y_axis = np.meshgrid(x_axis,y_axis)

# Definição do Eixo z, que corresponde a aplicação da função sobre os valores do intervalo
z_axis = np.array([function([x1,x2]) for x1,x2 in zip(np.ravel(X_axis), np.ravel(Y_axis))])
Z_axis = z_axis.reshape(Y_axis.shape)

# Geração de Figuras
# ________________________________________________________________________________________________
# As Figuras 1 e 2 retratam o comportamento da função no intervalo determinado
# Figura 1
function_figure_1 = plt.axes(projection='3d')  # type: Axes

function_figure_1.plot_surface(X_axis, Y_axis, Z_axis)

function_figure_1.set_xlabel('x1 Variant')
function_figure_1.set_ylabel('x2 Variant')
function_figure_1.set_zlabel('f(x1,x2) result')
function_figure_1.set_title('Behavior of the Function 2D in the Determined Interval');

plt.show()
# Figura 2
function_figure_2 = plt.axes(projection='3d')
function_figure_2.plot_wireframe(X_axis, Y_axis, Z_axis, color='black')

function_figure_1.set_xlabel('x1 Variant')
function_figure_1.set_ylabel('x2 Variant')
function_figure_1.set_zlabel('f(x1,x2) result')

function_figure_2.set_title('Behavior of the Function 2D in the Determined Interval');

plt.show()

# Aplicação da descida de gradiente para todos os valores do intervalo determinado e seu resultado em function

grad_descent_values = [descida_gradiente(it, function, gradient_function) for it in interval]
values_x_2d = [grad_descent_values[i][j][0] for i in  range(len(grad_descent_values)) for j in range(len(grad_descent_values[i]))]
values_fx_2d = [grad_descent_values[i][j][1] for i in  range(len(grad_descent_values)) for j in range(len(grad_descent_values[i]))]
local_minimum = [grad_descent_values[i][-1][0] for i in range(len(grad_descent_values))]

# Figura 3 - Representando o procedimento acima
plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

z = values_fx_2d
x = [values_x_2d[i][0] for i in range(len(values_x_2d))]
y = [values_x_2d[i][1] for i in range(len(values_x_2d))]

ax.plot(x, y, z, label='parametric curve')
ax.set_xlabel("x1 variant")
ax.set_ylabel("x2 variant")
ax.set_zlabel("f(x)result")
ax.set_title("Behavior of f(x) by applying Gradient Descent ")
ax.legend()

plt.show()

#Figura 4 - Representando os mínimos locais da função obtidos pelo método descida de gradiente dentro do intervalo determinado
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

x_lm = [local_minimum[i][0] for i in range(len(local_minimum))]

y_lm = [local_minimum[i][1] for i in range(len(local_minimum))]

step_value = (final_value_int[0] - initial_value_int[0])/len(x_lm)
z_lm = [initial_value_int[0] + x*step_value for x in range(len(x_lm))]

ax.plot(x_lm, y_lm, z_lm, label='parametric curve')
ax.set_xlabel("x1 minimum")
ax.set_ylabel("x2 minimum")
ax.set_zlabel("f(x)result")
ax.set_title("Local Minimum behavior of f(x) by applying Gradient Descent ")
ax.legend()

plt.show()
# ________________________________________________________________________________________________