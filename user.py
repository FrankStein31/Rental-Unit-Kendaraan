import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uas"
)

mycursor = mydb.cursor()

class User:
    
    def __init__(self):
        self
    
    def login(val1, val2):
        sql = "SELECT level FROM user WHERE username = %s AND password = %s"
        val = (val1, val2)
        mycursor.execute(sql, val)
        level = mycursor.fetchone()
        return str(level[0]) if level else None

    def select_data():
        sql = "SELECT * FROM user"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    
    def insert_data(nama, alamat, no_hp, username, password, level):
        sql = "INSERT INTO user (nama, alamat, no_hp, username, password, level) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nama, alamat, no_hp, username, password, level)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")

