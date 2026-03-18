import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salario.csv')

fig, ax = plt.subplots()

barras = ax.bar(df["nombre"], df["sueldo"], color="green")
ax.bar_label(barras)

plt.show()