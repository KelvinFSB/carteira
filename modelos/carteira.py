from modelos.funcoes_compartilhadas import limpar_console
from modelos.transacao import Transacao
from time import sleep


class Carteira:
    carteiras = []

    def __init__(self, nome_da_carteira):
        self._nome_da_carteira = nome_da_carteira.title()
        self._saldo = 0.0
        self.transacoes = []

    def get_nome(self):
        return self._nome_da_carteira

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def extrato(self):
        limpar_console()
        print(f'{self._nome_da_carteira} - Saldo: R$ {self.get_saldo():.2f}\n')
        print('Transações:\n')
        for transacao in self.transacoes:
            print(f'{transacao.data}: {transacao.descricao}, Valor: R$ {transacao.valor:.2f}')
        input('\n\nAperte qualquer tecla para retornar ao menu inciar')
        limpar_console()

    def depositar(self, valor, descricao):
        limpar_console()
        if valor > 0:
            novo_saldo = self.get_saldo() + valor
            self.set_saldo(novo_saldo)
            self.transacoes.append(Transacao(valor, descricao))
            print(f"Depósito de {valor} realizado com sucesso na carteira {self.get_nome()}")
            sleep(2)
            limpar_console()
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor, descricao):
        limpar_console()
        if valor > 0 and valor <= self.get_saldo():
            novo_saldo = self.get_saldo() - valor
            self.set_saldo(novo_saldo)
            self.transacoes.append(Transacao(valor, descricao))
            print(f"Saque de {valor} realizado com sucesso na carteira {self.get_nome()}")
            sleep(2)
            limpar_console()
        else:
            print("O valor do saque deve ser maior que zero e menor ou igual ao saldo disponível.")

    def transferir(self, carteira_destino, valor, descricao):
            self.sacar(valor, descricao)
            carteira_destino.depositar(valor, descricao)
            print(f"Transferência de {valor} para {carteira_destino.get_nome()} realizada com sucesso.")
    carteiras = []
