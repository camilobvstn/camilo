import sys
import re
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate

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



app = QtWidgets.QApplication([])
login = uic.loadUi("Credenciales2.ui")
admin= uic.loadUi("admin.ui")
empleado=uic.loadUi("empleado.ui")
rrhh=uic.loadUi("rrhh.ui")


admin.stackedWidget.setCurrentIndex(0)

empleado.stackedWidget.setCurrentIndex(0)
rrhh.stackedWidget.setCurrentIndex(0)


def cerrar_programa():
    QtWidgets.QApplication.quit()

def ir_a_laboral():
    admin.stackedWidget.setCurrentIndex(5)

def ir_a_filtro():
    admin.stackedWidget.setCurrentIndex(2)

def ir_a_inicio():
    admin.stackedWidget.setCurrentIndex(0)

def ir_a_lista():
    admin.stackedWidget.setCurrentIndex(1)  # Cambia a la página de la lista en el QStackedWidget

def ir_a_form_personal():
    admin.stackedWidget.setCurrentIndex(4)  # Cambia a la página form_personal en el QStackedWidget

def validar_inputs():
    nombre = admin.input_nombre.text().strip()
    rut = admin.input_rut.text().strip()
    direccion = admin.input_dire.text().strip()
    telefono = admin.input_tel.text().strip()
    sexo = admin.input_sexo.currentText()  # Obtener el texto seleccionado del combo box
    valid = True

# Validar el campo de nombre
    if len(nombre) == 0:
        admin.error_nombre.setText("El nombre no puede estar vacío.")
        valid = False
    elif any(char.isdigit() for char in nombre):
        admin.error_nombre.setText("El nombre no puede contener números.")
        valid = False
    else:
        admin.error_nombre.setText("")  # Borrar mensaje de error

    # Validar el campo de teléfono
    if len(telefono) == 0:
        admin.error_telefono.setText("Ingrese un número de teléfono.")
        valid = False
    elif not telefono.isdigit() or len(telefono) != 9:
        admin.error_telefono.setText("El teléfono debe tener 9 dígitos y sin letras.")
        valid = False
    else:
        admin.error_telefono.setText("")  # Borrar mensaje de error

    # Validar el campo de RUT
    if len(rut) == 0:
        admin.error_rut.setText("Ingrese un RUT.")
        valid = False
    elif not re.match(r"^\d{7,8}-\d{1}$", rut):
        admin.error_rut.setText("Formato incorrecto de RUT. Ejemplo: 12345678-9")
        valid = False
    else:
        admin.error_rut.setText("")  # Borrar mensaje de error

    # Validar el campo de dirección
    if len(direccion) == 0:
        admin.error_dire.setText("Ingrese una dirección.")
        valid = False
    else:
        admin.error_dire.setText("")  # Borrar mensaje de error

    # Validar el campo de sexo
    if sexo == "-":
        admin.error_sexo.setText("Seleccione un sexo.")
        valid = False
    else:
        admin.error_sexo.setText("")  # Borrar mensaje de error

    if valid:
        admin.stackedWidget.setCurrentIndex(5)  # Cambiar a la página form_laboral si todo es válido

def validar_form_laboral(self):
    cargo = admin.input_cargo.text().strip()
    departamento = admin.input_departamento.text().strip()
    fecha = admin.input_fecha.date()
    laboral = admin.input_laboral.currentText()  # Obtener el texto seleccionado del combo box
    valid = True

# Validar el campo de cargo
    if len(cargo) == 0:
        admin.error_cargo.setText("Ingrese un cargo.")
        valid = False
    else:
        admin.error_cargo.setText("")  # Borrar mensaje de error

    # Validar el campo de departamento
    if len(departamento) == 0:
        admin.error_departamento.setText("Ingrese un departamento.")
        valid = False
    else:
        admin.error_departamento.setText("")  # Borrar mensaje de error

    # Validar el campo de fecha
    if fecha > QDate.currentDate():
        admin.error_fecha.setText("La fecha no puede ser superior a la actual.")
        valid = False
    else:
        admin.error_fecha.setText("")  # Borrar mensaje de error

    # Validar el campo de laboral
    if laboral == "-":
        admin.error_laboral.setText("Seleccione una opción de contrato laboral.")
        valid = False
    else:
        admin.error_laboral.setText("")  # Borrar mensaje de error

    if valid:
        admin.stackedWidget.setCurrentIndex(7)  # Cambiar a la página form_emergencia si todo es válido

