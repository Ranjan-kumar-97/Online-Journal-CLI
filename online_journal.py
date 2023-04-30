from online_journal_db import OnlineJournalDB


def onlineJournal():
    db = OnlineJournalDB()
    while True:
        print("\n***** WELCOME TO ONLINE JOURNAL *****\n")
        print("Tyoe Insert to insert a Journal")
        print("Type Fetch to Fetch all Journal details by using Journal ID")
        print("Tyoe Delete to Delete a Journal by using Journal ID")
        print("Type Update to Update a Journal details by using Journal ID")
        print("Press Q to to Exit from Online Journal\n")

        try:
            choice = input().lower()
            if(choice == 'insert'):
                #checking ID
                id = int(input("Please Enter Journal Id : "))
                if db.fetch_id(id) == 1:
                    print("ID already Exists!..")
                    continue
                else:
                    #insert
                    jt = input("Please Enter Journal Title (Max 200 ch.) : ")
                    jw = input("Please Enter Writer Name (Max 200 ch.) : ")
                    jc = input("Please Enter Writer/Publisher contact Number : ")
                    jp = input("Please Enter Journal Published Date (DD-MM-YYYY) : ")
                    j = input("Please Start Writing Journal here (Max 1500 ch. ) : ")
                    db.insert_journal(jid,jt, jw, jc, jp, j)

            elif(choice == 'fetch'):
                #Fetch All Details
                db.fetch_all()

            elif(choice == 'delete'):
                #checking ID
                id = int(input("Please Enter Journal Id : "))
                if db.fetch_id(id) == 0:
                    print("ID does not Exist!..")
                    continue
                else:
                    #Delete Journal
                    jid = int(input("Enter Journal ID to delete : "))
                    db.delete_journal(jid)

            elif(choice == 'update'):
                #checking ID
                id = int(input("Please Enter Journal Id : "))
                if db.fetch_id(id) == 0:
                    print("ID does not Exist!..")
                    continue
                else:
                    #update Journal
                    jid = int(input("Enter Journal ID to Update Details : "))
                    jt = input("Please Enter New Journal Title (Max 200 ch.) : ")
                    jw = input("Please Enter New Writer Name (Max 200 ch.) : ")
                    jc = input("Please Enter New Writer/Publisher contact Number : ")
                    jp = input("Please Enter New Journal Published Date (DD-MM-YYYY) : ")
                    db.update_journal(jid,jt, jw, jc, jp)
                
            elif(choice == 'q'):
                print("See You again!..")
                break

            else:
                print("Invalid Input! Please try again!..")
        except Exception as e:
            print(e)
            print("Wrong Choice!..")



if __name__ == '__main__':
    onlineJournal()