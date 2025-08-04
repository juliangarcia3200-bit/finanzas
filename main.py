from funciones_financieras import interes_simple

capital = 10000000
tasa = 0.095
n = 3

interes = interes_simple(capital, tasa, n)
print(f"El intereses sobre el capital {capital:,.2f}, asciende a ${interes:,.2f} durante los {n} meses")