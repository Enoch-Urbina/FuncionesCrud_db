-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS bodegaaurrera;

-- Usar la base de datos
USE bodegaaurrera;

-- Creación de tablas

-- Tabla unidades
CREATE TABLE unidades (
    id_unidad INT(11) PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla categoria
CREATE TABLE categoria (
    id_categoria INT(11) PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Tabla proveedor
CREATE TABLE proveedor (
    id_proveedor INT(11) PRIMARY KEY,
    nombre VARCHAR(250),
    telefono VARCHAR(15),
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla articulo
CREATE TABLE articulo (
    id_articulo CHAR(13) PRIMARY KEY,
    nombre VARCHAR(250),
    descripcion TEXT,
    precio DECIMAL(10,2),
    costo DECIMAL(10,2),
    stock INT(11),
    id_categoria INT(11),
    id_proveedor INT(11),
    id_unidad INT(11),
    CONSTRAINT Pertenece FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
    CONSTRAINT Provee FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor),
    CONSTRAINT Usa FOREIGN KEY (id_unidad) REFERENCES unidades(id_unidad)
);

-- Tabla cliente
CREATE TABLE cliente (
    id_cliente INT(11) PRIMARY KEY,
    nombre VARCHAR(250),
    telefono VARCHAR(10),
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla empleado
CREATE TABLE empleado (
    id_empleado INT(11) PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(45)
);

-- Tabla pedido
CREATE TABLE pedido (
    id_pedido INT(11) PRIMARY KEY,
    id_proveedor INT(11),
    fecha_pedido DATETIME,
    estado ENUM('pendiente', 'recibido', 'cancelado'),
    CONSTRAINT Realiza FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);

-- Tabla venta
CREATE TABLE venta (
    id_venta INT(11) PRIMARY KEY,
    fecha DATETIME,
    id_cliente INT(11),
    id_empleado INT(11),
    total DECIMAL(10,2),
    CONSTRAINT Tiene FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    CONSTRAINT Atiende FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

-- Tabla detallesventa
CREATE TABLE detallesventa (
    id_venta INT(11),
    id_articulo CHAR(13),
    cantidad INT(11),
    precio_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    PRIMARY KEY (id_venta, id_articulo),
    CONSTRAINT Genera FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
    CONSTRAINT Aparece FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo)
);

-- Tabla detallespedidos
CREATE TABLE detallespedidos (
    id_pedido INT(11),
    id_articulo CHAR(13),
    cantidad INT(11),
    precio_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    PRIMARY KEY (id_pedido, id_articulo),
    CONSTRAINT Incluye FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
    CONSTRAINT Aparece2 FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo)
);

-- Tabla inventario (corregida)
CREATE TABLE inventario (
    id_inventario INT(11) PRIMARY KEY,
    id_articulo CHAR(13),
    cantidad INT(11),
    fecha_actualizacion TIMESTAMP,
    CONSTRAINT Registra FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo)
);

-- Creación de índices
CREATE INDEX idx_articulo_categoria ON articulo(id_categoria);
CREATE INDEX idx_articulo_proveedor ON articulo(id_proveedor);
CREATE INDEX idx_articulo_unidad ON articulo(id_unidad);
CREATE INDEX idx_venta_cliente ON venta(id_cliente);
CREATE INDEX idx_venta_empleado ON venta(id_empleado);
CREATE INDEX idx_detallesventa_venta ON detallesventa(id_venta);
CREATE INDEX idx_detallesventa_articulo ON detallesventa(id_articulo);
CREATE INDEX idx_detallespedidos_pedido ON detallespedidos(id_pedido);
CREATE INDEX idx_detallespedidos_articulo ON detallespedidos(id_articulo);
CREATE INDEX idx_pedido_proveedor ON pedido(id_proveedor);
CREATE INDEX idx_inventario_articulo ON inventario(id_articulo);