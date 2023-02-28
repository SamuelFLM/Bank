import PySimpleGUI as sg
import re

def cadastro(home):
    sg.theme_background_color("white")
    cabecalho = [
                sg.Image(filename="img//img Cadastro//Icon//esquerda.png", background_color="white", pad=(20,(30,0)), enable_events=True, k="voltar"),
                sg.Image(filename="img//img Cadastro//Icon//Criarconta.png", background_color="white", pad=(10,(30,0)), enable_events=False, k="ajuda"),
                ]
    logo = [sg.Image(filename="img//img Cadastro//Icon//logo.png", background_color="white", pad=(20,(50,30))),]
    dados_nome_sobrenome = [
        [sg.Image(filename="img//img Cadastro//Icon//Nome.png", background_color="white", pad=(30,(30,0))),
         sg.Image(filename="img//img Cadastro//Icon//Sobrenome.png", background_color="white",  pad=(110,(30,0))),],
        [sg.Input("",background_color="white", border_width=0,k="nome", s=(10,0), pad=(30,(30,0)), font="Inter 13"),sg.Input("",background_color="white", border_width=0,k="sobrenome", s=(10,0), pad=(60,(30,0)),font="Inter 13"),],
        [sg.Image(filename="img//img Cadastro//Icon//linha_sobrenome.png", background_color="white", pad=(30,(0,40))),
         sg.Image(filename="img//img Cadastro//Icon//linha_sobrenome.png", background_color="white", pad=(5,(0,40))),]
    ]
    dados_email = [[sg.Image(filename="img//img Cadastro//Icon//E-mail.png", background_color="white", pad=(30,(0,0)))],
                   [sg.Input("",background_color="white", border_width=0,k="email", s=(40,0), pad=(30,(20,0)),font="Inter 13")]
                   ,sg.Image(filename="img//img Cadastro//Icon//linha_email.png", background_color="white",pad=(30,(0,40))),]
    
    dados_cpf = [[sg.Image(filename="img//img Cadastro//Icon//CPF.png", background_color="white", pad=(30,(0,0)))],
                 [sg.Input("",background_color="white", border_width=0,k="cpf", s=(15,0), pad=(30,(20,0)),font="Inter 13")],
                 sg.Image(filename="img//img Cadastro//Icon//linha_cpf.png", background_color="white", pad=(30,(0,50))),]
    
    dados_data_nascimento = [[sg.Image(filename="img//img Cadastro//Icon//Data Nascimento.png", background_color="white", pad=(30,(0,0)))],
                             [sg.Input("",background_color="white", border_width=0,k="data_nascimento", s=(9,0), pad=(30,(20,0)),font="Inter 13", )],
                             sg.Image(filename="img//img Cadastro//Icon//linha_dt_nascimento.png", background_color="white", pad=(30,(0,70))),]
    
    rodape = [sg.Image(filename="img//img Cadastro//Icon//off.png", background_color="white", enable_events=True, key="continuar", pad=(0,(30,0)))]
    
    layout = [cabecalho,logo,dados_nome_sobrenome,dados_email,dados_cpf,dados_data_nascimento,rodape]
    window = sg.Window("Cadastro", layout=layout, size=(410, 750), margins=(0,0), icon="img//logo.ico")
    
    while True:
        event, values =window.read(timeout=1)
        if event == sg.WIN_CLOSED:
                break
        if event == "voltar":
            window.close()
            home()
            break
        
        # if(bool(values["email"])):
        #         email = values["email"]
        #         validacao = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email)
        #         if validacao:
        #             return True
        #         else:
        #             return False
        
        # if bool(values["cpf"]):
        #     cpf = values["cpf"]
        #     validacao_cpf = re.search(r'([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})',cpf)
        #     if validacao_cpf and (len(cpf) == 11):
        #         return True
        #     else:
        #         return False
                
            
if __name__ == "__main__":
    cadastro(home="")