#Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas.

juntar_duas_listas = lambda lista1, lista2: lista1 + lista2

if __name__ == "__main__":
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    print(juntar_duas_listas(numeros, [3, 6, 2, 5, 8]))
