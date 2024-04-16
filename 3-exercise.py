lista_palabras = ["manzana", "banana", "pera", "naranja", "limón", "marcelo", ""];

letra = "m";


def palabras_con_letra(lista_palabras, letra):

    palabras_filtradas = [palabra for palabra in lista_palabras if palabra.startswith(letra)];

    return palabras_filtradas;



palabras_con_letra_m = palabras_con_letra(lista_palabras, letra);

print("Palabras que comienzan con la letra '{}':".format(letra), palabras_con_letra_m);


