import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from conexiondb import conectar

conexion = conectar()
cursor = conexion.cursor()

def obtener_proveedor():
    cursor.execute("SELECT * FROM proveedor")
    return cursor.fetchall()

def insertar_proveedor(nombre, telefono, email, direccion):
    sql = "INSERT INTO proveedor (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, email, direccion))
    conexion.commit()

def actualizar_proveedor(id_proveedor, nombre, telefono, email, direccion):
    sql = "UPDATE proveedor SET nombre=%s, telefono=%s, email=%s, direccion=%s WHERE id_proveedor=%s"
    cursor.execute(sql, (nombre, telefono, email, direccion, id_proveedor))
    conexion.commit()

def eliminar_proveedor(id_proveedor):
    cursor.execute("DELETE FROM proveedor WHERE id_proveedor=%s", (id_proveedor,))
    conexion.commit()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Proveedor")
layout = QVBoxLayout()

nombre_input = QLineEdit()
telefono_input = QLineEdit()
email_input = QLineEdit()
direccion_input = QLineEdit()

layout.addWidget(QLabel("Nombre:"))
layout.addWidget(nombre_input)
layout.addWidget(QLabel("Teléfono:"))
layout.addWidget(telefono_input)
layout.addWidget(QLabel("Email:"))
layout.addWidget(email_input)
layout.addWidget(QLabel("Dirección:"))
layout.addWidget(direccion_input)

tabla = QTableWidget()
tabla.setColumnCount(5)
tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "Dirección"])
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
    datos = obtener_proveedor()
    for fila_idx, fila in enumerate(datos):
        tabla.insertRow(fila_idx)
        for col_idx, valor in enumerate(fila):
            tabla.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))

def limpiar_inputs():
    nombre_input.clear()
    telefono_input.clear()
    email_input.clear()
    direccion_input.clear()

def agregar_proveedor():
    insertar_proveedor(
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def actualizar_proveedor_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un proveedor para actualizar.")
        return
    id_proveedor = int(tabla.item(fila, 0).text())
    actualizar_proveedor(
        id_proveedor,
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def eliminar_proveedor_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un proveedor para eliminar.")
        return
    id_proveedor = int(tabla.item(fila, 0).text())
    eliminar_proveedor(id_proveedor)
    cargar_tabla()
    limpiar_inputs()

def cargar_datos_fila(fila, _):
    nombre_input.setText(tabla.item(fila, 1).text())
    telefono_input.setText(tabla.item(fila, 2).text())
    email_input.setText(tabla.item(fila, 3).text())
    direccion_input.setText(tabla.item(fila, 4).text())

btn_agregar.clicked.connect(agregar_proveedor)
btn_actualizar.clicked.connect(actualizar_proveedor_ui)
btn_eliminar.clicked.connect(eliminar_proveedor_ui)
tabla.cellClicked.connect(cargar_datos_fila)

ventana.setLayout(layout)
cargar_tabla()
ventana.show()
ventana.resize(800, 600)
sys.exit(app.exec())
