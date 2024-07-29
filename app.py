"""

******Projeto Incompleto**********

Programa usando PySimpleGUI licenciado pelo próprio dev
Sem intuito Comercial, somente como estudo

"""

#Parte onde cria a interface gráfica do projeto

import PySimpleGUI as sg
#tema da interface
sg.theme('reddit')
#Lista de variaves da interface e definindo onde cada um vai ficar
layout = [
    # Um texto             Um campo INPUT (para escrever o que deseja)
    [sg.Text('E-mail'),sg.Input(key='email')],
    # Um texto             Um campo INPUT (para escrever o que deseja, só que com máscara)
    [sg.Text('senha'),sg.Input(key='senha',password_char='*')],
    # Um botão que permite navegar em teus arquivos e salvar ele numa variavél   Mostrando o caminho/nome
    [sg.FolderBrowse('Escolher Pasta Anexos',target='inputAnexos'),sg.Input(key='inputAnexos')],
    [sg.FolderBrowse('Escolher Pasta Planilha',target='inputPlanilha'),sg.Input(key='inputPlanilha')],
    # Um botão com o nome "salvar"
    [sg.Button('Salvar')],
]
#Criando a tela      Título     Formato de como os componentes vão aparecer
janela = sg.Window('Principal',layout=layout)

#Ações da tela

while True:
    #Lê a tela
    event, values = janela.read()
    #Faz uma análise do que foi feito na tela
    if event == sg.WIN_CLOSED:
        #Tela fechou
        break
    elif event == 'Salvar':
        #As informações da tela foram para estas variavéis
        email = values['email']
        senha = values['senha']
        anexos = values['inputAnexos']
        planilha = values['inputPlanilha']
        #Mostrou no terminal se nas variavéis foram salvas
        print(f'{email}, {senha}, {anexos}, {planilha}')