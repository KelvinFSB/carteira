from datetime import datetime

class Transacao:
    '''
    classe responsavel por criar as informações das trasações

    output:
    valor
    descrição
    data

    '''
    def __init__(self, valor, descricao):
        self.valor = valor
        self.descricao = descricao
        self.data = datetime.now()