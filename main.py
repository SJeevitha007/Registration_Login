def register():
    db = open("user_database.txt","r+")
    Email = input("Enter username:")
    Password=input("Enter Password:")
    Password1=input("Re-Enter Password:")
    name=[]
    pswd=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        name.append(a)
        pswd.append(b)
    if (Email[0].isalpha()):
        try:
            username,url=Email.split("@")
            website,extension=url.split(".")
            if (len(website) < 1):
                print("something wrong in url")
                register()
            if (website.isalnum()) is False:
                print("Invalid id,something wrong in url")
                return register()
            if (1<=len(extension)<=3) is False:
                print("Invalid id, ext")
                register()
        except:
            print("Something  wrong")
            register()
    else:
        print("Invalid id, Num /special added,start again")
        register()

    if Password==Password1:
         if 5< len(Password) <16:
            l, u, d, s = 0, 0, 0, 0
            special = "!@#$%^&*()"
            for i in Password:
                if (i.islower()):
                    l+=1
                if (i.isupper()):
                    u+=1
                if (i.isdigit()):
                    d+=1
                if (i in special):
                    s+=1
            if (l>=1 and u>=1 and d>=1 and s>=1):
                pass
            else:
                print("Invalid password!,Please follow the password conditions")
                register()
         else:
            print("Password doesn't meet the length criteria Please restart")
            register()
    else:
        print("Password not match")
        register()
    if Email in name:
        print("User id Exist,register with different user_id")
        register()
    else:
        db=open("user_database.txt","a")
        db.write(Email+", "+ Password+ "\n" )
        print("Successfully registered!")
def login():
    db=open("user_database.txt","r")
    Email= input("Enter user id:")
    Password=input("Enter the password:")
    flag=0
    name=[]
    pswd=[]
    for i in db:
        a, b = i.split(",")
        b=b.strip()
        name.append(a)
        pswd.append(b)
        data=dict(zip(name,pswd))
    if Email not in name:
        print("User id doesn't exist,Please register ")
        register()

    for name, pswd in data.items():
        if Password==data[Email]:
            print("Login Successful")
            break
            #print("Login Successful")
        else:
            s=input("Incorrect Password,want to try again yes/no:")
            if s=="yes":
                login()
            else:
                x= input("Forgot Password yes/no:")
                if x=="yes":
                    id=input("Enter the user_id")
                    for name, pswd in data.items():
                        if id==name:
                            print("The correct password is :",pswd)
def home():
    Choose=input("Login / Register:")
    if Choose=="Login":
        print("Login:")
        login()
    elif Choose=="Register":
        print("Register:")
        register()
    else:
        print("Choose the the options")
home()












