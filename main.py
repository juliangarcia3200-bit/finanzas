from funciones_financieras import interes_simple

monto = 10000000
porcentaje = 0.095
n = 3

interes = interes_simple(monto, porcentaje, n)
print(f"El intereses sobre el capital {monto:,.2f}, asciende a ${interes:,.2f} durante los {n} meses")