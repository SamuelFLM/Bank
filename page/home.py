import PySimpleGUI as sg


sg.theme_background_color("#0A1B1E")
def home():
    cabecalho = [sg.Image(filename="img\img home\Logo\logo2.png", pad=(0,(0,0)), background_color=sg.theme_background_color())]
    opcao = [
        [sg.Image(filename="img\img home\Icon\Invista com Taxa Zero.png", pad=(0,(60,0)), background_color=sg.theme_background_color())],
        [sg.Image(filename="img\img home\Icon\soucliente.png", pad=(0,(30,0)), background_color=sg.theme_background_color())],
        [sg.Image(filename="img\img home\Icon\criarconta.png", pad=(0,(0,0)), background_color=sg.theme_background_color())],
    ]
    
    layout = [cabecalho, opcao]
    window = sg.Window("Home", layout, size=(410, 750), margins=(0,0), element_justification="c")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
home()