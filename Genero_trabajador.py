class Genero_trabajador:
    def __init__(self, sexo, id_sexo_usuario:int=0):
        self.__sexo = sexo
        self.__id_sexo_usuario = id_sexo_usuario

    def get_sexo(self):
        return self.__sexo
    def get_id_sexo_usuario(self):
        return self.__id_sexo_usuario
    
    def set_sexo(self, newsexo):
        self.__sexo = newsexo
    def set_id_sexo_usuario(self, newid_sexo_usuario): #Posible eliminacion
        self.__id_sexo_usuario = newid_sexo_usuario

    def __str__(self):
        txt = f"\nsexo: {self.__sexo}"
        txt += f"\nid del sexo: {self.__id_sexo_usuario}"
        return txt

