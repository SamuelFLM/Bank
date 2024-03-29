import PySimpleGUI as sg

def aprovado(home):
    sg.theme_background_color("white")
    cabecalho = [sg.Image(filename="img//img aprovado//icon//Group 20.png", background_color="white", pad=(20,(30,0)))]
    titulo  = [sg.Image(filename="img//img aprovado//icon//Olá, sua conta foi aprovada com sucesso!!.png", background_color="white", pad=(25,(60,50)))]
    mensagem = [sg.Image(filename="img//img aprovado//icon//Use os dados abaixo para efetuar o login no app.png", background_color="white", pad=(25,(0,50)))]
    logo = [sg.Image(filename="img\img Cadastro\Icon\Group 25.png", background_color="white", pad=(15,(0,50)))]
    
    dados_agencia_conta_corrente = [
        [sg.Image(filename="img//img aprovado//icon//Agência.png", background_color="white",pad=(20,(0,20))), sg.Image(filename="img//img aprovado//icon//Conta corrente.png", background_color="white", pad=(100,(0,20)))],
        [sg.Input("4325",background_color="white", disabled_readonly_background_color="white",border_width=0,k="agencia",disabled=True, s=(10,0), pad=(20,(0,0)),font="Inter 13"), sg.Input("123456-1",background_color="white",disabled_readonly_background_color="white",disabled=True ,border_width=0,k="contacorrente", s=(10,0), pad=(65,(0,0)),font="Inter 13")],
        [sg.Image(filename="img//img aprovado//icon//Line 12 (1).png", background_color="white",pad=(20,(0,0))),sg.Image(filename="img//img aprovado//icon//Line 12 (1).png", background_color="white", pad=(10,(0,0)))]
    ]
    senha_eletronica = [
        [sg.Image(filename="img//img aprovado//icon//Senha eletrônica.png", background_color="white", pad=(20,(50,0)))],
        [sg.Input("1234",background_color="white", disabled_readonly_background_color="white",border_width=0,k="senha_eletronica",disabled=True, s=(10,0), pad=(20,(20,0)),font="Inter 13")],
        [sg.Image(filename="img//img aprovado//icon//Line 13.png", background_color="white", pad=(20,(0,100)))]
        
    ]
    rodape = [[sg.Image(filename="img//img aprovado//icon//rodape.png", background_color="white" , pad=(0,(30,0)), enable_events=True, k="efetuarlogin")]]
    
    layout = [cabecalho,titulo,mensagem,logo,dados_agencia_conta_corrente,senha_eletronica,rodape]
    
    window = sg.Window("APROVADO", layout, size=(410, 750), margins=(0,0),icon="img//logo.ico")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "efetuarlogin":
            window.close()
            home()
            break