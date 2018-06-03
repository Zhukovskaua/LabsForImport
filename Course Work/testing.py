import numpy as np

first_matrix = np.genfromtxt("1.txt", delimiter=",")
second_matrix = np.genfromtxt("2.txt", delimiter=",")

print(first_matrix)
print(second_matrix)

a = first_matrix.transpose()
print(a)