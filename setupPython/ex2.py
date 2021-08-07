#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as mp

#a)
vecNormal = np.random.normal(5.0, 2.0, 100000)

#b)
vecUniform = np.random.uniform(0, 10, 100000)

#c)
print("Normal Vector")
print("Mean = "),
print(np.mean(vecNormal))
print("Standard Deviation = "),
print(np.std(vecNormal))
print("Uniform Vector")
print("Mean = "),
print(np.mean(vecUniform))
print("Standard Deviation = "),
print(np.std(vecUniform))
