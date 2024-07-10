class Parentesco:
    def __init__(self, parentesco, id_parentesco:int=0):
        self.__parentesco = parentesco
        self.__id_parentesco = id_parentesco

    def get_parentesco(self):
        return self.__parentesco
    def get_id_parentesco(self):
        return self.__id_parentesco
    
    def set_parentesco(self,newparentesco):
        self.__parentesco = newparentesco
    def set_id_parentesco(self, newid_parentesco): #Funcion con posible eliminacion
        self.__id_parentesco = newid_parentesco

    def __str__(self):
        txt = f"\nparentesco: {self.__parentesco}"
        txt += f"\nid parentesco: {self.__id_parentesco}"