import pandas as pd

clientes = pd.read_csv("clientes.csv")
facturacion = pd.read_csv("facturacion.csv")

resultado = pd.merge(facturacion, clientes, on="id_cliente", how="left")

agrupador = resultado.groupby(["nombre", "pais"]).sum()["monto"]

# Exporta en csv
agrupador.to_csv("Agrupados.csv")

# Exporta en xslx usando pip install openpyxl
agrupador.to_excel("Agrupados.xlsx")