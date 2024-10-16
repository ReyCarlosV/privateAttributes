class Venta:

    __id_venta = None

    __fecha = None

    __cliente = None

    __productos = {}  # Lista de productos vendidos

    #__total = none

    # Getters para acceder a los atributos privados

    def get_id_venta(self):

        return self.__id_venta


    def get_fecha(self):

        return self.__fecha


    def get_cliente(self):

        return self.__cliente


    def get_productos(self):

        return self.__productos


    #def get_total(self):

        #return


    # Setters para modificar los atributos privados

    def set_id_venta(self, id_venta):

        self.__id_venta = id_venta


    def set_fecha(self, fecha):

        self.__fecha = fecha


    def set_cliente(self, cliente):

        self.__cliente = cliente


    def set_productos(self, productos):

        self.__productos = productos


    #def set_total(self, total):

       #self.__total = total


    # Método para mostrar los detalles de la venta

    def mostrar_detalle(self):

        print(f"ID Venta: {self.__id_venta}")

        print(f"Fecha: {self.__fecha}")

        print(f"Cliente: {self.__cliente}")

        print(f"Productos: {', '.join(self.__productos)}")

       #print(f"Total: ${self.__total:.2f}")


    def agregar_producto(self, producto, cantidad, precio_unitario):
        if len(self.__productos) < 3:
            if producto not in self.__productos:
                self.__productos[producto] = {
                    'cantidad': cantidad,
                    'precio_unitario': precio_unitario
                }
                print(f"Producto '{producto}' agregado al carrito.")
            else:
                print(f"El producto '{producto}' ya está en el carrito.")
        else:
            print("El carrito ya tiene 3 productos. No puedes agregar más.")

    def mostrar_productos(self):
        if self.__productos:
            for producto, detalles in self.__productos.items():
                print(f"Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio Unitario: {detalles['precio_unitario']}")
        else:
            print("El carrito está vacío.")

    def calcular_total(self):
        total = 0
        for producto, detalles in self.__productos.items():
            subtotal = detalles['cantidad'] * detalles['precio_unitario']
            total += subtotal
        return total
