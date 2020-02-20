def calcular_media(lista_de_notas):
    resultado = 0
    contador = 0
    for nota in lista_de_notas:
        resultado = resultado + nota
        contador = contador + 1
    return resultado / contador
    
precos_da_laranja = [ 6, 4, 1, 8, 8, 10, 1 ]
media = calcular_media(precos_da_laranja)
print(media)
