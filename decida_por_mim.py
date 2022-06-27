#Esse programa permite que o usuário faça uma pergunta e escreve uma resposta para ela

import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso',
            'Não sei, decida por si mesmo',
            'Não faça isso',
            'Você não tem nada melhor para fazer? '
        ]
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida_por_mim = DecidaPorMim()
decida_por_mim.Iniciar()
