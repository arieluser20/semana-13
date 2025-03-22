def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 1000  # Monto total de la compra
monto2 = 2000  # Otro monto total de la compra

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, 15)  # Aplicando un 15% de descuento

print(f"Descuento aplicado a {monto1}: ${descuento1}")
print(f"Descuento aplicado a {monto2} con 15%: ${descuento2}")
