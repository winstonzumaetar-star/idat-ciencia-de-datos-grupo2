def calcular_precio_final(precio_base):
    igv = 0.18  # IGV del 18%
    impuesto = precio_base * igv
    total = impuesto + precio_base
    return total

# Ejemplo de uso
producto_a = calcular_precio_final(100)
print(f"El precio final del producto A es: {producto_a}")