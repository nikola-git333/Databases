import mysql.connector
 
class Baza:
    __instance = None
 
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Baza.__instance is None:
            Baza()
        return Baza.__instance
 
    def __init__(self):
        """ Virtually private constructor. """
        if Baza.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sakila', port=3306)
            self.__cursor = self.__db.cursor()
            Baza.__instance = self
 
    def prikaziSeme(self):
        self.__cursor.execute("SHOW DATABASES")
        shemas = self.__cursor.fetchall()
        for shema in shemas:
            print(shema)
 
    def unesiShemuNaKojuSePrijavljujes(self):
        print("Unesi semu:")
        sema = str(input())
        upit = "USE " + sema
        print(upit)
        self.__cursor.execute(upit)
 
    def prikaziTabele(self):
        self.__cursor.execute("SHOW TABLES")
        tables = self.__cursor.fetchall()
        for table in tables:
            print(table)
 
    def listajSadrzajIzTabele(self, tabela):
        self.__cursor.execute("SELECT * FROM " + tabela)
        records = self.__cursor.fetchall()
        for record in records:
            print(record)
 
    def obrisiPodatakPoIDu(self, id, tabela):
        try:
            self.__cursor.execute("DELETE FROM " + tabela + " WHERE id = " + id)
            self.__db.commit()
        except:
            self.__db.rollback()
 
    def prikaziKolone(self, tabela):
        self.__cursor.execute("SHOW COLUMNS FROM " + tabela)
        columns = self.__cursor.fetchall()
        for column in columns:
            print(column)
 
    def azurirajPodatakPoIDu(self, id, tabela, kolona, novaVrednost):
        try:
            upit = "UPDATE " + tabela + " SET " + kolona + "='" + novaVrednost + "' WHERE id = " + id
            print(upit)
            self.__cursor.execute(upit)
            self.__db.commit()
        except:
            self.__db.rollback()
 
 
if __name__ == "__main__":
    '''k = Baza()
    print(id(k))
    k2 = Baza.getInstance()
    print(id(k2))'''
    b = Baza()
    print(id(b))
    b = Baza.getInstance()
    print(id(b))
    b.prikaziTabele()
    print("----------------------------")
    b.prikaziSeme()
    b.unesiShemuNaKojuSePrijavljujes()
    b.prikaziTabele()
    tabela = input("Unesi tabelu: ")
    b.listajSadrzajIzTabele(tabela)
    print("----------------------------")
    b.prikaziKolone(tabela)
    b.obrisiPodatakPoIDu(input("Unesi id za brisanje: "), tabela)
    b.listajSadrzajIzTabele(tabela)
    b.azurirajPodatakPoIDu(input("Unesi id za azuriranje: "), tabela, input("Unesi kolonu za azuriranje: "), input("Unesi novu vrednost: "))
    b.listajSadrzajIzTabele(tabela)