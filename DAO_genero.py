from Genero_trabajador import Genero_trabajador
import credenciales
import mysql.connector
class DAO_genero:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion=mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor=self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def registrar_Genero_trabajador(self,c:Genero_trabajador):
        self.__conectar()
        sql="INSERT INTO genero_trabajador (sexo) VALUES (%s)"
        valores=(c.get_sexo(),)
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def modificar_Genero_trabajador(self,co:Genero_trabajador):
        self.__conectar()
        sql="UPDATE Genero_trabajador SET sexo=%s WHERE id_sexo_usuario=%s"
        valores=(co.get_sexo(),co.get_id_sexo_usuario())
        self.__cursor.execute(sql,valores)
        self.__cerrar()

    def eliminar_Genero_trabajador(self,codigo):
        self.__conectar()
        sql="DELETE FROM Genero_trabajador WHERE ..codigo.."
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
                u = Genero_trabajador(t[1],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM genero_trabajador"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Genero_trabajador(t[1],t[0])
                usuario.append(u)
            return usuario
        else:
            return None