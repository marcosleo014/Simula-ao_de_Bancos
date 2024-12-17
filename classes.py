class Cliente:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self,clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.depósito(saldo)
    def resumo(self):
        print(f"CC n°: {self.número} Saldo: {self.saldo:10.2f}")
    def saque(self,valor):
        if self.saldo>=valor:
            self.saldo -= valor
            print(f"Saque realizado: -{valor}")
            self.operações.append(['SAQUE',valor])
        else:
            print("Saldo insuficiente para realização do saque")
    def depósito(self,valor):
        self.saldo += valor
        print(f"Depósito realizado: +{valor}")
        self.operações.append(['DEPÓSITO',valor])
    def extrato(self):
        print(f"Extrato CC n° {self.número}:\n")
        for operação in self.operações:
            print(f"{operação[0]} {operação[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}")

class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.contas = []
    def abrir_conta(self,conta):
        self.contas.append(conta)
    def fechar_conta(self,conta):
        self.contas.append(conta)
    def exibir_contas(self):
        for conta in self.contas:
            conta.resumo()
