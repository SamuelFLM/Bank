import PySimpleGUI as sg

background = background_color = "black"

def register():
    
    cabecalho = [
        [sg.Image(filename="img\img Register\Logo\logo.png", expand_x=True,pad=(0,(0,0)))]
    ]
    
    cadastro = [
        [sg.Image(filename="img\img Register\Icon\CADASTRO.png", background_color=background, pad=(115,(30,0)))],
        #EMAIL
        [sg.Image(filename="img\img Register\Icon\E-MAIL.png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(80,20), font="arial 11 bold",pad=(40,(20,0)), background_color="orange",border_width=0, text_color="white", justification="left", key="email", focus=True, disabled_readonly_text_color="white")],
        [sg.Image(filename="img\img Register\Icon\line.png", background_color=background, pad=(0,(0,0)))],
        #SENHA
        [sg.Image(filename="img\img Register\Icon\SENHA.png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(30,0), font="arial 11 bold",pad=(40,(20,0)), background_color=None, text_color="orange", justification="left", key="senha", password_char="*")]
    ]
    
    rodape = [
        [sg.Image(filename="img\img Register\Icon\checkoff.png", background_color=background, pad=(0,(40,0)), enable_events=True, key="check"),sg.Image(filename="img\img Register\Icon\licenca.png",background_color=background,pad=(10,(40,0)))],
        [sg.Image(filename="img\img Register\Icon\direita.png", background_color=background,pad=(0,(40,0)))]
    ]
    
    layout = [cabecalho, cadastro,rodape]
    
    window = sg.Window("CADASTRO", layout,size=(293,510), background_color=background,grab_anywhere=True, element_justification="center",margins=(0,0),)
    return window


window = register()
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break