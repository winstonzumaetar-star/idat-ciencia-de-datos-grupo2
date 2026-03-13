import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril"]
luz = [40, 50, 45, 60]
agua = [25, 30, 28, 35]

plt.plot(mes, luz, label="Luz")
plt.plot(mes, agua, label="Agua")

plt.title("Gastos de la casa")
plt.legend()
plt.show()