import numpy as np
a = np.arange(30).reshape(5,2,3)
print(a)
b = np.arange(25).reshape(5,5)
print(b)

print(b.shape)
print(a.shape)
I = np.eye(4)
print(I)
f = np.full((3,3),5)
print(f)
r = np.random.random((4,3))
print(r.reshape(3,4))
