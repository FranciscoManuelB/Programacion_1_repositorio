from itertools import product

K, M = map(int, input("Introduce K y M separados por espacio: ").split())

listas = []
for i in range(K):
    datos = list(map(int, input(f"Introduce la lista {i+1}: ").split()))
    Ni = datos[0]
    elementos = datos[1:]
    listas.append(elementos)

max_valor = 0

for combinacion in product(*listas):
    suma_cuadrados = sum(x**2 for x in combinacion)
    valor_mod = suma_cuadrados % M
    max_valor = max(max_valor, valor_mod)

print(max_valor)
