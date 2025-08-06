#Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas.

juntar_duas_listas = lambda lista1, lista2: lista1 + lista2

if __name__ == "__main__":
    
    natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
    tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

    print(juntar_duas_listas(natureza, tecnologia))
