def saldo_final(saldo_inicial, deposito, retiro):
    saldo = saldo_inicial
    saldo += deposito
    saldo -= retiro
    return saldo