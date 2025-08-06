#Crie uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome') e retorne uma nova lista contendo apenas os nomes de cada objeto.

extracao_nomes = lambda lista_objetos: [objeto["nome"] for objeto in lista_objetos]

if __name__ == "__main__":
    lista_objetos = [
        {"nome": "Bill Gates"},
        {"nome": "Linus Torvalds"},
        {"nome": "Dennis Ritchie"}
    ]
    
    print(lista_objetos)
    print(extracao_nomes(lista_objetos))

