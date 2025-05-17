import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from conexiondb import conectar

conexion = conectar()
cursor = conexion.cursor()

def obtener_categorias():
    cursor.execute("SELECT * FROM categoria")
    return cursor.fetchall()

def insertar_categoria(nombre):
    sql = "INSERT INTO categoria (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()

def actualizar_categoria(id_categoria, nombre):
    sql = "UPDATE categoria SET nombre=%s WHERE id_categoria=%s"
    cursor.execute(sql, (nombre, id_categoria))
    conexion.commit()

def eliminar_categoria(id_categoria):
    cursor.execute("DELETE FROM categoria WHERE id_categoria=%s", (id_categoria,))
    conexion.commit()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Categorías")
layout = QVBoxLayout()

nombre_input = QLineEdit()

layout.addWidget(QLabel("Nombre:"))
layout.addWidget(nombre_input)

tabla = QTableWidget()
tabla.setColumnCount(2)
tabla.setHorizontalHeaderLabels(["ID", "Nombre"])
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
    datos = obtener_categorias()
    for fila_idx, fila in enumerate(datos):
        tabla.insertRow(fila_idx)
        for col_idx, valor in enumerate(fila):
            tabla.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))

def limpiar_inputs():
    nombre_input.clear()

def agregar_categoria():
    insertar_categoria(nombre_input.text())
    cargar_tabla()
    limpiar_inputs()

def actualizar_categoria_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una categoría para actualizar.")
        return
    id_categoria = int(tabla.item(fila, 0).text())
    actualizar_categoria(id_categoria, nombre_input.text())
    cargar_tabla()
    limpiar_inputs()

def eliminar_categoria_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una categoría para eliminar.")
        return
    id_categoria = int(tabla.item(fila, 0).text())
    eliminar_categoria(id_categoria)
    cargar_tabla()
    limpiar_inputs()

def cargar_datos_fila(fila, _):
    nombre_input.setText(tabla.item(fila, 1).text())

btn_agregar.clicked.connect(agregar_categoria)
btn_actualizar.clicked.connect(actualizar_categoria_ui)
btn_eliminar.clicked.connect(eliminar_categoria_ui)
tabla.cellClicked.connect(cargar_datos_fila)

ventana.setLayout(layout)
cargar_tabla()
ventana.show()
ventana.resize(800, 600)
sys.exit(app.exec())
