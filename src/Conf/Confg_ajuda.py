import PySimpleGUI as sg
import re
## Arruma bug
window = 1

while True:    
    event, values =window.read()
    if event == sg.WIN_CLOSED:
        break
        
    if(bool(values["email"])):
        email = values["email"]
            
        validacao = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email)
        if validacao:
            window["email_titulo"].update(filename="img\img ajuda\Icon\E-mail.png")
            window["line_rosa"].update(filename="img\img ajuda\Icon\Line.png")
        else:
            window["email_titulo"].update(filename="img\img ajuda\Icon\Verifique o e-mail digitado.png")
            window["line_rosa"].update(filename="img\img ajuda\Icon\Line Rosa.png")
        # contador = len(values["comentario"])
        # window["caracteres"].update(f"{contador}/ 50 caracteres")
    if event == "rodape":
            pass            