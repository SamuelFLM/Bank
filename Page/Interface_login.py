import PySimpleGUI as sg

background = background_color = "black"

def login():
    
    cabecalho = [
        [sg.Image(filename="img\img Login\Logo\logo.png", expand_x=True,pad=(0,(0,0)))]
    ]
    
    cadastro = [
        [sg.Image(filename="img\img Login\Icon\LOGIN.png", background_color=background, pad=(115,(30,0)))],
        #EMAIL
        [sg.Image(filename="img\img Login\Icon\E-MAIL.png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(30,0), font="arial 11 bold",pad=(40,(20,0)), background_color="#FF8A00", text_color="white", justification="center", key="emailLogin")],
        #SENHA
        [sg.Image(filename="img\img Login\Icon\SENHA.png", background_color=background, pad=(125,(40,0)))],
        [sg.Input("", size=(30,0), font="arial 11 bold",pad=(40,(20,0)), background_color="#FF8A00", text_color="white", justification="center", key="senhaLogin", password_char="*")]
    ]
    
    rodape = [
        [sg.Image(filename="img\img Login\Icon\esquerda.png", background_color=background,pad=(30,(60,0)),enable_events=True,key="voltar"),
         sg.Image(filename="img\img Login\Icon\direita.png", background_color=background,pad=(30,(60,0)),enable_events=True,key="continuar")]
    ]
    
    layout = [cabecalho, cadastro,rodape]
    
    window = sg.Window("CADASTRO", layout,size=(293,510), background_color=background,grab_anywhere=True, element_justification="center",margins=(0,0),)
    return window


window = login()
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "voltar":
        print("voltando")
    if event == "continuar":
        print("continuando")
        