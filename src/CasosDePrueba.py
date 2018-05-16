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
        self.prueba = None

    #Caso inicial para probar formato de email
    def test_emailIncorrecto(self):
        self.validar = self.prueba.registrarUsuario("hola", "Manuel123","Manuel123")
        self.assertEqual(-1, self.validar[0])
        
    #Caso inicial para probar cuando el email no contiene punto
    def test_emailIncorrecto2(self):
        self.validar = self.prueba.registrarUsuario("hola@s", "Manuel123","Manuel123")
        self.assertEqual(-1, self.validar[0])
    
    #Caso interior para probar que un email es valido
    def test_emailValido(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel1234","Manuel1234")
        self.assertEqual(0, self.validar[0])
        
    # Caso interior claves desiguales
    def test_clavesdesiguales(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel1234")
        self.assertEqual(-2, self.validar[0])
    
    # Caso interior claves iguales
    def test_clavesiguales(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel123")
        self.assertEqual(0, self.validar[0])
        
    #Caso frontera para cuando la clave es exactamente 8 caracteres
    def test_clave8Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel12","Manuel12")
        self.assertEqual(0, self.validar[0])
        
    #Caso frontera para cuando la clave es exactamente 16 caracteres
    def test_clave16Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel1234567890","Manuel1234567890")
        self.assertEqual(0, self.validar[0])  
        
    #Caso esquina para cuando la clave es exactamente 7 caracteres
    def test_clave7Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel1","Manuel1")
        self.assertEqual(-3, self.validar[0])  
        
    #Caso esquina para cuando la clave es exactamente 17 caracteres
    def test_clave17Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel12345678901","Manuel12345678901")
        self.assertEqual(-3, self.validar[0])  
        
    #Caso esquina para cuando la clave es exactamente 9 caracteres
    def test_clave9Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel123","Manuel123")
        self.assertEqual(0, self.validar[0])  
        
    #Caso esquina para cuando la clave es exactamente 15 caracteres
    def test_clave15Char(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel123456789","Manuel123456789")
        self.assertEqual(0, self.validar[0])
        
    #Caso malicioso cuando la clave no tiene digitos
    def test_claveSinDigitos(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuelabc","Manuelabc")
        self.assertEqual(-3, self.validar[0])
        
    #Caso malicioso cuando la clave no tiene mayusculas
    def test_claveSinMayusculas(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "manuelab1","manuelab1")
        self.assertEqual(-3, self.validar[0])
        
    #Caso malicioso cuando la clave no tiene minusculas
    def test_claveSinMinusculas(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "MANUEL123","MANUEL123")
        self.assertEqual(-3, self.validar[0])
        
    #Caso malicioso cuando la clave contiene un caracter especial
    def test_claveConCaracEspecial(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Manuel123$","Manuel123$")
        self.assertEqual(-3, self.validar[0])
        
    #Caso malicioso cuando la clave tiene menos de 3 letras
    def test_claveMenosDe3Letras(self):
        self.validar = self.prueba.registrarUsuario("hola@s.com", "Ma123456","Ma123456")
        self.assertEqual(-3, self.validar[0])
    
    #Caso interior usuario registrado y aceptado al ingresar.
    def test_usuarioaceptado(self):
        self.registro = self.prueba.registrarUsuario("13-11223@usb.ve", "Manuel123","Manuel123")
        self.validar = self.prueba.IngresarUsuario("13-11223@usb.ve", "Manuel123")
        self.assertEqual(0, self.validar[0])
    
    #Caso esquina usuario no registrado y intenta ingresar al sistema.
    def test_ingresousuarionoregistrado(self):
        self.prueba.diccionario = None
        self.validar = self.prueba.IngresarUsuario("13-11223@usb.ve", "Manuel123")
        self.assertEqual(-4, self.validar[0])
    
    #Caso esquina usuario registrado y intenta ingresar al sistema con clave invalida
    def test_ingresousuarioclaveinvalida(self):
        self.registro = self.prueba.registrarUsuario("13-11223@usb.ve", "Manuel123","Manuel123")
        self.validar = self.prueba.IngresarUsuario("13-11223@usb.ve", "Manuel1234")
        self.assertEqual(-5, self.validar[0])
            

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()