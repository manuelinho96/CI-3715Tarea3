from django.db import models
import re

# Create your models here.
class Seguridad:
    
    def registrarUsuario(self,correo,clave1,clave2):
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
        except:
            print("Formato de correo no válido.")
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
            assert(len(clave1) >= 8 and len(clave1) <= 16)
            for char in clave1:
                if char.isdigit():
                    digitos += 1
                elif char.isupper():
                    mayusculas += 1
                elif char.islower():
                    minusculas += 1
                else:
                    raise
            assert(digitos >= 1 and mayusculas >= 1 and minusculas >= 1 and mayusculas + minusculas >= 3)
        except:
            print("La clave no es valida")
            return -3
        
        return 0