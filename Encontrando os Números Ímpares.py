#Crie uma função que filtre uma lista de números e retorne apenas os números ímpares.

numeros_impares = lambda lista: [n for n in lista if n % 2 != 0]

if __name__ == "__main__":
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    print(numeros_impares(numeros))
