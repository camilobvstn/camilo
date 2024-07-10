#<-------------------------------------------- IMPORT --------------------------------------------->

from Usuario import Usuario
from Genero_trabajador import Genero_trabajador
from Cargo_trabajador import Cargo_trabajador
from Contacto_emergencia import Contacto_emergencia
from Carga_familiar import Carga_familiar
from Parentesco import Parentesco
from Departamento import Departamento
from Area import Area

#<-------------------------------------------- IMPORT DAO ----------------------------------------->

from DAO_usuario import DAO_usuario
from DAO_genero import DAO_genero
from DAO_cargo_trabajador import DAO_cargo_trabajador
from DAO_emergencia import DAO_emergencia
from DAO_carga_familiar import DAO_carga_familiar
from DAO_parentesco import DAO_parentesco
from DAO_departamento import DAO_departamento
from DAO_area import DAO_area

#<-------------------------------------------- REGISTROS ------------------------------------------>

def registrar_usuario():
    d = DAO_usuario()
    nombre = input("Ingrese nombre: ")
    rut = input("ingrese rut: ")
    direccion = input("ingrese direccion: ")
    telefono = input("ingrese telefono: ")
    contraseña = input("ingrese contraseña: ")
    cargo_trabajador_id = buscar_id_cargo_trabajador()
    genero_trabajador_id = buscar_id_genero()
    departamento_id = buscar_id_departamento()
    u = Usuario(nombre, rut, direccion, telefono, contraseña,cargo_trabajador_id,genero_trabajador_id,departamento_id)
    d.registrar_usuario(u)

def registrar_genero():
    d = DAO_genero()
    sexo = input("ingrese sexo: ")
    u = Genero_trabajador(sexo)
    d.registrar_Genero_trabajador(u)

def registrar_cargo():
    d = DAO_cargo_trabajador()
    cargo = input("Ingrese su cargo: ")
    fecha = input("ingrese fecha de ingreso: ")
    u = Cargo_trabajador(cargo, fecha)
    d.registrar_Cargo_trabajador(u)

def registrar_parentesco():
    d = DAO_parentesco()
    parentesco = input("ingrese paresco: ")
    u = Parentesco(parentesco)
    d.registrar_parentesco(u)

def registrar_departamento():
    d = DAO_departamento()
    departamento = input("ingresa nombre del departamento: ")
    area = buscar_id_area()
    u = Departamento(departamento,area)
    d.registrar_departamento(u)

def registrar_area():
    d = DAO_area()
    nombre_area = input("ingresa area: ")
    u = Area(nombre_area)
    d.registrar_area(u)

def registrar_contacto_emergencia():
    d = DAO_emergencia()
    nombre = input("ingrese nombre: ")
    telefono = input("ingrese telefono: ")
    relacion = input("ingrese relacion con el trabajador: ")
    parentesco = buscar_id_parentesco()
    u = Contacto_emergencia(nombre,telefono,relacion,parentesco)
    d.registrar_contacto_emergencia(u)

def registrar_carga_familiar():
    d = DAO_carga_familiar()
    nombre = input("ingresa nombre de la carga familiar: ")
    id_usuario = buscar_id_usuario()
    id_parentesco = buscar_id_parentesco()
    id_sexo_usuario = buscar_id_genero()
    u = Carga_familiar(nombre,id_usuario,id_parentesco,id_sexo_usuario)
    d.registrar_carga_familiar(u)

#<-------------------------------------------- ELIMINAR REGISTROS ----------------------------------------->

def eliminar_usuario():
    d = DAO_usuario()
    rut = input("ingrese rut: ")
    r = d.buscar_rut(rut)
    if r != None:
        print("encontrado")
        d.eliminar_usuario(r)
    else:
        print("no se encontro nada")


#<---------------------------------------------- MOSTRAR TABLA ------------------------------------------->

def mostrar_tabla():
    d = DAO_usuario()
    r = d.tabla()
    for c in r:
        print("----------------------------------------------------------")
        print(c)
        print("----------------------------------------------------------")

#<-------------------------------------------- BUSQUEDA ID ----------------------------------------->

def buscar_id_cargo_trabajador():
    d = DAO_cargo_trabajador()
    r = d.buscar_id()
    return r
    
def buscar_id_genero():
    d = DAO_genero()
    r = d.buscar_id()
    return r
    
def buscar_id_departamento():
    d = DAO_departamento()
    r = d.buscar_id()
    return r
    
def buscar_id_parentesco():
    d = DAO_parentesco()
    r = d.buscar_id()
    return r

def buscar_id_usuario():
    d = DAO_usuario()
    r = d.buscar_id()
    return r
    
def buscar_id_carga_familiar():
    d = DAO_carga_familiar()
    r = d.buscar_id()
    return r

def buscar_id_area():
    d = DAO_area()
    r = d.buscar_id()
    return r

def buscar_cargo():
    rut = input("ingrese rut: ")
    d = DAO_cargo_trabajador()
    d = d.buscar_cargo(rut)
    print(d)

    
#<-------------------------------------------- LLAMADO AL REGISTRO ID ----------------------------------------->


buscar_cargo()
#eliminar_usuario()
#registrar_cargo()
#registrar_genero()
#registrar_departamento()
#registrar_usuario()
#registrar_parentesco()
#registrar_area()
#registrar_contacto_emergencia()
#registrar_carga_familiar()
#mostrar_tabla()

#<-------------------------------------------- LLAMADO A LA BUSQUEDA ID ----------------------------------------->

#buscar_id_cargo_trabajador()
#buscar_id_genero()
#buscar_id_usuario()
#buscar_id_parentesco()
#buscar_id_departamento()
#buscar_id_carga_familiar()




