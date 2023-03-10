import PySimpleGUI as sg
import re
import pyautogui as bot
def ajudar(home):
        sg.theme_background_color("white")
        cabecalho = [
            [sg.Image(filename="img\img ajuda\Icon\Voltar.png", background_color="white", pad=(15,(40,20)),enable_events=True, key="voltar")],
            [sg.Image(filename="img\img ajuda\Icon\Olá, como podemos te ajudar_.png", background_color="white", pad=(30,(40,40)))],
            [sg.Image(filename="img\img ajuda\Icon\Envie sua dúvida ou comentário.png", background_color="white", pad=(35,(5,40)))]],
        
        email = [
            [sg.Image(filename="img\img ajuda\Icon\E-mail.png", background_color="white", pad=(35,(5,20)),k="email_titulo")],
            [sg.Input("",font="Inter 13",size=(50,2),pad=(35,(0,0)), border_width=0, background_color="white", k="email")],
            [sg.Image(filename="img\img ajuda\Icon\Line.png", background_color="white", pad=(35,(5,20)),key="line_rosa")],
                ]
        comentario = [
            [sg.Image(filename="img\img ajuda\Icon\Comentário.png", background_color="white", pad=(35,(5,20)))],
            [sg.Input("",font="Inter 13",size=(50,2),pad=(35,(0,0)), border_width=0, background_color="white", k="comentario")],
            [sg.Image(filename="img\img ajuda\Icon\Line.png", background_color="white", pad=(35,(5,20)))],
            [[sg.Text("0 / 500 caracteres", background_color="white", text_color="black",pad=(35,(10,0)), key="caracteres")]],]
        rodape = [[sg.Image(filename="img\img ajuda\Icon\Rodapeoff.png", background_color="white", enable_events=True,pad=(0,(170,0)), key="rodape")],]
        layout = [cabecalho,email,comentario,rodape]
        
        window = sg.Window("Ajuda", layout=layout, size=(410, 750), margins=(0,0))
        while True:    
            event, values =window.read(timeout=1)
            if event == sg.WIN_CLOSED:
                break
        
            contador = len(values["comentario"])
            window["caracteres"].update(f"{contador}/ 500 caracteres")
        
            if event == "voltar":
                window.close()
                home()
                break
                
            if(bool(values["email"]) and bool(values["comentario"])):
                window["rodape"].update(filename="img\img ajuda\Icon\Rodapeon.png")
            else:
                window["rodape"].update(filename="img\img ajuda\Icon\Rodapeoff.png")
            if(bool(values["email"])):
                email = values["email"]
                validacao = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email)
                if validacao:
                    window["email_titulo"].update(filename="img\img ajuda\Icon\E-mail.png")
                    window["line_rosa"].update(filename="img\img ajuda\Icon\Line.png")
                else:
                    window["email_titulo"].update(filename="img\img ajuda\Icon\Verifique o e-mail digitado.png")
                    window["line_rosa"].update(filename="img\img ajuda\Icon\Line Rosa.png")
                    window["rodape"].update(filename="img\img ajuda\Icon\Rodapeoff.png")

            if event == "rodape":
                    pass       
