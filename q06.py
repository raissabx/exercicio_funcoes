def conversao (hora, minuto):
    if hora <= 12:
        return str(hora) + ':' + str(minutos)

    elif hora == 0:
        return str(12) + ':' + str(minutos)
    else:
        return str(hora-12) + ':' + str(minutos)

def converteTurno(hora):
    if hora > 12:
        return 'P'
    else:
        return 'A' 


def saida(turno):
    if turno == 'A':
        return 'A.M'

    elif turno == 'P':
        return 'P.M'
    
    else:
        print('Valor inválido')

opcao = ''
while opcao != 's':
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    horario = conversao(horas, minutos)
    turno = converteTurno(horas)
    turno = saida(turno)
    print(horario + turno)
    opcao = input('Continuar - Enter, Sair - s').lower()

print('Fim do programa')
