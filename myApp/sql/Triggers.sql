-- -------------------------- TRIGGER VENTAS --------------------------
CREATE OR REPLACE FUNCTION FN_VentaStock()
RETURNS TRIGGER
AS $$
BEGIN
    UPDATE producto
    SET stock=stock-new.cantidad
    WHERE id_producto = new.id_producto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER TR_VentaStock
AFTER INSERT
ON detalles_venta
    FOR EACH ROW
    EXECUTE FUNCTION FN_VentaStock();
-- -------------------------- TRIGGER COMPRAS --------------------------
CREATE OR REPLACE FUNCTION FN_CompraStock()
RETURNS TRIGGER
AS $$
BEGIN
    UPDATE producto
    SET stock=stock+new.cantidad
    WHERE id_producto = new.id_producto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER TR_CompraStock
AFTER INSERT
ON detalles_compra
    FOR EACH ROW
    EXECUTE FUNCTION FN_CompraStock();
-- -------------------------- TRIGGER GANANCIAS --------------------------
CREATE OR REPLACE FUNCTION FN_Ganancia()
RETURNS TRIGGER
AS $$
BEGIN
    UPDATE producto
    SET valor_ganancia=new.valor_venta-new.valor_compra
    WHERE id_producto = new.id_producto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER TR_Ganancia
AFTER INSERT OR UPDATE
ON producto
    FOR EACH ROW
    WHEN(pg_trigger_depth()<1)
    EXECUTE FUNCTION FN_Ganancia();
-- ----------------------- TRIGGER CAMBIOS --------------------------------
CREATE OR REPLACE FUNCTION FN_Cambios()
RETURNS TRIGGER
AS $$
BEGIN
    IF new.id_producto <> old.id_producto THEN
        UPDATE producto
        SET stock=producto.stock+old.cantidad
        WHERE id_producto = old.id_producto;

        UPDATE producto
        SET stock = producto.stock-new.cantidad
        WHERE id_producto = new.id_producto;

    ELSIF new.id_producto = old.id_producto AND old.cantidad > new.cantidad THEN

        UPDATE producto
        SET stock = producto.stock+(old.cantidad-new.cantidad)
        WHERE id_producto = new.cantidad;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER TR_Cambios
AFTER UPDATE
ON detalles_venta
    FOR EACH ROW
    WHEN(pg_trigger_depth()<1)
    EXECUTE FUNCTION FN_Cambios();


UPDATE detalles_venta
SET id_producto = 2,cantidad = 1
WHERE id_detventa = 6;

INSERT INTO producto (nombre_producto, valor_compra, valor_venta, valor_ganancia, stock, estado)
VALUES ('Calculadora',5000,8000,0,10,'A');



SELECT  id_detventa,id_producto,cantidad,
       (select nombre_producto from producto where detalles_venta.id_producto = producto.id_producto),
       (select stock from producto where detalles_venta.id_producto = producto.id_producto)
FROM detalles_venta;

SELECT * FROM producto;

SELECT nombre_producto,stock from producto where stock < 10;
