
def all_values_is_numbers(a, b):
    return isinstance(a, int) and isinstance(b, int)

def test_all_number(func):
    def wraper(*args, **kwargs):
        num_one, num_two = args
        if all_values_is_numbers(num_one, num_two):
            return func(num_one, num_two)
        else:
            return 'ambos os valores devem ser numberos'
    return wraper


@test_all_number
def somar(a,b):
    return a+b

@test_all_number
def sub(a,b):
    return a-b

@test_all_number
def mult(a,b):
    return a*b

@test_all_number
def div(a,b):
    two_number_equal_zero = a == 0 and b == 0

    if two_number_equal_zero:
        return 'nao pode dividir por 0'
    return a/b

@test_all_number
def pot(a,b):
    return a**b

mathematical_formulas = {
    '1': somar, 
    '2': sub, 
    '4': mult, 
    '3': div,
    '5': pot,
    }

def operations():
    print('''
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir 
    5 - Potencia 
    ''')
    return input('Informe o numero da operação que deseja realizar: ')

def main(a, b):
    return mathematical_formulas[operations()](a, b)
    
while True:
    sair = int(input('1 - Sair | 0 - Continuar: '))
    if sair == 1:
        break
    a = int(input('Informe o primeiro numero: '))
    b = int(input('Informe o segundo numero: '))
    print(mathematical_formulas[operations()](a, b))

