from funciones_financieras import saldo_final

saldo = 2000000
deposito = 500000
retiro = 300000
saldo = saldo_final(saldo, deposito, retiro)
print(f"saldo final : {saldo}")