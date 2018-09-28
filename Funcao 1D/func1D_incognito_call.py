import numpy as np

from func1D_incognito import func1D_incognito as f
from func1D_incognito import grad_func1D_incognito as grad_f

########################################

#1.1 - Definição dos pontos em x
x = np.array([0.99, 4, 6])
print 'x=', x

#1.2 - Valor da função em x
fx = f(x)
print 'f(x)=', fx

#1.3 - Grandiente da função em x
gx = grad_f(x)
print 'nabla f(x)=', gx

########################################