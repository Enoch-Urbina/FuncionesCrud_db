-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS db23270637;

-- Usar la base de datos
USE db23270637;

-- Tabla unidades
CREATE TABLE unidades (
    id_unidad INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla categoria
CREATE TABLE categoria (
    id_categoria INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Tabla proveedor
CREATE TABLE proveedor (
    id_proveedor INT(11) AUTO_INCREMENT PRIMARY KEY,
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
    id_cliente INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(250),
    telefono VARCHAR(10),
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla empleado
CREATE TABLE empleado (
    id_empleado INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(45)
);

-- Tabla pedido
CREATE TABLE pedido (
    id_pedido INT(11) AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT(11),
    fecha_pedido DATETIME,
    estado ENUM('pendiente', 'recibido', 'cancelado'),
    CONSTRAINT Realiza FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);

-- Tabla venta
CREATE TABLE venta (
    id_venta INT(11) AUTO_INCREMENT PRIMARY KEY,
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
    id_inventario INT(11) AUTO_INCREMENT PRIMARY KEY,
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



-- Insertar unidad
INSERT INTO unidades (id_unidad, nombre) VALUES (1, 'pieza');

-- Insertar proveedor ficticio
INSERT INTO proveedor (id_proveedor, nombre, telefono, email, direccion)
VALUES (1, 'Proveedor Genérico', '5551234567', 'contacto@proveedor.com', 'Calle Falsa 123');

-- Insertar categorías
INSERT INTO categoria (id_categoria, nombre) VALUES (1, 'Barras de cereal');
INSERT INTO categoria (id_categoria, nombre) VALUES (2, 'Bebidas');
INSERT INTO categoria (id_categoria, nombre) VALUES (3, 'Bebidas calientes');
INSERT INTO categoria (id_categoria, nombre) VALUES (4, 'Galletas');
INSERT INTO categoria (id_categoria, nombre) VALUES (5, 'Harinas y cereales');

-- Insertar productos
INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('7501000628372', 'Galletas Marías Gamesa 513g', 'Galletas Marías Gamesa 513g', 12.23, 8.56, 47, 4, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('7501000663071', 'Harina para Hot Cakes Tradicional 1.2kg', 'Harina para Hot Cakes Tradicional 1.2kg', 15.81, 11.07, 11, 5, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('7501761822656', 'Atole Quaker Vainilla 45g', 'Atole Quaker Vainilla 45g', 16.13, 11.29, 34, 3, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('7501761863291', 'Barra Stila Fresa 150g', 'Barra Stila Fresa 150g', 13.64, 9.55, 48, 1, 1, 1);

-- Todos los siguientes productos son categoría "Bebidas" (id_categoria = 2)
INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530245', 'Refresco Coca-Cola botella de 1 litro', 'Refresco Coca-Cola botella de 1 litro', 18.27, 12.79, 10, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530292', 'Refresco Coca-Cola botella de 2 litros', 'Refresco Coca-Cola botella de 2 litros', 16.32, 11.42, 35, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530388', 'Refresco Fresca sabor toronja 2 litros', 'Refresco Fresca sabor toronja 2 litros', 16.53, 11.57, 20, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530437', 'Paquete Coca-Cola 2L + Fanta naranja 2L', 'Paquete Coca-Cola 2L + Fanta naranja 2L', 14.10, 9.87, 6, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530474', 'Refresco Coca-Cola botella de 3 litros', 'Refresco Coca-Cola botella de 3 litros', 19.57, 13.70, 2, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530480', 'Refresco Sprite 3 litros', 'Refresco Sprite 3 litros', 11.42, 7.99, 26, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530524', 'Refresco Coca-Cola original 2.5 litros', 'Refresco Coca-Cola original 2.5 litros', 12.56, 8.79, 34, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530536', 'Refresco Coca-Cola light 2 litros', 'Refresco Coca-Cola light 2 litros', 15.62, 10.93, 21, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530565', 'Refresco Sprite lima-limón 2 litros', 'Refresco Sprite lima-limón 2 litros', 18.03, 12.62, 28, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530574', 'Agua mineralizada Ciel 2 litros', 'Agua mineralizada Ciel 2 litros', 17.96, 12.57, 31, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530704', 'Pack 4 botellas Coca-Cola original 600ml', 'Pack 4 botellas Coca-Cola original 600ml', 12.00, 8.40, 1, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530469', 'Refresco Delaware Punch uva 600 ml', 'Refresco Delaware Punch uva 600 ml', 19.28, 13.50, 13, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530472', 'Agua Ciel botella de 1.5 litros', 'Agua Ciel botella de 1.5 litros', 18.68, 13.08, 24, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530479', 'Refresco Fanta naranja 3 litros', 'Refresco Fanta naranja 3 litros', 19.71, 13.80, 41, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530481', 'Refresco Fresca toronja 3 litros', 'Refresco Fresca toronja 3 litros', 11.86, 8.30, 49, 2, 1, 1);

INSERT INTO articulo (id_articulo, nombre, descripcion, precio, costo, stock, id_categoria, id_proveedor, id_unidad)
VALUES ('750105530533', 'Refresco Coca-Cola light 600 ml', 'Refresco Coca-Cola light 600 ml', 19.83, 13.88, 17, 2, 1, 1);
