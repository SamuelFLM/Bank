import pyodbc

class Connection:
    
    def __init__(self):
        self.server = "localhost\SQLEXPRESS"
        self.database = "LOGIN"
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes;') 
        self.cursor = self.cnxn.cursor()

if __name__ == "__main__":
    # OK 
    conexao = Connection()