class Departamento:
    def __init__(self,nombre_departamento:str,id_area:int=0,id_departamento:int=0):
        self.__id_departamento = id_departamento
        self.__nombre_departamento = nombre_departamento
        self.__id_area= id_area

    def get_id_departamento(self):
        return self.__id_departamento
    def get_nombre_departamento(self):
        return self.__nombre_departamento
    def get_id_area(self):
        return self.__id_area

    def set_id_departamento(self,newid_departamento):
        self.__id_departamento = newid_departamento
    def set_nombre_departamento(self, newnombre_departamento): #Funcion con posible eliminacion
        self.__nombre_departamento = newnombre_departamento
    def set_id_area(self, newid_area): #Funcion con posible eliminacion
        self.__id_area = newid_area

    def __str__(self):
        txt = f"\nid departamento: {self.__id_departamento}"
        txt += f"\nnombre departamento: {self.__nombre_departamento}"
        txt += f"\nid area: {self.__id_area}"