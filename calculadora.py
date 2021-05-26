operator = {
    '': lambda a, b: a+b, 
    '2': lambda a, b: a-b, 
    '4': lambda a, b: a/b, 
    '3': lambda a, b: a*b,
    '5': lambda a, b: a**b,
    }

def calculator():
    print('''
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir 
    5 - Potencia 
    ''')
    return input('Informe o numero da operação que deseja realizar: ')

def main():
    while True:
        sair = int(input('1 - Sair | 0 - Continuar: '))
        if sair == 1:
            break
        a = int(input('Informe o valor de A: '))
        b = int(input('Informe o valor de B: '))
        return operator[calculator()](a,b)
        

if __name__ == '__main__':
    print(main())