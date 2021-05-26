import unittest
import calculadora


class CalculatorTest(unittest.TestCase):

    def test_two_values_not_are_number(self):
        self.assertFalse(calculadora.all_values_is_numbers(1,'a'))

    def test_two_values_equal_zero(self):
        self.assertEqual(calculadora.div(0, 0), 'nao pode dividir por 0')

    def test_sum(self):
        result = calculadora.mathematical_formulas['1'](1, 5)
        self.assertEqual(result, 6)

    def test_sub(self):
        result = calculadora.mathematical_formulas['2'](1, 5)
        self.assertEqual(result, -4)

    def test_mul(self):
        result = calculadora.mathematical_formulas['4'](1, 5)
        self.assertEqual(result, 5)

    def test_pot(self):
        result = calculadora.mathematical_formulas['5']('a', 2)
        self.assertEqual(result, 'ambos os valores devem ser numberos')

    def test_pot(self):
        result = calculadora.mathematical_formulas['5'](2, 2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
