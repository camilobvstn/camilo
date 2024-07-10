from Contacto_emergencia import Contacto_emergencia
import credenciales 
import mysql.connector
class DAO_emergencia:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion=mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor=self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def registrar_contacto_emergencia(self,c:Contacto_emergencia):
        self.__conectar()
        sql="INSERT INTO Contacto_emergencia (nombre,telefono,id_parentesco,relacion_trabajador) VALUES (%s,%s,%s,%s)"
        valores=(c.get_nombre(),c.get_telefono(),c.get_id_parentesco(),c.get_relacion_trabajador())
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def actualizar(self,co:Contacto_emergencia):
        self.__conectar()
        sql="UPDATE Contacto_emergencian SET nombre=%s, telefono=%s"
        valores=(co.get_nombre(),co.get_telefono())
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def eliminar_contacto_emergencia(self,codigo):
        self.__conectar()
        sql= "DELETE FROM contacto_emergencia WHERE usuario_id = (SELECT usuario_id FROM usuario WHERE rut = %s)"
        valores=(codigo,)
        self.__cursor.execute(sql,valores)
        self.__cerrar()
        print("la condicion ha sido eliminado")

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM contacto_emergencia"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Contacto_emergencia(t[1],t[2],t[4],t[3],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM contacto_emergencia"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Contacto_emergencia(t[1],t[2],t[4],t[3],t[0])
                usuario.append(u)
            return usuario
        else:
            return None