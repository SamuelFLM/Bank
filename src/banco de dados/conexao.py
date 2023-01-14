import pyodbc

class Connection:
    
    def __init__(self):
        self.server = "localhost\SQLEXPRESS"
        self.database = "LOGIN"

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes;')
        cursor = cnxn.cursor()

if __name__ == "__main__":
    conexao = Connection()