class Main:
    pass

print("Testando projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "444555-666777")
Conta = Conta(c1.get_nome(), 6565, 0)
Conta.deposita(100)
Conta.saque(50)
Conta.extrato()



