class Cliente:
    def __init__(self, nombre_cliente, saldo):
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo

    def comprar(self, nombre_producto, monto):
        if self.saldo >= monto:
            self.saldo -= monto # self.saldo = self.saldo - monto
            print(f"Operación exitosa!")

            mensage = f"Compra realizada por {self.nombre_cliente} del producto {nombre_producto}. Saldo restante: {self.saldo}"
            return mensage
        else:
            print("Operación fallida!")
            return f"Saldo insuficiente para realizar la compra de {nombre_producto}."


cliente = Cliente("Luis", 1000)  # Instancia de clase con valores iniciales

resultado = cliente.comprar(nombre_producto="Celular", monto=200)  # Llamada al metodo comprar con el producto y monto a comprar
print(f"Resultado: {resultado}")

resultado = cliente.comprar(monto=300, nombre_producto="Zapatillas")
print(f"Resultado: {resultado}")

resultado = cliente.comprar("Boletos de avión", 500)
print(f"Resultado: {resultado}")

resultado = cliente.comprar("Hamburguesa", 10)
print(f"Resultado: {resultado}")
