class Carga_familiar:
    def __init__(self, nombre, id_usuario:int=0, id_parentesco:int=0, id_sexo_usuario:int=0, id_cargafamiliar:int=0):
         self.__nombre = nombre
         self.__id_parentesco = id_parentesco
         self.__id_usuario = id_usuario
         self.__id_sexo_usuario = id_sexo_usuario
         self.__id_cargafamiliar = id_cargafamiliar

    def get_nombre(self):
        return self.__nombre 
    def get_id_parentesco(self):
        return self.__id_parentesco
    def get_id_usuario(self):
        return self.__id_usuario
    def get_id_sexo_usuario(self):
        return self.__id_sexo_usuario
    def get_id_cargafamiliar(self):
        return self.__id_cargafamiliar
    
    def set_nombre(self, newnombre):
        self.__nombre = newnombre
    def set_id_parentesco(self, newid_parentesco): #Funcion con posible eliminacion
        self.__id_parentesco = newid_parentesco
    def set_id_cargafamiliar(self,newid_carga_familiar): #Funcion con posible eliminacion
        self.__id_cargafamiliar = newid_carga_familiar
    
    def __str__(self):
        txt = f"\nnombre: {self.__nombre}"
        txt += f"\nid parentesco: {self.__id_parentesco}"
        txt += f"\nid usuario: {self.__id_usuario}"
        txt += f"\nid sexo usuario: {self.__id_sexo_usuario}"
        txt += f"\nid carga familiar: {self.__id_cargafamiliar}"
        return txt