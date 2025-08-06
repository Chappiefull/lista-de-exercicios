#Crie uma função que receba uma lista de números e retorne a soma de todos os seus valores.

soma_dos_valores = lambda lista: sum(lista)

if __name__ == "__main__": 
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    print(soma_dos_valores(numeros))
