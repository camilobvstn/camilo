from Parentesco import Parentesco
import credenciales
import mysql.connector

class DAO_parentesco:

    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion=mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor=self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()
        

    def registrar_parentesco(self,p:Parentesco):
        self.__conectar()
        sql="INSERT INTO parentesco (parentesco) VALUES (%s)"
        valores=(p.get_parentesco(),)
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def modificar_parentesco(self,pa:Parentesco):
        self.__conectar()
        sql="UPDATE Parentesco SET parentesco=%s WHERE id_parentesco=%s"
        valores=(pa.get_parentesco(),pa.get_id_parentesco())
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def eliminar_parentesco(self,codigo):
        self.__conectar()
        sql="DELETE FROM Parentesco WHERE ..codigo.."
        valores=(codigo,)
        self.__cursor.execute(sql,valores)
        self.__cerrar()
        print("la condicion ha sido eliminado")

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM genero_trabajador"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Parentesco(t[1],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM parentesco"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Parentesco(t[1],t[0])
                usuario.append(u)
            return usuario
        else:
            return None