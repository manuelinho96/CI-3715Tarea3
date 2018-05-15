from django.db import models
import re

# Create your models here.
class Seguridad (models.Model):
    
    diccionario = { }
    
    def registrarUsuario(self,correo,clave1,clave2):
        esvalido = self.validarargumentos(correo, clave1, clave2)
        if esvalido != 0:
            return esvalido
        claveCodificada = clave1[::-1]
        self.diccionario[correo] = claveCodificada
        return 0
    
    def IngresarUsuario(self,correo,clave):
        esvalido = self.validarargumentos(correo, clave, clave)
        if esvalido != 0:
            return esvalido
        try:
            if self.diccionario.get(correo) == None:
                raise
        except:
            print("Usuario invalido")
            return -4
        try:
            assert(self.diccionario.get(correo) == clave[::-1])
        except:
            print("Clave inválida")
            return -5
        print("Usuario Aceptado")
        return 0
    
    def validarargumentos(self, correo, clave1, clave2):
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
        except:
            print("Correo electrónico inválido.")
            return -1
        try:
            assert(clave1==clave2)
        except:
            print("Las claves no coinciden.")
            return -2
        try:
            minusculas = 0
            mayusculas = 0
            digitos = 0
            string = ""
            assert(len(clave1) >= 8 and len(clave1) <= 16)
            for char in clave1:
                if char.isdigit():
                    digitos += 1
                elif char.isupper():
                    mayusculas += 1
                elif char.islower():
                    minusculas += 1
                else:
                    string = "No deben haber caracteres especiales en la clave."
                    raise
            assert(digitos >= 1 and mayusculas >= 1 and minusculas >= 1 and mayusculas + minusculas >= 3)
        except:
            if (string==""):
                if (len(clave1) < 8):
                    string = "La clave tiene menos de 8 caracteres"
                elif (len(clave1) > 16):
                    string = "La clave tiene mas de 16 caracteres"
                else:
                    if (digitos < 1):
                        string = "La clave debe tener al menos un digito"
                    elif (mayusculas < 1):
                        string = "La clave debe tener al menos una letra mayuscula"
                    elif (minusculas < 1):
                        string = "La clave debe tener al menos una letra minuscula"
                    elif(mayusculas+minusculas < 3):
                        string = "La clave debe tener al menos tres letras"
            print("Clave Inválida: " + string)
            return -3
        return 0