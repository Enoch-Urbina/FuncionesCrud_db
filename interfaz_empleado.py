import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from conexiondb import conectar

conexion = conectar()
cursor = conexion.cursor()

def obtener_empleados():
    cursor.execute("SELECT * FROM empleado")
    return cursor.fetchall()

def insertar_empleado(nombre, telefono, email, direccion, puesto):
    sql = "INSERT INTO empleado (nombre, telefono, email, direccion, puesto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, email, direccion, puesto))
    conexion.commit()

def actualizar_empleado(id_empleado, nombre, telefono, email, direccion, puesto):
    sql = "UPDATE empleado SET nombre=%s, telefono=%s, email=%s, direccion=%s, puesto=%s WHERE id_empleado=%s"
    cursor.execute(sql, (nombre, telefono, email, direccion, puesto, id_empleado))
    conexion.commit()

def eliminar_empleado(id_empleado):
    cursor.execute("DELETE FROM empleado WHERE id_empleado=%s", (id_empleado,))
    conexion.commit()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Empleado")
layout = QVBoxLayout()

nombre_input = QLineEdit()
telefono_input = QLineEdit()
email_input = QLineEdit()
direccion_input = QLineEdit()
puesto_input = QLineEdit()

layout.addWidget(QLabel("Nombre:"))
layout.addWidget(nombre_input)
layout.addWidget(QLabel("Teléfono:"))
layout.addWidget(telefono_input)
layout.addWidget(QLabel("Email:"))
layout.addWidget(email_input)
layout.addWidget(QLabel("Dirección:"))
layout.addWidget(direccion_input)
layout.addWidget(QLabel("Puesto:"))
layout.addWidget(puesto_input)

tabla = QTableWidget()
tabla.setColumnCount(6)
tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "Dirección", "Puesto"])
layout.addWidget(tabla)

boton_layout = QHBoxLayout()
btn_agregar = QPushButton("Agregar")
btn_actualizar = QPushButton("Actualizar")
btn_eliminar = QPushButton("Eliminar")
boton_layout.addWidget(btn_agregar)
boton_layout.addWidget(btn_actualizar)
boton_layout.addWidget(btn_eliminar)
layout.addLayout(boton_layout)

def cargar_tabla():
    tabla.setRowCount(0)
    datos = obtener_empleados()
    for fila_idx, fila in enumerate(datos):
        tabla.insertRow(fila_idx)
        for col_idx, valor in enumerate(fila):
            tabla.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))

def limpiar_inputs():
    nombre_input.clear()
    telefono_input.clear()
    email_input.clear()
    direccion_input.clear()
    puesto_input.clear()

def agregar_empleado():
    insertar_empleado(
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text(),
        puesto_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def actualizar_empleado_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un empleado para actualizar.")
        return
    id_empleado = int(tabla.item(fila, 0).text())
    actualizar_empleado(
        id_empleado,
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text(),
        puesto_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def eliminar_empleado_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un empleado para eliminar.")
        return
    id_empleado = int(tabla.item(fila, 0).text())
    eliminar_empleado(id_empleado)
    cargar_tabla()
    limpiar_inputs()

def cargar_datos_fila(fila, _):
    nombre_input.setText(tabla.item(fila, 1).text())
    telefono_input.setText(tabla.item(fila, 2).text())
    email_input.setText(tabla.item(fila, 3).text())
    direccion_input.setText(tabla.item(fila, 4).text())
    puesto_input.setText(tabla.item(fila, 5).text())

btn_agregar.clicked.connect(agregar_empleado)
btn_actualizar.clicked.connect(actualizar_empleado_ui)
btn_eliminar.clicked.connect(eliminar_empleado_ui)
tabla.cellClicked.connect(cargar_datos_fila)

ventana.setLayout(layout)
cargar_tabla()
ventana.show()
ventana.resize(800, 600)
sys.exit(app.exec())
