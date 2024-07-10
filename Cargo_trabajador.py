class Cargo_trabajador:
    def __init__(self, cargo_trabajador,fecha_ingreso, id_cargo:int=0):
        self.__cargo_trabajador = cargo_trabajador
        self.__fecha_ingreso = fecha_ingreso
        self.__id_cargo = id_cargo

    def get_cargo_trabajador(self):
        return self.__cargo_trabajador
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso
    def get_id_cargo(self):
        return self.__id_cargo
    
    def set_cargo_trabajador(self, newcargo_trabajador):
        self.__cargo_trabajador = newcargo_trabajador
    def set_fecha_ingreso(self, newfecha):
        self.__fecha_ingreso = newfecha

    def __str__(self):
        txt = f"\nCargo de trabajador: {self.__cargo_trabajador}"
        txt = f"\nFecha de ingreso: {self.__fecha_ingreso}" #Agregado: "Anthony"
        txt += f"\nId cargo: {self.__id_cargo}"
        return txt
