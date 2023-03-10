from Auth_conexao import Connection
from Auth_register import Register

class Login:
    def __init__(self, registro):
        self.conexao = Connection()    
        self.registro = registro
        
    def validacao_usuario_existente(self):
        _sql_valida_usuario_existente = f"""
        SELECT EMAIL,SENHA FROM REGISTRO WHERE EMAIL='{self.registro.email}' and SENHA='{self.registro.senha}'
        """
        self.conexao.cursor.execute(_sql_valida_usuario_existente)
        validacao = self.conexao.cursor.fetchall()
        
        if (validacao):
            return True
        else:
            return False    
    
if __name__  == "__main__":
    login = Login(Register("admin", "admin"))
    login.validacao_usuario_existente()