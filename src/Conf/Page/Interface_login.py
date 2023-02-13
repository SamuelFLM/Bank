import PySimpleGUI as sg

def login():
    sg.theme_background_color("white")
    cabecalho = [[sg.Image(filename="img//img Login//Icon//chevron-left-24.png", background_color="white", pad=(10,(20,60)), enable_events=True, k="voltar"),sg.Image(filename="img//img Login//Icon//Group 21.png", background_color="white", pad=(15,(20,60)), enable_events=True, k="ajuda")]]
    logo = [sg.Image(filename="img//img Cadastro//Icon//logo.png", background_color="white", pad=(20,(50,0)))]
    agencia_conta_corrente = [
        [sg.Image(filename="img//img Login//Icon//Agência.png", background_color="white", pad=(25,(50,0))), sg.Image(filename="img//img Login//Icon//Conta corrente.png", background_color="white", pad=(95,(50,0)))],
        [[sg.Input("",background_color="white", border_width=0,k="agencia", s=(10,0), pad=(25,(20,0)), font="Inter 13"),sg.Input("",background_color="white", border_width=0,k="conta_corrente", s=(10,0), pad=(60,(20,0)),font="Inter 13"),],],
        [sg.Image(filename="img//img Login//Icon//Line 4.png", background_color="white", pad=(25,(0,40))),
         sg.Image(filename="img//img Login//Icon//Line 4.png", background_color="white", pad=(5,(0,40))),]
        ]
    senha_eletronica = [
        [sg.Image(filename="img//img Login//Icon//Senha eletrônica.png", background_color="white", pad=(25,(0,0)))],
        [sg.Input("",background_color="white", border_width=0,k="agencia", s=(10,0), pad=(25,(30,0)), font="Inter 13")],
        [sg.Image(filename="img//img Login//Icon//Line 5.png", background_color="white", pad=(25,(0,30)))],
    ]
    rodape = [sg.Image(filename="img\img Login\Icon\Group 15.png", background_color="white", pad=(0,(220,0)))]
    
    layout = [cabecalho,logo,agencia_conta_corrente,senha_eletronica,rodape]
    window = window = sg.Window("Login", layout, size=(410, 750), margins=(0,0), icon="img//logo.ico")
    
    while True:
        event, values = window.read(timeout=1)
        if event == sg.WIN_CLOSED:
            break
login()