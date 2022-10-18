from random import randint

def craps():
    rodada = 1
    resultado = ''
    ponto = 0
    while not (resultado == 'ganhou' or resultado == 'perdeu'):
        dados = randint(2, 12)
        print(f'Dados gerou: {dados}')

        if rodada == 1 and dados in (7, 11):
            print('Natural')
            print('Ganhou')
            resultado = 'ganhou'

        elif rodada == 1 and dados in (2, 3, 12):
            print('CRAPS')
            print('Você perdeu')
            resultado = 'perdeu'

        elif rodada == 1 and dados in (4, 5, 6, 8, 9, 10):
            print('Pronto')
            pontos = dados

        else:
            if dados == 7:
                print('Você perdeu!')
                resultado = 'perdeu'

            elif dados == ponto:
                print('Você ganhou!')
                resultado = 'ganhou'

        rodada = rodada + 1
        input('Enter')
    print('Fim do jogo')

craps()


