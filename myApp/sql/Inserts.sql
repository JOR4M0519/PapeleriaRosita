-- ------------------------------------- INSERTS DE PRODUCTO ----------------------------------------
INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Alpin',1000,2000,1000,6,'A');
INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Chocorramo',2000,3000,1000,7,'A');
INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Resma de Papel',20000,30000,10000,7,'A');
INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Lapiz',500,1000,500,10,'A');
INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Cuaderno 7 Materias',10000,30000,20000,15,'A');
-- ------------------------------------- INSERTS DE PROVEEDOR ----------------------------------------
INSERT INTO proveedor (razon_social, email_proveedor, telefono, estado)
VALUES ('AloCorp','asdasd@gmail.com','3203541217','A');
INSERT INTO proveedor (razon_social, email_proveedor, telefono, estado)
VALUES ('Alpina','aalpina@gmail.com','3203421774','A');
INSERT INTO proveedor (razon_social, email_proveedor, telefono, estado)
VALUES ('Prisma','aprisma@gmail.com','3117791133','A');
INSERT INTO proveedor (razon_social, email_proveedor, telefono, estado)
VALUES ('Primavera','aaPrimavera@gmail.com','3024467853','A');
INSERT INTO proveedor (razon_social, email_proveedor, telefono, estado)
VALUES ('Scribe','ascribe@gmail.com','3140501747','A');
-- ---------------------------------- INSERTS DE DETALLES COMPRA -------------------------------------
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (5,'2023-05-23',1,1);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (3,'2023-05-24',1,1);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (1,'2023-03-23',1,1);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (2,'2023-04-30',1,1);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (3,'2023-01-30',2,2);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (6,'2023-02-25',2,2);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (2,'2023-04-30',5,3);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (3,'2023-01-30',3,4);
INSERT INTO detalles_compra (cantidad, fecha, id_producto, id_proveedor) VALUES (6,'2023-02-25',4,5);
-- ----------------------------------- INSERTS DE DETALLES VENTA -------------------------------------
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (6,'2023-05-23',1);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (1,'2023-05-05',2);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (2,'2023-04-13',1);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (4,'2023-03-06',3);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (4,'2023-04-06',4);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (4,'2023-05-06',5);
INSERT INTO detalles_venta (cantidad, fecha, id_producto) VALUES (4,'2023-06-06',3);