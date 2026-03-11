import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('compras.csv')

df["fecha"] = pd.to_datetime(df["fecha"]) # Convertir la columna "fecha" a formato datetime

df["sub_total"] = df["precio_unitario"] * df["cantidad"]

df = df[(df["total"] > 1000)]

ordenamiento_metodo_pago = df.sort_values(["metodo_pago", "ciudad"], ascending=[False, True])

ordenamiento_metodo_pago["igv"] = ordenamiento_metodo_pago["precio_unitario"] * 0.18
# print(ordenamiento_metodo_pago)

# filtrado solo del mes de enero
fecha_inicio = pd.to_datetime("2026-01-01")
fecha_fin = pd.to_datetime("2026-01-31")

# filtro_enero = ordenamiento_metodo_pago[(ordenamiento_metodo_pago["fecha"] >= fecha_inicio) & (ordenamiento_metodo_pago["fecha"] <= fecha_fin)]
filtro_enero = ordenamiento_metodo_pago[ordenamiento_metodo_pago["fecha"].between(fecha_inicio, fecha_fin)]

filtro_enero_dia_tres = filtro_enero[filtro_enero["fecha"].dt.day == 3]

print(filtro_enero_dia_tres)