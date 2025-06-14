import socket
import jsonpickle
import pyodbc

def authreg():
    option = conn.recv(1024).decode()
    authorisation = jsonpickle.decode(conn.recv(1024).decode())
    if option == "r":
        if checkAuthorisation(dsn, authorisation): conn.send("Already registered".encode())
        else: conn.send(register(dsn, authorisation).encode())
    elif option == "a":
        if checkAuthorisation(dsn, authorisation): conn.send("Authorised".encode())
        else: conn.send("Not authorised".encode())
    else:
        conn.send("Wrong input".encode())

def register(dsn, authorisation):
    try:
        conn = pyodbc.connect(dsn)
        cursor = conn.cursor()
        insert_query = "INSERT INTO [Users] VALUES (?, ?, ?)"
        values = (authorisation['name'], authorisation['login'], authorisation['password'])
        cursor.execute(insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return "Registered"
    except Exception as e:
        print(f"Error: {e}")
        return "Not registered"

def checkAuthorisation(dsn, authorisation):
    try:
        conn = pyodbc.connect(dsn)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [Users]")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        for row in rows:
            if authorisation['login'] == row[2] and authorisation['password'] == row[3]:
                return True
    except Exception as e:
        print(f"Error: {e}")
    return False

IP = "127.0.0.1"
PORT = 4000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost\\SQLEXPRESS;DATABASE=db_test;UID=;PWD=;Trusted_Connection=yes;'
server.listen(1)
conn, addr = server.accept()
authreg()
conn.close()
server.close()
