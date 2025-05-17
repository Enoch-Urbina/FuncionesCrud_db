import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from conexiondb import conectar

conexion = conectar()
cursor = conexion.cursor()

def obtener_unidades():
    cursor.execute("SELECT * FROM unidades")
    return cursor.fetchall()

def insertar_unidad(nombre):
    sql = "INSERT INTO unidades (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()

def actualizar_unidad(id_unidad, nombre):
    sql = "UPDATE unidades SET nombre=%s WHERE id_unidad=%s"
    cursor.execute(sql, (nombre, id_unidad))
    conexion.commit()

def eliminar_unidad(id_unidad):
    cursor.execute("DELETE FROM unidades WHERE id_unidad=%s", (id_unidad,))
    conexion.commit()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Unidades")
layout = QVBoxLayout()

# Entradas
nombre_input = QLineEdit()
layout.addWidget(QLabel("Nombre:"))
layout.addWidget(nombre_input)

# Tabla
tabla = QTableWidget()
tabla.setColumnCount(2)
tabla.setHorizontalHeaderLabels(["ID", "Nombre"])
layout.addWidget(tabla)

# Botones
boton_layout = QHBoxLayout()
btn_agregar = QPushButton("Agregar")
btn_actualizar = QPushButton("Actualizar")
btn_eliminar = QPushButton("Eliminar")
boton_layout.addWidget(btn_agregar)
boton_layout.addWidget(btn_actualizar)
boton_layout.addWidget(btn_eliminar)
layout.addLayout(boton_layout)

# Funciones
def cargar_tabla():
    tabla.setRowCount(0)
    datos = obtener_unidades()
    for fila_idx, fila in enumerate(datos):
        tabla.insertRow(fila_idx)
        for col_idx, valor in enumerate(fila):
            tabla.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))

def limpiar_inputs():
    nombre_input.clear()

def agregar_unidad():
    insertar_unidad(nombre_input.text())
    cargar_tabla()
    limpiar_inputs()

def actualizar_unidad_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una unidad para actualizar.")
        return
    id_unidad = int(tabla.item(fila, 0).text())
    actualizar_unidad(id_unidad, nombre_input.text())
    cargar_tabla()
    limpiar_inputs()

def eliminar_unidad_ui():
    fila = tabla.currentRow()
    if fila < 0:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una unidad para eliminar.")
        return
    id_unidad = int(tabla.item(fila, 0).text())
    eliminar_unidad(id_unidad)
    cargar_tabla()
    limpiar_inputs()

def cargar_datos_fila(fila, _):
    nombre_input.setText(tabla.item(fila, 1).text())

# Eventos
btn_agregar.clicked.connect(agregar_unidad)
btn_actualizar.clicked.connect(actualizar_unidad_ui)
btn_eliminar.clicked.connect(eliminar_unidad_ui)
tabla.cellClicked.connect(cargar_datos_fila)

# Mostrar
ventana.setLayout(layout)
cargar_tabla()
ventana.show()
ventana.resize(800, 600)
sys.exit(app.exec())
