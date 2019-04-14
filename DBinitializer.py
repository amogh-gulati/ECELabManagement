import mysql.connector

def doStuff():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Onetoo3#",
         )
    except:
        print("mysql database not connected")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    mydb = mysql.connector.connect(user='root',
    password='Onetoo3#', host='127.0.0.1',
     port='3306', database="mydatabase")

    mycursor = mydb.cursor()

    sql1 = "CREATE TABLE IF NOT EXISTS Transaction (TranID int PRIMARY KEY AUTO_INCREMENT,OwnerID varchar(32),recieverID varchar(32),OTP int,CompID int,status bool NOT NULL,FOREIGN KEY (OwnerID) REFERENCES USER(UserID),FOREIGN KEY (recieverID) REFERENCES USER(UserID),FOREIGN KEY (CompID) REFERENCES Component(CompID));"
    sql2 = "CREATE TABLE IF NOT EXISTS Component (CompID int PRIMARY KEY AUTO_INCREMENT,OwnerID varchar(32),UserID varchar(32),model varchar(32),Lendable bool NOT NULL,FOREIGN KEY (OwnerID) REFERENCES USER(UserID),FOREIGN KEY(UserID) REFERENCES USER(UserID));"
    sql3 = "CREATE TABLE IF NOT EXISTS USER (UserID varchar(32) PRIMARY KEY ,Name varchar(32),Role int NOT NULL,passwrd varchar(32));"
    sql4 = "CREATE TABLE IF NOT EXISTS Login (LoginID int PRIMARY KEY AUTO_INCREMENT,UserID varchar(32), FOREIGN KEY (UserID) REFERENCES USER(UserID));"

    # mycursor.execute("CREATE DATABASE mydatabase;")

    mycursor.execute(sql3)
    mycursor.execute(sql4)
    mycursor.execute(sql2)
    mycursor.execute(sql1)

    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    mycursor.execute("INSERT INTO USER (UserID,Name, Role, passwrd) VALUES ('root','root', '1', 'password');")
    mydb.commit()


if __name__=="__main__":
    doStuff() 
