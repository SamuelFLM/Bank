import PySimpleGUI as sg
from Interface_login import *
from Interface_cadastro import *
from Interface_ajuda import *

def home():
    cabecalho = [sg.Image(filename="img\img home\Icon\Group 26.png", pad=(0,(0,0)), background_color=sg.theme_background_color("white") ,enable_events=True)]
    opcao = [
        [sg.Image(filename="img\img home\Icon\image 1.png", pad=(0,(60,20)), background_color=sg.theme_background_color("white"))],
        [sg.Image(filename="img\img home\Icon\Benefícios em DOBRO.png", pad=(0,(30,20)), background_color=sg.theme_background_color("white"), enable_events=True)],
        [sg.Image(filename="img\img home\Icon\Group 7.png", pad=(0,(40,0)), background_color=sg.theme_background_color("white"),enable_events=True, key="login")],
        [sg.Image(filename="img\img home\Icon\Group 8.png", pad=(0,(0,30)), background_color=sg.theme_background_color("white"),enable_events=True, key="cadastro")],
        [sg.Image(filename="img\img home\Icon\Enviar dúvida ou comentario..png", pad=(0,(0,0)), background_color=sg.theme_background_color("white"),enable_events=True, key="ajuda")],
    ]
    
    layout = [cabecalho, opcao]
    window = sg.Window("Home", layout, size=(410, 750), margins=(0,0), element_justification="c", icon="img//logo.ico", grab_anywhere=True)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "login":
            window.close()
            login(home=home)
            break
        if event == "ajuda":
            window.close()
            ajudar(home=home)
            break
        
        if event == "cadastro":
            window.close()
            cadastro(home=home)
            break
if __name__ == "__main__":
    home()  