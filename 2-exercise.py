numeros1 =  [1, 2, 4, 6];

numeros2 =  [3, 5, 7, 8];

impares = [x for x in numeros1 + numeros2 if x % 2 != 0]

mayores_a_5 = [x for x in numeros1 + numeros2 if x > 5]

print("Valores impares:", impares)
print("Valores mayores a 5:", mayores_a_5)

