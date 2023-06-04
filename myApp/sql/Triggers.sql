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

UPDATE producto
SET valor_venta = 1700
WHERE id_producto = 10;

SELECT * FROM producto WHERE id_producto = 10;

