import numpy as np

sample_list = np.array([1, 2, 3])
print(sample_list)

my_matrix =np.array( [[5, 2, 3],[4, 5, 6],[7, 8, 9]])
print(my_matrix)
# 
print(my_matrix.T)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

suma = A + B
print("Suma de matrices:\n", suma)
producto = np.dot(A, B)
print("Producto de matrices:\n", producto)

sample_list = np.arange(50,100,1)
sample_list = np.random.choice(sample_list,10)
print(sample_list)
# Ejemplo: 5 enteros entre 10 y 20
arr = np.random.randint(10, 20, 5)
print(arr)

arr = np.random.randn(5)  # 5 números de una normal estándar
print(arr)

# Ejemplo: array 2x3
arr = np.random.rand(2, 3)
print(arr)

# Ejemplo: 5 números aleatorios
arr = np.random.random(5)
print(arr)

arr = np.random.randint(10, 20,size=(3,3))
print(arr)