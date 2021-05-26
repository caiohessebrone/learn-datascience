
def all_values_is_numbers(a, b):
    return isinstance(a, int) and isinstance(b, int)

def somar(a,b):
    if all_values_is_numbers(a, b):
        return a+b
    return 'ambos os valores devem ser numberos'

def sub(a,b):
    return a-b
    if all_values_is_numbers(a, b):
        return a+b
    return 'ambos os valores devem ser numberos'


def mult(a,b):
    if all_values_is_numbers(a, b):
        return a*b
    return 'ambos os valores devem ser numberos'


def div(a,b):
    two_number_equal_zero = a == 0 and b == 0
    if two_number_equal_zero:
        return 'nao pode dividir por 0'

    if all_values_is_numbers(a, b):
        return a/b
    return 'ambos os valores devem ser numberos'


def pot(a,b):
    if all_values_is_numbers(a, b):
        return a**b
    return 'ambos os valores devem ser numberos'


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
    while True:
        sair = int(input('1 - Sair | 0 - Continuar: '))
        if sair == 1:
            break
        return mathematical_formulas[operations()](a, b)
