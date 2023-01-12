import PySimpleGUI as sg

background = background_color = "black"
def home():
    
    cabecalho = [
        sg.Image(filename="img\img home\Logo\logo.png", background_color=background, pad=(0,(50,0)))
    ]
    
    login= [
        [sg.Image(filename="img\img home\Icon\entrar.png", background_color=background, pad=(0,(150,0)))],
        [sg.Image(filename="img\img home\Icon\criarcadastro.png", background_color=background, pad=(0,(30,0))) ],
        [sg.Image(filename="img\img home\Icon\Precisa de ajuda_.png", background_color=background, pad=(0,(50,0)))],
    ]
    layout = [cabecalho, login]
    window = sg.Window("Ion Itau", layout=layout, size=(293,510), background_color=background,grab_anywhere=True, element_justification="center")
    return window

window = home()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break