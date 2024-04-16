numeros =  [1, 2, 4, 6];

numeros2 = [3, 5, 7, 8];



def suma(numbers, numbers2):
    suma = [];

    for i in range(len(numbers)):
        suma.append(numbers[i] + numbers2[i]);
    
    return suma;

resultado = suma(numeros, numeros2);

print("The result is: ", resultado);
