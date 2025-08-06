#Elabore uma função que receba uma lista com valores possivelmente duplicados e retorne uma nova lista contendo apenas os valores únicos, sem repetições.

def retirar_duplicados(lista):
    lista_sem_duplicados = []
    for n in lista:
        if n not in lista_sem_duplicados:
            lista_sem_duplicados.append(n)
    return lista_sem_duplicados

if __name__ == "__main__":
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

    print(retirar_duplicados(numeros))
