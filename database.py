import mysql.connector
from random import randint
mydb = mysql.connector.connect(
    host = "localhost",user = "root",
    passwd = "Onetoo3#",database = "mydatabase"
)

#in role 0 is student 1 is staff
#userID is username
mycursor = mydb.cursor()

def addComp(UserID):
    print("Enter the model")
    Mno = input()
    print("Lendable? Y/N")
    yn=input()
    if yn=='Y' or yn=='y':
        yn=1
    else:
        yn=0
    slq="INSERT INTO Component (OwnerID ,UserID, model, Lendable) VALUES ('%s','%s','%s',%d);"%(UserID,UserID,Mno,yn)
    mycursor.execute(slq)
    mydb.commit()
    print("Component added!")

def delComp(UserID):
    showComp(UserID)
    print("Enter the component ID")
    compID = int(input())
    presql="UPDATE Transaction SET CompID = NULL WHERE CompID = %d;"%(compID)
    sql="Delete from Component where CompID = %d;"%(compID)
    mycursor.execute(presql)
    mycursor.execute(sql)
    mydb.commit()
    print("Deleted")

def sendComp(UserID):
    showComp(UserID)
    print("Enter the component ID to be sent")
    compID = int(input())
    sql="Select OwnerID from Component where CompID = %d;"%(compID)
    mycursor.execute(sql)
    owner=None
    try:
        owner=mycursor.fetchall()
        owner=owner[0][0]
        print(owner)
    except:
        sendComp(UserID)
    if owner!=UserID:
        print("Not Allowed")
        return
    print("Enter recievers UserID")
    recID = input()
    otp = randint(10000,99999)
    sql="INSERT INTO Transaction (OwnerID ,recieverID, CompID, OTP, status) VALUES ('%s','%s','%s',%d,%d);"%(owner,recID,compID,otp,False)
    mycursor.execute(sql)
    mydb.commit()
    print("OTP :",otp," share it with the reciever")

def recComp(UserID):
    sql="SELECT * FROM Transaction where recieverID='%s' and status=0"%(UserID)
    mycursor.execute(sql)
    print("ID","Owner","CompID")
    for x in mycursor.fetchall():
        print(x[0]," ",x[1],"  ",x[4])
    print("Select TransactionID")
    inp = int(input())
    print("Enter the OTP shared by sender")
    otp = int(input())
    sql="SELECT otp FROM Transaction where recieverID='%s' and status=0"%(UserID)
    mycursor.execute(sql)
    result  = mycursor.fetchall()
    if otp==result[0][0]:
        sql="UPDATE Transaction SET status = 1 where recieverID='%s' and TranID=%d"%(UserID,inp)
        mycursor.execute(sql)
        print("transaction successful")
    else:
        print("wrong otp entered")
    #print("Maybe its done")

def showComp(UserID):
    slq="SELECT * FROM Component"
    mycursor.execute(slq)
    print("ComponentID       Model         Availability")
    for i in mycursor.fetchall():
        if i[4]==1:
            print(i[0],".",i[3], "-- Available")
        else:
            print(i[0],".",i[3],"-- Not Available")
    print("--------")

def addU(UserID):

    print("Enter Name")
    name = input()
    flag = True
    username = ""
    passwd = ""
    while flag:
        print("Enter UserName")
        username = input()
        slq="SELECT UserID FROM user where UserID='"+username+"';"
        mycursor.execute(slq)
        result=mycursor.fetchall()
        if result==[]:
        #print(result)
            break
        else:
            print("Username already taken")
    
    while flag:
        print("Enter password")
        pass1 = input()
        print("Re-enter password")
        pass2 = input()
        if pass1 == pass2:
            passwd = pass1
            break
    print("Select Role")
    print("0 - Student")
    print("1 - Staff")
    role = int(input())
    role = str(role)
    query = "INSERT INTO USER (UserID,Name, Role, passwrd) VALUES ('"+username+"','"+name+"', '"+role+"', '"+ passwd+"');"
    mycursor.execute(query)
    mydb.commit()
    print("Added user : "+ name +" username :"+ username+" successfully")


