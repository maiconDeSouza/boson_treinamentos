x = y = z = False

n_1 = n_2 = 0

print('Digite um número para representar n_1:')
n_1 = int(input())

print('Digite um número para representar n_2:')
n_2 = int(input())

x = n_1 == n_2
y = n_1 > n_2
z = n_1 != n_2

print(f"{n_1} igual {n_2}, {x}")
print(f"{n_1} maior {n_2}, {y}")
print(f"{n_1} diferente {n_2}, {z}")
