import PySimpleGUI as sg
import pyautogui as bot
def login(home):
    sg.theme_background_color("white")
    cabecalho = [[sg.Image(filename="img//img Login//Icon//chevron-left-24.png", background_color="white", pad=(10,(20,60)), enable_events=True, k="voltar"),sg.Image(filename="img//img Login//Icon//Group 21.png", background_color="white", pad=(15,(20,60)), enable_events=True, k="ajuda")]]
    logo = [sg.Image(filename="img\img Cadastro\Icon\Group 25.png", background_color="white", pad=(20,(50,0)))]
    agencia_conta_corrente = [
        [sg.Image(filename="img//img Login//Icon//Agência.png", background_color="white", pad=(25,(50,0))), sg.Image(filename="img//img Login//Icon//Conta corrente.png", background_color="white", pad=(95,(50,0)))],
        [[sg.Input("",background_color="white", border_width=0,k="agencia", s=(10,0), pad=(25,(20,0)), font="Inter 13"),sg.Input("",background_color="white", border_width=0,k="conta_corrente", s=(10,0), pad=(60,(20,0)),font="Inter 13"),],],
        [sg.Image(filename="img//img Login//Icon//Line 4.png", background_color="white", pad=(25,(0,40))),
         sg.Image(filename="img//img Login//Icon//Line 4.png", background_color="white", pad=(5,(0,40))),]
        ]
    senha_eletronica = [
        [sg.Image(filename="img//img Login//Icon//Senha eletrônica.png", background_color="white", pad=(25,(0,0)))],
        [sg.Input("",background_color="white", border_width=0,k="senha_eletronica", s=(10,0), pad=(25,(30,0)), font="Inter 13")],
        [sg.Image(filename="img//img Login//Icon//Line 5.png", background_color="white", pad=(25,(0,30)))],
    ]
    rodape = [sg.Image(filename="img\img Login\Icon\Group 15.png", background_color="white", pad=(0,(220,0)), enable_events=True, k="esqueceu_senha")]
    
    layout = [cabecalho,logo,agencia_conta_corrente,senha_eletronica,rodape]
    window = window = sg.Window("Login", layout, size=(410, 750), margins=(0,0), icon="img//logo.ico")
    
    while True:
        event, values = window.read(timeout=1)
        if event == sg.WIN_CLOSED:
            break
        
        agencia = str(values["agencia"])
        conta_corrente = str(values["conta_corrente"])
        senha = str(values["senha_eletronica"])
        
        
        if event == "voltar":
            window.close()
            home()
            break
        
        if agencia == "4325" and conta_corrente == "123456-1" and senha == "1234":
            bot.confirm(title="ENTROU", text="VOCE ENTROU NO SISTEMA COM SUCESSO", buttons=["OK"])
            validacao = bot.confirm(title="ENTROU", text="DESEJA CONTINUAR?", buttons=["OK", "SAIR"])
            if validacao == "SAIR":
                break
            if validacao == "OK":
                window["agencia"].update("")
                window["conta_corrente"].update("")
                window["senha_eletronica"].update("")