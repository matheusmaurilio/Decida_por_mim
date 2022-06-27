#Esse programa permite que o usuário faça uma pergunta e escreve uma resposta para ela

import random
import PySimpleGUI as PSG

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso',
            'Não sei, decida por si mesmo',
            'Não faça isso',
            'Você não tem nada melhor para fazer? '
        ]
    def Iniciar(self):
        layout = [ 
            [PSG.Text('Faça sua pergunta:')],
            [PSG.Input()],
            [PSG.Output((20,10))],
            [PSG.Button('Decida por mim')]
        ]
        self.janela = PSG.Window('Decida por mim', layout)
        while True:
            self.eventos, self.valores = self.janela.Read() 

            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
            if self.eventos == PSG.WIN_CLOSED:    
                break
            
            
decida_por_mim = DecidaPorMim()
decida_por_mim.Iniciar()
