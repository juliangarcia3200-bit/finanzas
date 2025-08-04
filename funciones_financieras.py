def interes_simple(monto, porcentaje, n):
    return monto * porcentaje * n
     
def interes_compuesto(capital, tasa, tiempo):
    """
    Calcula el interés compuesto.

    :param capital: Capital inicial (float)
    :param tasa: Tasa de interés anual (float)
    :param tiempo: Tiempo en años (float)
    :return: Monto total después del interés compuesto (float)
    """
    return capital * (1 + tasa) ** tiempo