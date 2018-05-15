'''
Created on 15 may. 2018

@author: manuelito
'''
import unittest
from SistLogin.models import Seguridad


class Test(unittest.TestCase):


    def setUp(self):
        self.prueba = Seguridad()


    def tearDown(self):
        pass

    #Caso inicial para probar formato de email
    def test_emailIncorrecto(self):
        self.emailvalido = self.prueba.registrarUsuario("hola", "s","s")
        self.assertEqual(-1, self.emailvalido)
        
    #Caso inicial para probar cuando el email no contiene punto
    def test_emailIncorrecto2(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s", "s","s")
        self.assertEqual(-1, self.emailvalido)
    
    #Caso para probar que un email es valido
    def test_emailValido(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s.com", "s","s")
        self.assertEqual(0, self.emailvalido)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()