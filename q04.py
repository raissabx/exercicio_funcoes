def numero(n):
    if n > 0:
        print('P')
    elif n <= 0:
        print('N')

n = int(input('Digite um número: '))
print('Esse número é:', end=' ')
numero(n)