from funciones_financieras import interes_compuesto

capital = 1000.0  # Capital inicial
tasa = 0.05  # Tasa de interés anual (5%)   
tiempo = 5  # Tiempo en años

resultado = interes_compuesto(capital, tasa, tiempo)
print(f"El monto total después de {tiempo} años es: {resultado:.2f}")