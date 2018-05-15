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
        
        return 0