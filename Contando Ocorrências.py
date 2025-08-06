#Desenvolva uma função que receba uma lista e um valor. A função deve contar quantas vezes esse valor aparece na lista e retornar o total.

contador_ocorrencias = lambda n, lista: len([numero for numero in lista if numero == n])

if __name__ == "__main__":
    from os import name, system

    clean = lambda: system('cls' if name == 'nt' else 'clear')

    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    while True:
        clean()
        try: 
            n = int(input("Digite um número inteiro para saber a quantidade de vezes que ele aparece na lista: "))
        except: 
            continue
        break

    print(contador_ocorrencias(n, numeros))

