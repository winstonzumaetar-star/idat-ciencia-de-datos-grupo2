class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

        if cantidad < 0:
            print(
                f"He descontado al producto {self.nombre} una cantidad de {-cantidad} y el stock es negativo, por favor revise el stock del producto")
        else:
            print(f"He actualizado el stock del producto {self.nombre} a {self.stock}")


producto = Producto("Laptop", 1500, 10)

producto.actualizar_stock(5)
producto.actualizar_stock(-8)
