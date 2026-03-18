import matplotlib.pyplot as plt
import pandas as pd

# Ejemplo 1 Leyendo un archivo externo
# df = pd.read_csv("gastos.csv")
# plt.pie(df["monto"], labels=df["categoria"], autopct="%1.3f%%", textprops={'color': 'white', 'fontsize': 12})


# Ejemplo 2 puedas consumir desde un dicicionario
# data = {
#     "categoria": ["comida", "transporte", "entretenimiento", "salud"],
#     "monto": [500, 200, 300, 100],
# }
# plt.pie(data["monto"], labels=data["categoria"], autopct="%1.3f%%", textprops={'color': 'white', 'fontsize': 12})

# Ejemplo 3 usando variables de listas
# categoria = ["comida", "transporte", "entretenimiento", "salud"]
# monto = [500, 200, 300, 100]
# plt.pie(monto, labels=categoria, autopct="%1.3f%%", textprops={'color': 'white', 'fontsize': 12})

# Ejemplo 4 Leyendo un archivo externo xlsx
df = pd.read_excel("gastos_excel.xls")
plt.pie(df["monto"], labels=df["categoria"], autopct="%1.3f%%", textprops={'color': 'white', 'fontsize': 12})

plt.title("Categoria de gastos")

plt.show()

# plt.savefig("gastos.jpg")