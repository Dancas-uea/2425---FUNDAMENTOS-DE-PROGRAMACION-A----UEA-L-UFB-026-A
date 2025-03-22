
# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado al monto total de la compra.

    Args:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float, optional): Porcentaje de descuento a aplicar. Por defecto es 10.

    Returns:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función desde el programa principal
# Primera llamada: solo se proporciona el monto total (descuento predeterminado 10%)
monto_compra1 = 1500
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

# Segunda llamada: se proporciona monto total y porcentaje de descuento (15%)
monto_compra2 = 3000
porcentaje2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje2)
monto_final2 = monto_compra2 - descuento2

# Mostrar resultados (incluyendo montos originales)
print(
    f"Compra 1 - Monto original: ${monto_compra1:.2f}, Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(
    f"Compra 2 - Monto original: ${monto_compra2:.2f}, Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")