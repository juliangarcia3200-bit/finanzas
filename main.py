from funciones_financieras import interes_simple, interes_compuesto

monto = 10000000
porcentaje = 0.05
n = 3

interes = interes_simple(monto, porcentaje, n)
print(f"El intereses sobre el capital {monto:,.2f}, asciende a ${interes:,.2f} durante los {n} meses")

capital = 1000.0  # Capital inicial
tasa = 0.05  # Tasa de interés anual (5%)   
tiempo = 5  # Tiempo en años

resultado = interes_compuesto(capital, tasa, tiempo)
print(f"El monto total después de {tiempo} años es: {resultado:.2f}")
