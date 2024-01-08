from modelos.gerenciamento_carteiras import ver_carteiras, achar_carteira
from modelos.funcoes_compartilhadas import limpar_console
from time import sleep
from modelos.juros_compostos import calcular_juros_compostos


def indice_carteira():
    from iniciar import retorno
    while True:
        ver_carteiras()
        try:
            escolha = int(input('\nO que deseja fazer?\n'
                            '1 - Acessar carteira\n'
                            '2 - Voltar ao menu inicial\n'))
            if escolha >= 1 and escolha <= 2:

                if escolha == 1:
                    limpar_console()
                    escolha_indice_carteira()
                elif escolha == 2:
                    limpar_console()
                    retorno()
            else:
                limpar_console()
                print('Você digitou uma opção errada, tente novamente!')
                sleep(2)
                limpar_console()
        #apresenta essa mensagem caso o jogador digite algo que não seja uma opção    
        except ValueError:
            limpar_console()
            print('Você digitou uma opção errada, tente novamente!')
            sleep(2)
            limpar_console()

def escolha_indice_carteira():
    ver_carteiras()
    carteira_solicitada = achar_carteira()
    while True:
        try:
            escolha = int(input('\nO que deseja fazer?\n'
                            '1 - Depositar\n'
                            '2 - Sacar\n'
                            '3 - Transferir\n'
                            '4 - Emprestimo entre carteiras\n'
                            '5 - Extrato de transações\n'
                            '6 - Voltar ao menu de carteiras\n'))
            if escolha >= 1 and escolha <= 6:

                if escolha == 1:
                    limpar_console()
                    deposito = float(input('Digite o valor do depósito: '))
                    descricao_depo = input('Digite a descrição do depósito: ')
                    carteira_solicitada.depositar(deposito, descricao_depo)
                    break
                elif escolha == 2:
                    limpar_console()
                    saque = float(input('Digite o valor do saque: '))
                    descricao_saque = input('Digite a descrição do saque: ')
                    carteira_solicitada.sacar(saque, descricao_saque)
                    break
                elif escolha == 3:
                    limpar_console()
                    ver_carteiras()
                    carteira_destino = achar_carteira()
                    ver_carteiras()
                    while True:
                        valor_transferencia = float(input('Digite o valor da transferência: '))
                        if  valor_transferencia < carteira_solicitada.get_saldo():
                            descricao_transferencia = input('Digite a descrição da transferência: ')
                            carteira_solicitada.transferir(carteira_destino, valor_transferencia, descricao_transferencia)
                            break
                        else:
                            limpar_console()
                            print('saldo insuficiente')
                            opção = int(input('deseja continuar?\n\
1 - Sim\n\
2 - Não\n'))
                            if opção == 1:
                                
                                limpar_console()
                                ver_carteiras()
                                continue
                            else:
                                limpar_console()
                                indice_carteira()
                elif escolha == 5:
                    carteira_solicitada.extrato()
                    break
                elif escolha == 6:
                    limpar_console()
                    break
                elif escolha == 4:
                    limpar_console()
                    ver_carteiras()
                    carteira_destino = achar_carteira()
                    ver_carteiras()
                    while True:
                        valor_transferencia = float(input('Digite o valor da transferência: '))
                        if  valor_transferencia < carteira_solicitada.get_saldo():
                            descricao_transferencia = 'emprestimo'
                            quantidade_de_parcelas = int(input('Digite em quantas vezes deseja pagar o imprestimo: '))
                            carteira_solicitada.transferir(carteira_destino, valor_transferencia, descricao_transferencia)
                            valor_de_parcela = calcular_juros_compostos(valor_transferencia,quantidade_de_parcelas)
                            carteira_solicitada.sacar(valor_de_parcela, descricao_transferencia)
                            carteira_destino.depositar(valor_de_parcela, descricao_transferencia)
                            break
                        else:
                            limpar_console()
                            print('saldo insuficiente')
                            opção = int(input('deseja continuar?\n\
1 - Sim\n\
2 - Não\n'))
                            if opção == 1:
                                
                                limpar_console()
                                ver_carteiras()
                                continue
                            else:
                                limpar_console()
                                indice_carteira()
                else:
                    limpar_console()
                    print('Você digitou uma opção errada, tente novamente!')
                    sleep(2)
                    limpar_console()
        #apresenta essa mensagem caso o jogador digite algo que não seja uma opção    
        except ValueError:
            limpar_console()
            print('Você digitou uma opção errada, tente novamente!')
            sleep(2)
            limpar_console()






def inicio():
    while True:
        indice_carteira()

