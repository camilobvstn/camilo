from Usuario import Usuario
from Tabla import Tabla
import credenciales
import mysql.connector

class DAO_usuario:

    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit() #cambios
        self.__conexion.close()

    def registrar_usuario(self,u:Usuario):
        self.__conectar()
        sql = "INSERT INTO usuario (nombre, rut, direccion, telefono, contraseña, id_cargo_trabajador, id_sexo_usuario, id_departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (u.get_nombre(),u.get_rut(),u.get_direccion(),u.get_telefono(),u.get_contraseña(),u.get_id_cargo_trabajador(),u.get_id_sexo_usuario(),u.get_id_departamento())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def modificar_usuario(self,u:Usuario):
        self.__conectar()
        sql = "UPDATE usuario SET nombre = %s, rut = %s, direccion = %s, telefono = %s, contraseña = %s WHERE id_usuario = %s"
        values = (u.get_nombre(),u.get_rut(),u.get_direccion(),u.get_telefono(),u.get_contraseña(),u.get_id_usuario())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def listar_usuario(self,rut):
        self.__conectar()
        sql = "SELECT * FROM usuario WHERE rut = %s"
        values = (rut,)
        self.__cursor.execute(sql,values)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Usuario(t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[0])
                usuario.append(u)
            return usuario
        else:
            return None
        
    def eliminar_usuario(self,rut):
        self.__conectar()
        sql = "START TRANSACTION; SET @id_usuario = (SELECT id_usuario FROM usuario WHERE rut = %s); SET @id_genero_trabajador = (SELECT genero_trabajador.id_sexo_usuario FROM usuario WHERE id_usuario = @id_usuario); SET @id_cargo_trabajador = (SELECT cargo_trabajador.id_cargo_trabajador FROM usuario WHERE id_usuario = @id_usuario); SET @id_departamento = (SELECT departamento.id_departamentos FROM usuario WHERE id_usuario = @id_usuario); SET @id_area = (SELECT area.id_area FROM departamento WHERE id_departamento = @id_departamento); DELETE FROM carga_familiar WHERE usuario.id_usuario = @id_usuario; DELETE FROM contacto_emergencia WHERE id_contacto_emergencia IN (SELECT contacto_emergencia.id_contacto_emergencia FROM usuario_has_contacto_emergencia WHERE usuario.id_usuario = @id_usuario); DELETE FROM usuario_has_contacto_emergencia WHERE usuario.id_usuario = @id_usuario; DELETE FROM usuario WHERE id_usuario = @id_usuario; DELETE FROM genero_trabajador WHERE id_sexo_usuario = @id_genero_trabajador; DELETE FROM cargo_trabajador WHERE id_cargo_trabajador = @id_cargo_trabajador; DELETE FROM departamento WHERE id_departamento = @id_departamento; DELETE FROM area WHERE id_area = @id_area; COMMIT;"
        values = (rut,)
        self.__cursos.execute(sql,values)
        self.__cerrar()
        
    def buscar_rut(self,rut):
        self.__conectar()
        sql = "SELECT * FROM usuario WHERE rut = %s"
        values = (rut,)
        self.__cursor.execute(sql,values)
        tupla = self.__cursor.fetchone()
        self.__cerrar()
        if tupla != []:
            for t in tupla:
                print(tupla)
                u = Usuario(t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[0])
            return u
        else:
            return None
        
    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM usuario"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Usuario(t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None
        
    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM usuario"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Usuario(t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[0])
                usuario.append(u)
            return usuario
        else:
            return None
        
    def tabla(self):
        self.__conectar()
        sql = "SELECT usuario.nombre AS Nombre, usuario.rut AS RUT, genero_trabajador.sexo AS Sexo, cargo_trabajador.cargo_trabajador AS Cargo FROM usuario JOIN genero_trabajador ON usuario.id_sexo_usuario = genero_trabajador.id_sexo_usuario JOIN cargo_trabajador ON usuario.id_cargo_trabajador = cargo_trabajador.id_cargo_trabajador;"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Tabla(t[1],t[0],t[2],t[3])
                usuario.append(u)
            return usuario
        else:
            return None
