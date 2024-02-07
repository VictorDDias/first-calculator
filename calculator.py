def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

while True:
    print('ESCOLHA A OPÇÃO DESEJADA')
    print()
    print('SOMA [1]')
    print()
    print('SUBTRAÇÃO [2]')
    print()
    print('MULTIPLICAÇÃO [3]')
    print()
    print('DIVISÃO [4]')
    print()
    try:
        escolha = int(input('Digite sua escolha: '))

        num1 = int(input('Digite o numero desejado: '))
        num2 = int(input('Digite o segundo numero desejado: '))
            
                
        if escolha == 1:
            print(f'O seu resultado foi: {soma(num1, num2)}')

        elif escolha == 2:
            print(f'O seu resultado foi: {subtracao(num1, num2)}')

        elif escolha == 3:
            print(f'O seu resultado foi: {multiplicacao(num1, num2)}')

        elif escolha == 4:
            print(f'O seu resultado foi: {divisao(num1, num2)}')
                
        else:
            print('Você não digitou nem uma opção')
    except ValueError:
        print('VocÊ precisa digitar um valor inteiro')
        break
        

