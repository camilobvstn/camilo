class Usuario:
    def __init__(self, nombre:str, rut:str, direccion:str, telefono:int, constraseña:str,id_cargo_trabajador, id_sexo_usuario ,id_departamento , id_usuario:int=0):
            self.__rut = rut
            self.__id_sexo_usuario = id_sexo_usuario #Posible eliminacion
            self.__id_cargo_trabajador = id_cargo_trabajador
            self.__nombre = nombre
            self.__direccion = direccion
            self.__telefono = telefono
            self.__contraseña = constraseña
            self.__id_usuario = id_usuario
            self.__id_departamento = id_departamento

    def get_rut(self):
        return self.__rut
    def get_id_sexo_usuario(self): #Posible eliminacion
        return self.__id_sexo_usuario
    def get_id_cargo_trabajador(self):
        return self.__id_cargo_trabajador
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    def get_usuario(self):
        return self.__id_usuario
    def get_contraseña(self):
        return self.__contraseña 
    def get_id_usuario(self):
        return self.__id_usuario
    def get_id_departamento(self):
        return self.__id_departamento
    
    def set_rut(self, newrut):
        self.__rut = newrut
    def set_id_sexo_usuario(self,newid_sexo_usuario): #Posible eliminacion
        self.__id_sexo_usuario = newid_sexo_usuario
    def set_nombre(self, newnombre):
        self.__nombre = newnombre
    def set_direccion(self, newdireccion):
        self.__direccion = newdireccion
    def set_id_usuario(self, newid_usuario): #Posible eliminacion
        self.__id_usuario = newid_usuario
    def set_contraseña(self, newcontraseña):
        self.__contraseña = newcontraseña

    def __str__(self):
        txt = f"\nrut: {self.__rut}"
        txt += f"\nid sexo: {self.__id_sexo_usuario}"
        txt += f"\nnombre: {self.__nombre}"
        txt += f"\ndireccion: {self.__direccion}"
        txt += f"\nid usuario: {self.__id_usuario}"
        txt += f"\ncontraseña: {self.__contraseña}"
        txt += f"\nid departamento: {self.__id_departamento}"
        return txt
    