def delU(UserID):
    print("Enter username to be deleted")
    username = ""
    username = input()
    slq="SELECT UserID FROM user where UserID='"+username+"';"
    mycursor.execute(slq)
    result=mycursor.fetchall()
    if result==[]:
        print("no such username exists")
        return
    else:
        q = "DELETE FROM Transaction WHERE OwnerID='"+username+"';"
        mycursor.execute(q)
        mydb.commit()
        q = "DELETE FROM Login WHERE UserID='"+username+"';"
        mycursor.execute(q)
        mydb.commit()
        q = "UPDATE Component SET OwnerID = NULL WHERE OwnerID='"+username+"';"
        mycursor.execute(q)
        mydb.commit()
        q = "UPDATE Component SET UserID = NULL WHERE UserID='"+username+"';"
        mycursor.execute(q)
        mydb.commit()
        q = "DELETE FROM USER WHERE UserID='"+username+"';" 
        mycursor.execute(q)
        mydb.commit()
    print("Username : "+username+" deleted successfully" )
    if UserID == username:
        main_menu()
    

def run(userID,Role):
    print("Choose the action to be executed")
    count = 1
    print(count , " - Show all Components")
    SHOW = count
    count+=1
    print(count , " - Add components")
    ADD = count
    count+=1
    print(count , " - Delete components")
    DEL = count
    count+=1
    print(count , " - Send Component")
    SEND = count
    count+=1
    print(count , " - Receive components")
    REC = count
    count+=1
    ADDU = -1
    DELU = -1
    if Role == "Staff":
        print(count , " - Add users")
        ADDU = count
        count+=1
        print(count , " - Delete users")
        DELU = count
        count+=1
    print(count , " - Exit")
    EXIT = count
    count+=1
    choice  = int(input())
    if choice == SHOW:
        showComp(userID)
    elif choice ==ADD:
        addComp(userID)
    elif choice ==DEL:
        delComp(userID)
    elif choice ==SEND:
        sendComp(userID)
    elif choice ==REC:
        recComp(userID)
    elif choice ==ADDU:
        addU(userID)
    elif choice ==DELU:
        delU(userID)
    elif choice ==EXIT:
        return True
    else:
        print("choose a valid option")
    return False
    



def main_menu():

    print("Choose the action to be executed")
    print("1 - Login")
    print("2 - Exit")
    choice = int(input())
    if choice==1:
        return False
    elif choice==2:
        return True
    else:
        print("please enter a valid input")
        return main_menu()


def login():
    print("Enter UserID")
    userID = input()
    slq="SELECT UserID FROM Login where UserID='"+userID+"';"
    mycursor.execute(slq)
    result=mycursor.fetchall()
    if result != []:
        print("User is already logged in from different terminal")
        print("1 - logout from there and continue")
        print("2 - Exit")
        c = int(input())
        if c!=1:
            print("Exiting")
            return False,"",0
    print("Enter password")
    passw = input()
    slq="SELECT passwrd FROM user where UserID='"+userID+"';"
    mycursor.execute(slq)
    result=mycursor.fetchall()
    slq="SELECT Role FROM user where UserID='"+userID+"';"
    mycursor.execute(slq)
    role = mycursor.fetchall()
    #print(role[0][0])
    if len(result)<1:
        return False,"student",userID
    else:
        #print(result)
        if passw==result[0][0]:
            query = "INSERT INTO Login (UserID) VALUES ('"+userID+"');"
            mycursor.execute(query)
            mydb.commit()
            if role[0][0] == 1:
                return True,"Staff",userID
            else :
                return True,"Student",userID
    return False,"student",userID

if __name__=="__main__":
    ExitOut = False
    while not ExitOut:
        auth = False
        ExitIn = False
        ExitOut = main_menu()
        if not ExitOut:
            auth,role,userID = login()
        if auth:
            print("Authentication Successful")
            while not ExitIn:
                ExitIn = run(userID,role)
                if ExitIn==False:
                    print("1 - Continue")
                    print("2 - Exit")
                    choice = int(input())
                    if choice==2:
                        break
                    elif choice!=1:
                        print("not valid input")
                        print("continuing")
            try:
                q = "DELETE FROM Login WHERE UserID='"+userID+"';"
                mycursor.execute(q)
                mydb.commit()
            except:
                pass
            print(userID+" logged out")
        elif not ExitOut:
            print("Authentication Failed Try again")