def validar_form_emergencia(self):
    telefono_emergencia = admin.input_telefonoemergencia.text().strip()
    nombre_emergencia = admin.input_nombreemergencia.text().strip()
    parentesco = admin.input_parentesco.text().strip()
    valid = True

# Validar el campo de teléfono de emergencia
    if len(telefono_emergencia) == 0:
        admin.error_telefonoemergencia.setText("Ingrese un número de teléfono de emergencia.")
        valid = False
    elif not telefono_emergencia.isdigit() or len(telefono_emergencia) != 9:
        admin.error_telefonoemergencia.setText("El teléfono de emergencia debe tener 9 dígitos y sin letras.")
        valid = False
    else:
        admin.error_telefonoemergencia.setText("")  # Borrar mensaje de error

    # Validar el campo de nombre de emergencia
    if len(nombre_emergencia) == 0:
        admin.error_nombrecontacto.setText("Ingrese un nombre de emergencia.")
        valid = False
    elif any(char.isdigit() for char in nombre_emergencia):
        admin.error_nombrecontacto.setText("El nombre de emergencia no puede contener números.")
        valid = False
    else:
        admin.error_nombrecontacto.setText("")  # Borrar mensaje de error

    # Validar el campo de parentesco
    if len(parentesco) == 0:
        admin.error_parentesco.setText("Ingrese el parentesco.")
        valid = False
    else:
        admin.error_parentesco.setText("")  # Borrar mensaje de error

    if valid:
        admin.stackedWidget.setCurrentIndex(8)  # Cambiar a la página siguiente si todo es válido

def limpiar_campos(self):
# Limpiar campos del formulario personal
    admin.input_nombre.clear()
    admin.input_rut.clear()
    admin.input_dire.clear()
    admin.input_tel.clear()
    admin.input_sexo.setCurrentIndex(0)
    admin.error_nombre.clear()
    admin.error_rut.clear()
    admin.error_dire.clear()
    admin.error_telefono.clear()
    admin.error_sexo.clear()

    # Limpiar campos del formulario laboral
    admin.input_cargo.clear()
    admin.input_departamento.clear()
    admin.input_fecha.setDate(QDate.currentDate())
    admin.input_laboral.setCurrentIndex(0)
    admin.error_cargo.clear()
    admin.error_departamento.clear()
    admin.error_fecha.clear()
    admin.error_laboral.clear()

    # Limpiar campos del formulario de emergencia
    admin.input_telefonoemergencia.clear()
    admin.input_nombreemergencia.clear()
    admin.input_parentesco.clear()
    admin.error_telefonoemergencia.clear()
    admin.error_nombrecontacto.clear()
    admin.error_parentesco.clear()

def cerrar_programa():
    QtWidgets.QApplication.quit()


def ir_a_inicio1():
    empleado.stackedWidget.setCurrentIndex(0)

def ir_a_lista1():
    empleado.stackedWidget.setCurrentIndex(1)  # Cambia a la página de la lista en el QStackedWidget




def ir_a_inicio2():
    rrhh.stackedWidget.setCurrentIndex(0)

def ir_a_lista2():
    rrhh.stackedWidget.setCurrentIndex(1)  # Cambia a la página de la lista en el QStackedWidget

def ir_a_form_personal2():
    rrhh.stackedWidget.setCurrentIndex(4)  # Cambia a la página form_personal en el QStackedWidget

def validar_inputs2():
    nombre = rrhh.input_nombre.text().strip()
    rut = rrhh.input_rut.text().strip()
    direccion = rrhh.input_dire.text().strip()
    telefono = rrhh.input_tel.text().strip()
    sexo = rrhh.input_sexo.currentText()  # Obtener el texto seleccionado del combo box
    valid = True

