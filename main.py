from classVENTA import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15 de Octubre de 2024")
venta.set_cliente("Pedro")
#venta.set_productos(["Producto 1", "Producto 2", "Producto 3"])
#venta.set_total(150.75)

venta.mostrar_detalle()

# Agregar productos
venta.agregar_producto("manzanas", 3, 12.00)
venta.agregar_producto("peras", 4, 60.00)
venta.agregar_producto("naranjas", 5, 45.00)

# Intentar agregar un cuarto producto
venta.agregar_producto("uvas", 2, 1.2)

# Mostrar los productos en el carrito
venta.mostrar_productos()


total = venta.calcular_total()
print(f"Total de la compra: {total:.2f}")
