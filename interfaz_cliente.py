import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from conexiondb import conectar

conexion = conectar()
cursor = conexion.cursor()

def obtener_cliente():
    cursor.execute("SELECT * FROM cliente")
    return cursor.fetchall()

def insertar_cliente(nombre, telefono, email, direccion):
    sql = "INSERT INTO cliente (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, email, direccion))
    conexion.commit()

def actualizar_cliente(id_cliente, nombre, telefono, email, direccion):
    sql = "UPDATE cliente SET nombre=%s, telefono=%s, email=%s, direccion=%s WHERE id_cliente=%s"
    cursor.execute(sql, (nombre, telefono, email, direccion, id_cliente))
    conexion.commit()

def eliminar_cliente(id_cliente):
    cursor.execute("DELETE FROM cliente WHERE id_cliente=%s", (id_cliente,))
    conexion.commit()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Cliente")
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
    datos = obtener_cliente()
    for fila_idx, fila in enumerate(datos):
        tabla.insertRow(fila_idx)
        for col_idx, valor in enumerate(fila):
            tabla.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))

def limpiar_inputs():
    nombre_input.clear()
    telefono_input.clear()
    email_input.clear()
    direccion_input.clear()

def agregar_cliente():
    insertar_cliente(
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def actualizar_cliente_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un cliente para actualizar.")
        return
    id_cliente = int(tabla.item(fila, 0).text())
    actualizar_cliente(
        id_cliente,
        nombre_input.text(),
        telefono_input.text(),
        email_input.text(),
        direccion_input.text()
    )
    cargar_tabla()
    limpiar_inputs()

def eliminar_cliente_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona un cliente para eliminar.")
        return
    id_cliente = int(tabla.item(fila, 0).text())
    eliminar_cliente(id_cliente)
    cargar_tabla()
    limpiar_inputs()

def cargar_datos_fila(fila, _):
    nombre_input.setText(tabla.item(fila, 1).text())
    telefono_input.setText(tabla.item(fila, 2).text())
    email_input.setText(tabla.item(fila, 3).text())
    direccion_input.setText(tabla.item(fila, 4).text())

btn_agregar.clicked.connect(agregar_cliente)
btn_actualizar.clicked.connect(actualizar_cliente_ui)
btn_eliminar.clicked.connect(eliminar_cliente_ui)
tabla.cellClicked.connect(cargar_datos_fila)

ventana.setLayout(layout)
cargar_tabla()
ventana.show()
ventana.resize(800, 600)
sys.exit(app.exec())
