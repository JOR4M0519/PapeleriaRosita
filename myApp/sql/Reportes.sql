-- ----------------------------------- REPORTES DE COMPRAS ---------------------------------------------
CREATE OR REPLACE FUNCTION FN_ReporteCompra(fecha_inicial DATE, fecha_final DATE, out resultado json)
AS $$
BEGIN
    resultado=array_to_json(array_agg(row_to_json(t)))
    FROM (
        SELECT id_detcompra,cantidad,fecha,
               (SELECT nombre_producto FROM producto WHERE producto.id_producto = detalles_compra.id_producto),
               (SELECT razon_social FROM proveedor WHERE proveedor.id_proveedor = detalles_compra.id_proveedor)
        FROM detalles_compra
        WHERE detalles_compra.fecha BETWEEN fecha_inicial AND fecha_final
		ORDER BY fecha DESC, id_detcompra
    ) t;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION FN_ReporteCompraProveedor(idProveedor int, fecha_inicial DATE, fecha_final DATE, out resultado json)
AS $$
BEGIN
    resultado=array_to_json(array_agg(row_to_json(t)))
    FROM (
        SELECT id_detcompra,cantidad,fecha,
               (SELECT nombre_producto FROM producto WHERE producto.id_producto = detalles_compra.id_producto),
               (SELECT razon_social FROM proveedor WHERE proveedor.id_proveedor = detalles_compra.id_proveedor)
        FROM detalles_compra
        WHERE detalles_compra.id_proveedor = idProveedor AND detalles_compra.fecha BETWEEN fecha_inicial AND fecha_final
		ORDER BY fecha DESC, id_detcompra
    ) t;
END;
$$ LANGUAGE plpgsql;

-- ----------------------------------- REPORTE DE VENTAS -----------------------------------------------

CREATE OR REPLACE FUNCTION FN_ReporteVenta(fecha_inicial DATE, fecha_final DATE, out resultado json)
AS $$
BEGIN
    resultado=array_to_json(array_agg(row_to_json(t)))
    FROM (
        SELECT id_detventa,cantidad,fecha,
               (SELECT nombre_producto FROM producto WHERE producto.id_producto = detalles_venta.id_producto)
        FROM detalles_venta
        WHERE detalles_venta.fecha BETWEEN fecha_inicial AND fecha_final
		ORDER BY fecha DESC, id_detventa
    ) t;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION FN_ReporteVentaProducto(idProducto int, fecha_inicial DATE, fecha_final DATE, out resultado json)
AS $$
BEGIN
    resultado=array_to_json(array_agg(row_to_json(t)))
    FROM (
        SELECT id_detventa,cantidad,fecha,
               (SELECT nombre_producto FROM producto WHERE producto.id_producto = detalles_venta.id_producto)
        FROM detalles_venta
        WHERE detalles_venta.id_producto = idProducto AND detalles_venta.fecha BETWEEN fecha_inicial AND fecha_final
		ORDER BY fecha DESC, id_detventa
    ) t;
END;
$$ LANGUAGE plpgsql;
-- ----------------------------------------- TEST SQL -------------------------------------------
SELECT public.fn_reporteventaproducto(5,'2023-01-30','2023-06-30');