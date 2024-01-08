from modelos.carteira import Carteira
from modelos.funcoes_compartilhadas import limpar_console
from time import sleep



carteiras = []
carteiras.append(Carteira('C/c'))
carteiras.append(Carteira('Poupança'))
carteiras.append(Carteira('Liberdade Financeira'))
carteiras.append(Carteira('Diversão'))

def ver_carteiras():
    for carteira in carteiras:
        print(f'Carteira: {carteira.get_nome().ljust(20)} | Saldo: R$ {carteira.get_saldo():.2f}')

def criar_carteira():
    nome_da_nova_carteira = str(input('Qual nome deseja dar para a nova carteira?').title())
    carteiras.append(Carteira(nome_da_nova_carteira))
    limpar_console()
    print(f'Carteira {nome_da_nova_carteira} criada com sucesso!')
    sleep(2)
    limpar_console()

def remover_carteira():
    carteira_para_remover = achar_carteira()
    carteiras.remove(carteira_para_remover)
    limpar_console()
    print(f'Carteira {carteira_para_remover._nome_da_carteira} removida com sucesso!')
    sleep(2)
    limpar_console()

def achar_carteira():
    while True:
        nome_carteira = str(input('Digite o nome da carteira: ').title())
        limpar_console()
        for carteira_solicitada in carteiras:
            if carteira_solicitada.get_nome() == nome_carteira:
                return carteira_solicitada
        print('Carteira não encontrada!')
        sleep(2)
        limpar_console()
        ver_carteiras()