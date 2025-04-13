import unittest
import main 

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = main.Calculadora()

    def test_suma(self):
        self.assertEqual(main.sumar(2, 3), 5)


    def test_resta(self):
        self.assertEqual(main.restar(5, 2), 3)

    def test_multiplicacion(self):
        self.assertEqual(main.multiplicar(3, 4), 12)

    def test_division(self):    
        self.assertEqual(main.dividir(10, 2), 5)

    def test_division_por_cero(self):   
        with self.assertRaises(ValueError):
            main.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()

