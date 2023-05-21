import numpy as np

y = np.zeros((2, 3, 4))
print((y).shape)
print((y.sum(axis=0)).shape)
print((y.sum(axis=1)).shape)
print((y.sum(axis=2)).shape)