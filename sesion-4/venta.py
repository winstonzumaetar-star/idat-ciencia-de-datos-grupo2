import pandas as pd

df = pd.read_csv("ventas_enero.csv")

ventas_mayores_1000 = df[df["precio_unitario"] > 1000]

print(ventas_mayores_1000)