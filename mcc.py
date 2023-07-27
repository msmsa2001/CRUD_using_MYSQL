import mysql.connector as connector

class MCC:
    def __init__(self) :
        self.con=connector.connect(host="localhost",
                        port='3306',
                        user='root',
                        password="leewayzon",
                        database="pythontest")
        
        query='create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
    
    #Insert
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User Saved to db")
    
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for  row in cur:
            print("User Id",row[0])
            print("User Name",row[1])
            print("User Phone ",row[2])
            print()

    #Fetch Simpel one
    def fetch_one(self,id):
        query="select * from user where userId={}".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        for  row in cur:
            print("User Id",row[0])
            print("User Name",row[1])
            print("User Phone ",row[2])
            print()

    #Delete user
    def delete_user(self,id):
        query="delete from user where userId={}".format(id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")
        
    def update_user(self,userID,newName,newPhone):
        query="update user set userName='{}',phone='{}' where userId={}".format(newName,newPhone,userID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query) 
        self.con.commit()
        print("Updated")       
