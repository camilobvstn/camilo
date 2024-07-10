class Contacto_emergencia:
    def __init__(self, nombre, telefono,relacion_trabajador:str, id_parentesco:int=0,id_contacto_emergencia:int=0):
        self.__nombre = nombre
        self.__id_parentesco = id_parentesco
        self.__telefono = telefono
        self.__relacion_trabajador = relacion_trabajador
        self.__id_contacto_emergencia = id_contacto_emergencia

    def get_nombre(self):
        return self.__nombre
    def get_id_parentesco(self):
        return self.__id_parentesco
    def get_telefono(self):
        return self.__telefono
    def get_id_contacto_emergencia(self):
        return self.__id_contacto_emergencia
    def get_relacion_trabajador(self):
        return self.__relacion_trabajador
    
    def set_nombre(self,newnombre):
        self.__nombre = newnombre
    def set_id_parentesco(self, newid_parentesco):
        self.__id_parentesco = newid_parentesco
    def set_telefono(self, newtelefono):
        self.__telefono = newtelefono
    def set_id_contacto_emergencia(self, newid_contacto_emergencia): #Funcion con posible eliminacion
        self.__id_contacto_emergencia = newid_contacto_emergencia
    def set_relacion_trabajador(self,newrelacion):
        self.__relacion_trabajador = newrelacion

    def __str__(self):
        txt = f"\nnombre: {self.__nombre}"
        txt += f"\ntelefono: {self.__telefono}"
        txt += f"\nrelacion con el trabajador: {self.__relacion_trabajador}"
        txt += f"\nid parentesco: {self.__id_parentesco}"
        txt += f"\nid contacto de emergencia: {self.__id_contacto_emergencia}"
        return txt