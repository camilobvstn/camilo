from Carga_familiar import Carga_familiar
from Usuario import Usuario
import credenciales
import mysql.connector

class DAO_carga_familiar:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit() #cambios
        self.__conexion.close()

    def registrar_carga_familiar(self,cf:Carga_familiar):
        self.__conectar()
        sql = "INSERT INTO carga_familiar (nombre,id_usuario,id_parentesco,id_sexo_usuario) VALUES (%s,%s,%s,%s)"
        values = (cf.get_nombre(),cf.get_id_usuario(),cf.get_id_parentesco(),cf.get_id_sexo_usuario())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def modificar_carga_familiar(self, cf:Carga_familiar):
        self.__conectar()
        sql = "UPDATE carga_familiar SET nombre = %s WHERE idcargafamiliar = %s"
        values = (cf.get_nombre(),cf.get_id_cargafamiliar())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def eliminar_carga_familiar(self, u:Usuario):
        self.__conectar()
        sql = "DELETE FROM carga_familiar WHERE Usuario_id_usuario = (SELECT usuario_id FROM usuario WHERE rut = %s)"
        values = (u.get_rut(),)
        self.execute(sql,values)
        self.__cerrar()

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM carga_familiar"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Carga_familiar(t[1],t[2],t[3],t[4],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM carga_familiar"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Usuario(t[1],t[2],t[3],t[4],t[0])
                usuario.append(u)
            return usuario
        else:
            return None
    

    

