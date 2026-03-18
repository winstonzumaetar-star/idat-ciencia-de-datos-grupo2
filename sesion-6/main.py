import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]

maximas = [25, 28, 26, 30, 31]
minimas = [15, 14, 16, 18, 17]

plt.plot(dias, maximas, label="Maximas", color="red")
plt.plot(dias, minimas, label="Minimas", color="blue")

plt.title("Pronostico del clima")

plt.show()