# Validar el campo de nombre
    if len(nombre) == 0:
        rrhh.error_nombre.setText("El nombre no puede estar vacío.")
        valid = False
    elif any(char.isdigit() for char in nombre):
        rrhh.error_nombre.setText("El nombre no puede contener números.")
        valid = False
    else:
        rrhh.error_nombre.setText("")  # Borrar mensaje de error

    # Validar el campo de teléfono
    if len(telefono) == 0:
        rrhh.error_telefono.setText("Ingrese un número de teléfono.")
        valid = False
    elif not telefono.isdigit() or len(telefono) != 9:
        rrhh.error_telefono.setText("El teléfono debe tener 9 dígitos y sin letras.")
        valid = False
    else:
        rrhh.error_telefono.setText("")  # Borrar mensaje de error

    # Validar el campo de RUT
    if len(rut) == 0:
        rrhh.error_rut.setText("Ingrese un RUT.")
        valid = False
    elif not re.match(r"^\d{7,8}-\d{1}$", rut):
        rrhh.error_rut.setText("Formato incorrecto de RUT. Ejemplo: 12345678-9")
        valid = False
    else:
        rrhh.error_rut.setText("")  # Borrar mensaje de error

    # Validar el campo de dirección
    if len(direccion) == 0:
        rrhh.error_dire.setText("Ingrese una dirección.")
        valid = False
    else:
        rrhh.error_dire.setText("")  # Borrar mensaje de error

    # Validar el campo de sexo
    if sexo == "-":
        rrhh.error_sexo.setText("Seleccione un sexo.")
        valid = False
    else:
        rrhh.error_sexo.setText("")  # Borrar mensaje de error

    if valid:
        rrhh.stackedWidget.setCurrentIndex(5)  # Cambiar a la página form_laboral si todo es válido

def validar_form_laboral2(self):
    cargo = rrhh.input_cargo.text().strip()
    departamento = rrhh.input_departamento.text().strip()
    fecha = rrhh.input_fecha.date()
    laboral = rrhh.input_laboral.currentText()  # Obtener el texto seleccionado del combo box
    valid = True

# Validar el campo de cargo
    if len(cargo) == 0:
        rrhh.error_cargo.setText("Ingrese un cargo.")
        valid = False
    else:
        rrhh.error_cargo.setText("")  # Borrar mensaje de error

    # Validar el campo de departamento
    if len(departamento) == 0:
        rrhh.error_departamento.setText("Ingrese un departamento.")
        valid = False
    else:
        rrhh.error_departamento.setText("")  # Borrar mensaje de error

    # Validar el campo de fecha
    if fecha > QDate.currentDate():
        rrhh.error_fecha.setText("La fecha no puede ser superior a la actual.")
        valid = False
    else:
        rrhh.error_fecha.setText("")  # Borrar mensaje de error

    # Validar el campo de laboral
    if laboral == "-":
        rrhh.error_laboral.setText("Seleccione una opción de contrato laboral.")
        valid = False
    else:
        rrhh.error_laboral.setText("")  # Borrar mensaje de error

    if valid:
        rrhh.stackedWidget.setCurrentIndex(7)  # Cambiar a la página form_emergencia si todo es válido

def validar_form_emergencia2(self):
    telefono_emergencia = rrhh.input_telefonoemergencia.text().strip()
    nombre_emergencia = rrhh.input_nombreemergencia.text().strip()
    parentesco = rrhh.input_parentesco.text().strip()
    valid = True

# Validar el campo de teléfono de emergencia
    if len(telefono_emergencia) == 0:
        rrhh.error_telefonoemergencia.setText("Ingrese un número de teléfono de emergencia.")
        valid = False
    elif not telefono_emergencia.isdigit() or len(telefono_emergencia) != 9:
        rrhh.error_telefonoemergencia.setText("El teléfono de emergencia debe tener 9 dígitos y sin letras.")
        valid = False
    else:
        rrhh.error_telefonoemergencia.setText("")  # Borrar mensaje de error

    # Validar el campo de nombre de emergencia
    if len(nombre_emergencia) == 0:
        rrhh.error_nombrecontacto.setText("Ingrese un nombre de emergencia.")
        valid = False
    elif any(char.isdigit() for char in nombre_emergencia):
        rrhh.error_nombrecontacto.setText("El nombre de emergencia no puede contener números.")
        valid = False
    else:
        rrhh.error_nombrecontacto.setText("")  # Borrar mensaje de error

    # Validar el campo de parentesco
    if len(parentesco) == 0:
        rrhh.error_parentesco.setText("Ingrese el parentesco.")
        valid = False
    else:
        rrhh.error_parentesco.setText("")  # Borrar mensaje de error

    if valid:
        rrhh.stackedWidget.setCurrentIndex(8)  # Cambiar a la página siguiente si todo es válido

