def soma():
    x = int(input('\nDigite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    
    print(f'A soma é {x + y}\n')


def sub():
    x = int(input('\nDigite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    
    print(f'A subtração é {x - y}\n')
    

while True:
    print('Faça uma escolha:')
    print('1. Adição')
    print('2. Subtração')
    print('0. Encerra o programa')
    
    n = int(input('Escolha: '))

    if n == 0:
        break
    
    elif n == 1:
        soma()
    
    elif n == 2:
        sub()
    
    else:
        print('Escolha fora do desconhecida.')
