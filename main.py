from funciones_financieras import interes_simple

monto = float(input("Ingrese el monto Inicial "))
porcentaje = float(input("Ingrese la tasa de interes "))
n = int(input("Ingrese el numero de meses "))

interes = interes_simple(monto, porcentaje, n)
print(f"El intereses sobre el capital {monto:,.2f}, asciende a ${interes:,.2f} durante los {n} meses")