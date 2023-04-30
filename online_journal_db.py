import mysql.connector as connector
import os
from dotenv import load_dotenv

load_dotenv("db_password.env")
passwrd = os.getenv("pass")

class OnlineJournalDB:
    def __init__(self):
        self.con = connector.connect(host = 'localhost',port = '3306', user = 'root', password = passwrd, database = 'online_journal')
        create_table_query = "CREATE TABLE IF NOT EXISTS journals(JournalId int PRIMARY KEY , Title varchar(200) NOT NULL, Writer varchar(200) NOT NULL, Contact varchar(15) ,Published varchar(10), Journal varchar(1500) NOT NULL) "
        cur = self.con.cursor()
        cur.execute(create_table_query)


    #Inserting new journal
    def insert_journal(self, jid, jt, jw, jc, jp, j):
        insert_query = "INSERT INTO journals(JournalId, Title, Writer, Contact, Published, Journal) VALUES ({},'{}','{}','{}','{}','{}')".format(jid,jt,jw,jc,jp,j)
        cur = self.con.cursor()
        cur.execute(insert_query)
        self.con.commit()
        print("One Journal Successfully Created ")
        
    #Fetching All data axcept Journal Content
    def fetch_all(self):
        fetch_query = "SELECT JournalId, Title, Writer, Contact, Published FROM journals"
        cur = self.con.cursor()
        cur.execute(fetch_query)
        for row in cur:
            print("Journal Id : ", row[0],", Title : ",row[1],", Writer : ",row[2],", Contact : ",row[3],", Published : ",row[4])

    #Deleting a Journal by taking Journal Id
    def delete_journal(self, jid):
        delete_query = "delete from journals where journalId= '{}'".format(jid)
        cur = self.con.cursor()
        cur.execute(delete_query)
        self.con.commit()
        print("Journal deleted having ID : ", jid)

    #Upting Jounal details except journal content by taking Journal Id 
    def update_journal(self,jid, njt, njw, njc, njp):
        updateJd_query = "UPDATE journals SET Title = '{}', Writer = '{}', Contact = '{}', Published = '{}' where JournalId = {}".format(njt,njw,njc,njp,jid)
        cur = self.con.cursor()
        cur.execute(updateJd_query)
        self.con.commit()
        print("Journal Details Updated having ID : ", jid)






