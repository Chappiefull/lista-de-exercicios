#Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados.

def segundo_maior_numero(lista):
    while True:
        maior_numero = max(lista)
        lista.remove(maior_numero)
        if max(lista) == maior_numero:
            continue
        break
    return max(lista)

if __name__ == "__main__":

    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
    print(segundo_maior_numero(numeros))
