import sqlite3

class Connection:
    def __init__(self):
        self.conn = sqlite3.connect("BookStore.db")
        self.cursor = self.conn.cursor()

    def select(self):
        self.cursor.execute("SELECT * FROM Books")
        result = self.cursor.fetchall()
        for el in result:
            print(el)
        
    def create(self):
        self.cursor.execute("CREATE TABLE Books(id PRIMARY KEY, title TEXT, year INT)")
        self.conn.commit()
    
    def insert(self):
        while True:
            choice = int(input("\nTo add a book enter 1.\nTo view the database 2.\nTo exit the program enter 0.\n"))
            if choice == 0:
                break
            elif choice == 1:
                book_id = int(input("Enter book ID: "))
                title = input("Enter the title of the book: ")
                year = int(input("Enter the year of the book: "))
                sql = "INSERT INTO Books VALUES(?, ?, ?)"
                val = (book_id, title, year)
                self.cursor.execute(sql, val)
                self.conn.commit()
                print(self.cursor.rowcount, "record(s) affected")
            elif choice == 2:
                self.cursor.execute("SELECT * FROM Books")
                result = self.cursor.fetchall()
                for el in result:
                    print(el)
            else:
                print("Wrong entry!")        
    
    def update(self):
        while True:
            choice = int(input("\nTo update a book enter 1.\nTo view the database enter 2.\nTo exit the program enter 0.\n"))
            if choice == 0:
                break
            elif choice == 1:    
                title = input("Enter the title of the new book: ")
                year = int(input("Enter the year of the new book: "))
                book_id = int(input("Enter the id of the book you want to change: "))
                sql = "UPDATE Books SET title = ?, year = ? WHERE id = ?"
                val = (title, year, book_id)
                self.cursor.execute(sql, val)
                self.conn.commit()
                print(self.cursor.rowcount, "record(s) affected")                
            elif choice == 2:
                self.cursor.execute("SELECT * FROM Books")
                result = self.cursor.fetchall()
                for el in result:
                    print(el)
            else:
                print("Wrong entry!")        
    
    def delete(self):
        while True:
            choice = int(input("\nTo delete a book enter 1.\nTo delete the table enter 2.\nTo exit the program enter 0.\n"))
            if choice == 0:
                break
            elif choice == 1:
                book_id = int(input("Enter the id of the book you want to delete: "))
                sql = "DELETE FROM Books WHERE id = ?"
                val = (book_id, )
                self.cursor.execute(sql, val)
                self.conn.commit()
                print(self.cursor.rowcount, "was deleted.")
            elif choice == 2:
                self.cursor.execute("DELETE FROM Books")
                self.conn.commit()
                print(self.cursor.rowcount, "was deleted.")
            else:
                print("Wrong entry!")
    
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed.")                
       
if __name__ == "__main__":
    pass