
from funciones_financieras import saldo_final

saldo = 2000000
deposito = 500000
retiro = 300000
saldo = saldo_final(saldo, deposito, retiro)
print(f"saldo final : {saldo}")

from funciones_financieras import ahorro

monto_ahorro = 3000000
tasa_ahorro = 0.08
tiempo_ahorro = 10

ahorro = ahorro(monto_ahorro,tasa_ahorro,tiempo_ahorro)
print(f"""El ahorro que realizaste al comienzo por {monto_ahorro:,.2f},
      con una tasa de {tasa_ahorro*100} % y a un tiempo de {tiempo_ahorro} años.
      Al final del tiempo tendrás un total de {ahorro:,.2f}""")

from funciones_financieras import interes_simple, interes_compuesto

monto = 10000000
porcentaje = 0.05
n = 3

interes = interes_simple(monto, porcentaje, n)
print(f"El intereses sobre el capital {monto:,.2f}, asciende a ${interes:,.2f} durante los {n} meses")

capital = float(input("Ingrese el capital inicial:")) # Capital inicial
tasa = float(input("Ingrese la tasa:"))  # Tasa de interés anual (5%)   
tiempo = float(input("Ingrese el tiempo:"))  # Tiempo en años

resultado = interes_compuesto(capital, tasa, tiempo)
print(f"El monto total después de {tiempo} años es: {resultado:.2f}")

