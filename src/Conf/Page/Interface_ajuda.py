import PySimpleGUI as sg
import re
sg.theme_background_color("white")

class Page_ajudar:
    
    def ajudar():
    
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
            [[sg.Text("0/ 50 caracteres", background_color="white", text_color="black",pad=(35,(10,0)), key="caracteres")]],]
        rodape = [[sg.Image(filename="img\img ajuda\Icon\Rodapeoff.png", background_color="white", enable_events=True,pad=(0,(170,0)), key="rodape")],]
        layout = [cabecalho,email,comentario,rodape]
        
        window = sg.Window("Ajuda", layout=layout, size=(410, 750), margins=(0,0))
        return window
       