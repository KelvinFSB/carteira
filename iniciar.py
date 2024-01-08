from modelos.funcoes_compartilhadas import limpar_console
from modelos.indice_carteira import inicio
from modelos.gerenciamento_carteiras import criar_carteira , remover_carteira, ver_carteiras
from modelos.gerenciamento_carteiras import carteiras
from time import sleep

def apresentacao():
    mensagem = '***Seja bem-vindo ao gestor de carteiras!***'
    print(len(mensagem) * '*')
    print(mensagem)
    print(len(mensagem) * '*')
    input('\n\nAperte qualquer tecla para iniciar!')
    limpar_console()

def sumario():
    print('1 - Ver minhas carteiras\n'
          '2 - Distribuir valores\n'
          '3 - Criar nova carteira\n'
          '4 - Remover carteira')

def escolha_sumario():

    while True:
        try:
            escolha_sumario = int(input('\nQual ação deseja realizar?\n'))
            if 0 < escolha_sumario <= 4:
                if escolha_sumario == 1:
                    limpar_console()
                    inicio()
                    break
                elif escolha_sumario == 2:
                    distribuir_valores()
                    break
                elif escolha_sumario == 3:
                    limpar_console()
                    criar_carteira()
                    retorno()
                    break
                elif escolha_sumario == 4:
                    limpar_console()
                    ver_carteiras()
                    remover_carteira()
                    retorno()
                    break
            else:
                limpar_console()
                print('Você digitou uma opção errada, tente novamente!')
                sleep(2)
                limpar_console()
                sumario()
        except ValueError:
            limpar_console()
            print('Você digitou uma opção errada, tente novamente!')
            sleep(2)
            limpar_console()
            sumario()



def distribuir_valores():
    while True:
        limpar_console()
        valor = float(input('Qual valor você deseja distribuir? '))
        descricao = input('Digite a descrição do depósito: ')
        valor_c_c = valor * 0.7
        valor_10 = valor * 0.1

        for carteiraa in carteiras:
            if carteiraa.get_nome() == 'C/C':
                carteiraa.depositar(valor_c_c, descricao)
            elif carteiraa.get_nome() == 'Poupança':
                carteiraa.depositar(valor_10, descricao)
            elif carteiraa.get_nome() == 'Liberdade Financeira':
                carteiraa.depositar(valor_10, descricao)
            elif carteiraa.get_nome() == 'Diversão':
                carteiraa.depositar(valor_10, descricao)

        sumario()
        escolha_sumario()
        break

def retorno():
    sumario()
    escolha_sumario()

if __name__ == '__main__':
    apresentacao()
    retorno()

