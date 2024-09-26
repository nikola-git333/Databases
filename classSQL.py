import mysql.connector

class Konekcija:
    
    def __init__(self):   
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database = "novadatabase",
        port=3306
        )
        self.mycursor = self.mydb.cursor()

    def select(self):
        self.mycursor.execute('SELECT * FROM users')
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
            
    def insert(self):
        sql = "INSERT INTO users (name, address) VALUES (%s, %s)"    
        val = [                                                      
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633')
            ]
        self.mycursor.executemany(sql, val)                 
        self.mydb.commit()
        print(self.mycursor.rowcount, "was inserted.") 
    
    def update(self,new = str,old = str):
        sql = "UPDATE users SET address = %s WHERE address = %s"
        val = (new, old)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) affected")
                                
    def delete(self):
        self.mycursor.execute('DELETE FROM users')
        self.mydb.commit()
        print(self.mycursor.rowcount, "was deleted.")
        

if __name__ == "__main__":
    conn = Konekcija()
    conn.delete()
    conn.insert()
    conn.update('Cornio 1','Mountain 21')
    conn.select()