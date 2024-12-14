import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uas"
)

mycursor = mydb.cursor()

class User:
    @staticmethod
    def login(username, password):
        try:
            sql = "SELECT level, id FROM user WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            
            if result:
                # Return both level and id
                return str(result[0]), result[1]
            else:
                # Return default values if login fails
                return None, None
        except Exception as e:
            print(f"Login error: {e}")
            return None, None

    @staticmethod
    def select_data():
        sql = "SELECT * FROM user"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    @staticmethod
    def insert_data(nama, alamat, no_hp, username, password, level):
        sql = "INSERT INTO user (nama, alamat, no_hp, username, password, level) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nama, alamat, no_hp, username, password, level)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount