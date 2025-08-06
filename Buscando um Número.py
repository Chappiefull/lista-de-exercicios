#Elabore uma função que receba um número e uma lista. A função deve buscar o número na lista e retornar 'True' se o encontrar e 'False' caso contrário.

tem_numero = lambda n, lista: n in lista

if __name__ == "__main__":
    from os import system, name
    clean = lambda: system('cls' if name == 'nt' else 'clear')

    while True:
        clean()
        try: 
            n = int(input("Digite um número inteiro para saber se ele está na lista: "))
            break
        except: continue
    
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    print(tem_numero(n, numeros))
