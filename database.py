import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Onetoo3#",
    database = "mydatabase"
)

#in role 0 is student 1 is staff
#userID is username
mycursor = mydb.cursor()

def addComp(UserID):
    print("Enter the Name")
    name  = input()
    print("Enter the model number")
    Mno = int(input())
    compID = 0
    #some sql shit
    print(compID)

def delComp(UserID):
    print("Enter the component ID")
    compID = int(input())
    #some sql shit

def sendComp(UserID):
    print("Enter the component ID to be sent")
    compID = int(input())
    print("Enter recievers UserID")
    recID = int(input())
    #some sql shit

def recComp(UserID):
    #search the transaction table
    print("print the OTP")

def showComp(UserID):
    print("show comp")

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
        addU(userID)
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
        return -1
    else:
        #print(result)
        if passw==result[0][0]:
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
        elif not ExitOut:
            print("Authentication Failed Try again")
