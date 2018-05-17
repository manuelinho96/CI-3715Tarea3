import re

# Definicion de la clase seguridad
class Seguridad:
    
    diccionario = { } # Dicc donde se guarda la informacion de los usuarios registrados
    
    # Funcion que dado un correo y dos claves
    # Si la informacion es correcta registra al usuario en el diccionario
    def registrarUsuario(self,correo,clave1,clave2):
        # Se verifica que el correo y las claves sean validas
        esvalido = self.validarargumentos(correo, clave1, clave2)
        if esvalido[0] != 0:
            return esvalido
        #Se verifica que el usuario no este registrado en el sistema
        if self.diccionario.get(correo) != None:
            return (-6,"Usuario ya registrado")
        # No hubo errores, se codifica el string con un reverse
        claveCodificada = clave1[::-1]
        # Se registra el usuario
        self.diccionario[correo] = claveCodificada
        return (0,"Usuario registrado con exito")
    
    # Funcion que dado un correo y una clave
    # realiza el intento de inicio de sesion de un usuario
    def IngresarUsuario(self,correo,clave):
        # Se verifica que el correo y la clave sean validas
        esvalido = self.validarargumentos(correo, clave, clave)
        if esvalido[0] != 0:
            return esvalido
        # Si es valido se verifica que el usuario este registrado
        try:
            if self.diccionario.get(correo) == None:
                raise
        except:
            string="Usuario invalido"
            print(string)
            return (-4,string)
        # Se desencripta la clave ingresada y si no coincide con la del diccionario
        # se arroja un error.
        try:
            assert(self.diccionario.get(correo) == clave[::-1])
        except:
            string = "Clave inválida"
            print(string)
            return (-5,string)
        # El usuario realizo un login exitoso
        string="Usuario Aceptado"
        print(string)
        return (0,string)
    
    # Funcion que verifica que el correo sea valido y
    # la contraseña cumpla con los requisitos especificados
    def validarargumentos(self, correo, clave1, clave2):
        # Se verifica que el correo es valido.
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
        except:
            string = "Correo electrónico inválido."
            print(string)
            return (-1,string)
        # Se verifica que las claves coinciden.
        try:
            assert(clave1==clave2)
        except:
            string = "Las claves no coinciden."
            print(string)
            return (-2,string)
        # Se verifican las condiciones especiales de la clave
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
                    string = "La clave debe tener mas de 8 caracteres"
                elif (len(clave1) > 16):
                    string = "La clave debe tener menos de 16 caracteres"
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
            return (-3,string)
        # La validacion fue exitosa
        return (0,"")