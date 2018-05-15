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
        self.emailvalido = self.prueba.registrarUsuario("hola", "Manuel123","Manuel123")
        self.assertEqual(-1, self.emailvalido)
        
    #Caso inicial para probar cuando el email no contiene punto
    def test_emailIncorrecto2(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s", "Manuel123","Manuel123")
        self.assertEqual(-1, self.emailvalido)
    
    #Caso para probar que un email es valido
    def test_emailValido(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel123")
        self.assertEqual(0, self.emailvalido)
        
    # Caso interior claves desiguales
    def test_clavesdesiguales(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel12")
        self.assertEqual(-2, self.emailvalido)
    
    # Caso interior claves iguales
    def test_clavesiguales(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel123")
        self.assertEqual(0, self.emailvalido)
    
    # Caso interior la clave es invalida
    def test_clavesinvalidas(self):
        self.emailvalido = self.prueba.registrarUsuario("hola@s.com", "Ma2","Ma2")
        self.assertEqual(-3, self.emailvalido)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()