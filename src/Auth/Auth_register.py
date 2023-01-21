from Auth_conexao import Connection

class Register:
    
    def __init__(self, email, senha):
        self.conexao = Connection()
        self.email = email
        self.senha = senha
        
    def registro(self):
        _sql_inserir_dados = f"""
        INSERT INTO REGISTRO VALUES('{self.email}', '{self.senha}')
        """
        self.conexao.cursor.execute(_sql_inserir_dados)
        self.conexao.cursor.commit()
        
if __name__ == "__main__":
    # OK
    reg = Register("admin", "admin")
    reg.registro()