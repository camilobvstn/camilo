class Tabla:
    def __init__(self, rut:str, nombre:str, sexo:str, cargo:str):
        self.__rut = rut
        self.__nombre = nombre
        self.__sexo = sexo
        self.__cargo = cargo

    def get_rut(self):
        return self.__rut
    def get_nombre(self):
        return self.__nombre
    def get_sexo(self):
        return self.__sexo
    def get_cargo(self):
        return self.__cargo
    
    def __str__(self):
        txt = f"\nRut: {self.__rut}"
        txt += f"\nNombre: {self.__nombre}"
        txt += f"\nSexo: {self.__sexo}"
        txt += f"\nCargo: {self.__cargo}"
        return txt