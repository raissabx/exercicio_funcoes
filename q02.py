parada = int(input('Digite um numero: '))

def questao02(parada):
    numero = 1
    texto = str(numero)
    print(texto)

    while numero < parada:
        numero = numero + 1
        texto = texto + ' ' + str(numero)
        print(texto)

questao02(parada)