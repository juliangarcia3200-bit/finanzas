from funciones_financieras import interes_compuesto

capital = float(input("Ingrese el capital inicial:")) # Capital inicial
tasa = float(input("Ingrese la tasa:"))  # Tasa de interés anual (5%)   
tiempo = float(input("Ingrese el tiempo:"))  # Tiempo en años

resultado = interes_compuesto(capital, tasa, tiempo)
print(f"El monto total después de {tiempo} años es: {resultado:.2f}")