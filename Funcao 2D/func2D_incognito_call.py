import numpy as np

from func2D_incognito import func2D_incognito as function
from func2D_incognito import grad_func2D_incognito as gradient_function


x = np.array([-2.39801,1.18262])
x = np.array([-2.1,0.99])

fx = f(x)
print 'f(x)=', fx

gx = grad_f(x)
print 'nabla f(x)=', gx
