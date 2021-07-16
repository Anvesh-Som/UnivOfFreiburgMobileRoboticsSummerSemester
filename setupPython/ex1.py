#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as mp
def fun(x):
	return np.cos(x)*np.exp(x)

x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=True)
to_plot = fun(x)
mp.ylabel('cos(x) * exp(x) ---> ') #axis labels
mp.xlabel('x ---> ')
mp.plot(x,to_plot)

# to save plot as image
mp.savefig('ex1.png')
mp.show()

vecNormal = np.rand