def limpiar_campos2(self):
# Limpiar campos del formulario personal
    rrhh.input_nombre.clear()
    rrhh.input_rut.clear()
    rrhh.input_dire.clear()
    rrhh.input_tel.clear()
    rrhh.input_sexo.setCurrentIndex(0)
    rrhh.error_nombre.clear()
    rrhh.error_rut.clear()
    rrhh.error_dire.clear()
    rrhh.error_telefono.clear()
    rrhh.error_sexo.clear()

    # Limpiar campos del formulario laboral
    rrhh.input_cargo.clear()
    rrhh.input_departamento.clear()
    rrhh.input_fecha.setDate(QDate.currentDate())
    rrhh.input_laboral.setCurrentIndex(0)
    rrhh.error_cargo.clear()
    rrhh.error_departamento.clear()
    rrhh.error_fecha.clear()
    rrhh.error_laboral.clear()

    # Limpiar campos del formulario de emergencia
    rrhh.input_telefonoemergencia.clear()
    rrhh.input_nombreemergencia.clear()
    rrhh.input_parentesco.clear()
    rrhh.error_telefonoemergencia.clear()
    rrhh.error_nombrecontacto.clear()
    rrhh.error_parentesco.clear()

def ir_a_laboral2():
    rrhh.stackedWidget.setCurrentIndex(5)

def buscar_cargo(valor):
    d = DAO_cargo_trabajador()
    r = d.buscar_cargo(valor)
    return r

def gui_entrar_admin():
    login.hide()
    admin.show()

def gui_entrar_empleado():
    login.hide()
    empleado.show()

def gui_entrar_rrhh():
    login.hide()
    rrhh.show()

def gui_login():

    run = login.InputEmail.text()
    password = login.InputConstra.text()
    valid = True
    if len(run) == 0:
        login.ErrorEmail.setText("Ingrese un R.U.N.")
        valid = False
    else:
        login.ErrorEmail.setText("")
    
    if password != "123":
        login.ErrorConstra.setText("Contraseña incorrecta.")
        valid = False
    else:
        login.ErrorConstra.setText("")
    
    if valid:
        if buscar_cargo(run) == "empleado":
            gui_entrar_empleado()
        elif buscar_cargo(run) == "administrador":
            gui_entrar_admin()
        elif buscar_cargo(run) == "rrhh":
            gui_entrar_rrhh()

empleado.btn_lista.clicked.connect(ir_a_lista1)
empleado.btn_principal.clicked.connect(ir_a_inicio1)  # Conectar el botón para limpiar campos
empleado.btn_salir.clicked.connect(cerrar_programa)



rrhh.btn_lista.clicked.connect(ir_a_lista2)
rrhh.bt_registrartrabajador.clicked.connect(ir_a_form_personal2)
rrhh.btn_personal.clicked.connect(validar_inputs2)
rrhh.btn_laboral.clicked.connect(validar_form_laboral2)
rrhh.btn_principal.clicked.connect(ir_a_inicio2)
rrhh.btn_emergencia.clicked.connect(validar_form_emergencia2)
rrhh.pushButton_6.clicked.connect(ir_a_form_personal2)
rrhh.pushButton_6.clicked.connect(limpiar_campos2)  # Conectar el botón para limpiar campos
rrhh.btnAtras1.clicked.connect(ir_a_form_personal2)
rrhh.btnAtras1_2.clicked.connect(ir_a_laboral2)
rrhh.btn_salir.clicked.connect(cerrar_programa)

admin.btn_lista.clicked.connect(ir_a_lista)
admin.bt_registrartrabajador.clicked.connect(ir_a_form_personal)
admin.btn_personal.clicked.connect(validar_inputs)
admin.btn_laboral.clicked.connect(validar_form_laboral)
admin.btn_principal.clicked.connect(ir_a_inicio)
admin.btn_emergencia.clicked.connect(validar_form_emergencia)
admin.pushButton_6.clicked.connect(ir_a_form_personal)
admin.pushButton_6.clicked.connect(limpiar_campos)  # Conectar el botón para limpiar campos
admin.btn_buscar.clicked.connect(ir_a_filtro)
admin.btnAtras1.clicked.connect(ir_a_form_personal)
admin.btnAtras1_2.clicked.connect(ir_a_laboral)
admin.btn_salir.clicked.connect(cerrar_programa)

login.btnIngresar.clicked.connect(gui_login)
login.show()
app.exec()