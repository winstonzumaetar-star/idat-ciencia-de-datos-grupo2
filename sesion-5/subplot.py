import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril"]
luz = [40, 50, 45, 60]
agua = [25, 30, 28, 35]

plt.subplot(2, 1, 1)
plt.plot(mes, luz)
plt.title("Gastos de Luz")

plt.subplot(2, 1, 2)
plt.plot(mes, agua)
plt.title("Gastos de Agua")


plt.tight_layout()
plt.show()