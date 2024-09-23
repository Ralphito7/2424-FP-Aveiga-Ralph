def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento y el monto final a pagar.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10%).
    :return: Monto del descuento y monto final a pagar.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final


# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función
    monto1 = 1000  # Monto total de la compra
    descuento1, monto_final1 = calcular_descuento(monto1)
    print(f"Monto total: ${monto1}")
    print(f"Descuento aplicado: ${descuento1:.2f} (10%)")
    print(f"Monto final a pagar: ${monto_final1:.2f}")

    # Segunda llamada a la función con un porcentaje de descuento diferente
    monto2 = 500  # Monto total de la compra
    porcentaje_descuento2 = 20  # Porcentaje de descuento
    descuento2, monto_final2 = calcular_descuento(monto2, porcentaje_descuento2)
    print(f"\nMonto total: ${monto2}")
    print(f"Descuento aplicado: ${descuento2:.2f} ({porcentaje_descuento2}%)")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
