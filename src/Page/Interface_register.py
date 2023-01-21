import PySimpleGUI as sg

background = background_color = "black"

def register():
    
    cabecalho = [
        [sg.Image(filename="img\img Register\Logo\logo.png", expand_x=True,pad=(0,(0,0)))]
    ]
    
    cadastro = [
        [sg.Image(filename="img\img Register\Icon\CADASTRO (1).png", background_color=background, pad=(100,(30,0)))],
        #EMAIL
        [sg.Image(filename="img\img Register\Icon\E-MAIL (1).png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(80,20), font="arial 14 bold",pad=(20,(20,0)), background_color="#FF8A00", text_color="black", justification="center", key="email")],
        [sg.Image(filename="img\img Register\Icon\line.png", background_color=background, pad=(0,(5,0)))],
        #SENHA
        [sg.Image(filename="img\img Register\Icon\SENHA (1).png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(80,20), font="arial 14 bold",pad=(20,(20,0)), background_color="#FF8A00", text_color="black", justification="center", key="senha", password_char="*")],
        [sg.Image(filename="img\img Register\Icon\line.png", background_color=background, pad=(0,(5,0)))],
    ]
    
    rodape = [
        [sg.Image(filename="img\img Register\Icon\checkoff.png", background_color=background, pad=(0,(40,0)), enable_events=True, key="check"),sg.Image(filename="img\img Register\Icon\licenca.png",background_color=background,pad=(10,(40,0)))],
        [sg.Image(filename="img\img Register\Icon\direita.png", background_color=background,pad=(0,(30,0)))]
    ]
    
    layout = [cabecalho, cadastro,rodape]
    
    window = sg.Window("CADASTRO", layout,size=(293,510), background_color=background,grab_anywhere=True, element_justification="center",margins=(0,0),)
    return window


window = register()
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break