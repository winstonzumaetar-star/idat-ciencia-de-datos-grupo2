import pandas as pd

df = pd.read_csv('compras.csv')

producto = df["producto"]

# print(producto)

sub_tabla = df[["producto", "precio_unitario"]]

# print(sub_tabla)

filtrado_metodo_de_pago = df[df["metodo_pago"] == "Yape"]
print(filtrado_metodo_de_pago)

filtrado_metodo_de_pago_y_total = df[(df["metodo_pago"] == "Yape") & (df["total"] > 100) & (df["ciudad"] == "Lima")]
print(filtrado_metodo_de_pago_y_total)