class Area:
    def __init__(self,nombre_area:str,id_area:int=0):
        self.__id_area = id_area
        self.__nombre_area= nombre_area

    def get_id_area(self):
        return self.__id_area
    def get_nombre_area(self):
        return self.__nombre_area

    def set_parentesco(self,newid_area):
        self.__id_area = newid_area
    def set_id_parentesco(self, newnombre_area): #Funcion con posible eliminacion
        self.__nombre_area = newnombre_area

    def __str__(self):
        txt = f"\nid area: {self.__id_area}"
        txt += f"\nnombre de area: {self.__nombre_area}"