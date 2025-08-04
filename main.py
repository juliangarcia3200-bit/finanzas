from funciones_financieras import ahorro

monto_ahorro = 3000000
tasa_ahorro = 0.08
tiempo_ahorro = 10

ahorro = ahorro(monto_ahorro,tasa_ahorro,tiempo_ahorro)
print(f"""El ahorro que realizaste al comienzo por {monto_ahorro:,.2f},
      con una tasa de {tasa_ahorro*100} % y a un tiempo de {tiempo_ahorro} años.
      Al final del tiempo tendrás un total de {ahorro:,.2f}""")