import matplotlib.pyplot as plt

cantidad = [10, 20, 25, 30]
horas = [1, 2, 3, 4]

plt.plot(horas, cantidad)
plt.title("Ventas de café por hora")
plt.xlabel("Horas")
plt.ylabel("Cantidad de café vendido")
plt.show()
