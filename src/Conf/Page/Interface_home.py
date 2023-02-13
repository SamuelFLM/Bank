import PySimpleGUI as sg
from Interface_login import *
from Interface_cadastro import *
from Interface_ajuda import *

def home():
    cabecalho = [sg.Image(filename="img\img home\Logo\logo2.png", pad=(0,(0,0)), background_color=sg.theme_background_color("#0A1B1E") ,enable_events=True, key="ajuda")]
    opcao = [
        [sg.Image(filename="img\img home\Icon\Invista com Taxa Zero.png", pad=(0,(60,0)), background_color=sg.theme_background_color("#0A1B1E"))],
        [sg.Image(filename="img\img home\Icon\soucliente.png", pad=(0,(30,0)), background_color=sg.theme_background_color("#0A1B1E"), enable_events=True, key="login")],
        [sg.Image(filename="img\img home\Icon\criarconta.png", pad=(0,(0,0)), background_color=sg.theme_background_color("#0A1B1E"),enable_events=True, key="cadastro")],
    ]
    
    layout = [cabecalho, opcao]
    window = sg.Window("Home", layout, size=(410, 750), margins=(0,0), element_justification="c", icon="img//logo.ico")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "login":
            pass
        if event == "ajuda":
            window.close()
            ajudar(home=home)
            break
        
        if event == "cadastro":
            window.close()
            cadastro(home=home)
            break
        
home()