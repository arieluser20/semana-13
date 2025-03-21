def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento basado en un porcentaje dado.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto 10%)
    :return: float - Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 200
monto2 = 500

# Primera llamada con el porcentaje por defecto (10%)
descuento1 = calcular_descuento(monto1)
print(f"El descuento para una compra de ${monto1} es: ${descuento1}")

# Segunda llamada con un porcentaje específico (15%)
descuento2 = calcular_descuento(monto2, 15)
print(f"El descuento para una compra de ${monto2} con 15% es: ${descuento2}")
