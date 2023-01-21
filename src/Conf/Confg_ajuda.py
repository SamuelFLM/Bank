import PySimpleGUI as sg
import re
from Page.Interface_ajuda import Page_ajudar
## Arruma bug
window = Page_ajudar.ajudar()

while True:    
    event, values =window.read()
    if event == sg.WIN_CLOSED:
        break
        
    if(bool(values["email"])):
        email = values["email"]
            
        validacao = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email)
        if validacao and bool(values["comentario"]):
            window["email_titulo"].update(filename="img\img ajuda\Icon\E-mail.png")
            window["line_rosa"].update(filename="img\img ajuda\Icon\Line.png")
            window["rodape"].update(filename="img\img ajuda\Icon\Rodapeon.png")
        else:
            window["email_titulo"].update(filename="img\img ajuda\Icon\Verifique o e-mail digitado.png")
            window["line_rosa"].update(filename="img\img ajuda\Icon\Line Rosa.png")
            window["rodape"].update(filename="img\img ajuda\Icon\Rodapeoff.png")
        # contador = len(values["comentario"])
        # window["caracteres"].update(f"{contador}/ 50 caracteres")
    if event == "rodape":
            pass            