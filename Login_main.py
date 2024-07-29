import PySimpleGUI as sg

def register():
    register_layout=[[sg.Text("Account:")],[sg.InputText()],
                     [sg.Text("Password:")],[sg.InputText()],
                     [sg.Text("Confirm Password")],[sg.InputText()],
                     [sg.Button("Cancel")],[sg.Button("OK")]]
    
    window=sg.Window('register_system', register_layout)
    
    while True:
        event , value = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
            
        account=input()
        password=input()
        print(account)
        print(password)
        print("confirm your password")
        password_confirm=input()
    
        if event=='OK':
            if password_confirm == password : 
                print("correct")
                break
            else :
                print("not the same password")
                print("please confirm password again")
                password_confirm=input()
   
        list1.append([account,password])
        print(list1)
   


def login():
    print("enter your account and password respectively")
    account=input()
    password=input()
    for i in range(0,len(list1)):
        if account==list1[i][0]:
            password_temp=list1[i][1]
            break
    # print(password_temp)

    for i in range (1,4):
        if(password==password_temp):
            print("successfully entered")
            return
        else:
            print("unsuccessfully entered,please enter password again")
            print("try again , remain times left : " , 4-i)
            password=input() 
        
def resetpassword():
    print("reset your password next")
    print("please enter your account name")
    while True:
        account=input()
        account_found=False
        for i in range(0,len(list1)):
            if account==list1[i][0]:
                print("account founded")
                a=i
                newpassword()
                return  
        if not account_found:
            print("Account not found , please enter correct account")   
        


def newpassword():
    print("Please enter new password")
    new_password=input()
    print("confirm new password")
    new_password_confirm=input()
    while True :
        if new_password==new_password_confirm :
            list1[a][1]=new_password
            return
        else:
            print("not the same password detected")
            print("confirm new password again")
            new_password_confirm=input()

a=1
list1=[]


