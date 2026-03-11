import pandas as pd

df = pd.read_csv("compras.csv")

df["venta_total"] = df["cantidad"] * df["precio_unitario"]
print(df)

mayor_a_mil = df["venta Total"]>1000
# mayor_a_mil = df[(df["venta_total"] > 1000)]
print(mayor_a_mil)