print("This is simple password manager")

def add():
    username = input("Please enter username: ")
    pwd = input("Please enter password: ")
    with open('passwords.txt','a') as p:
        p.write(username + '|' + pwd + '\n')
    
def view():
    with open('passwords.txt','r') as p:
        for line in p.readlines():
            print(line)
        

while True:
    pwd = input("U want to add or view the passwords you have(view/add)or q for quit? ").lower()
    if pwd == 'q':
        break
    if pwd == 'view':
        view()
    elif pwd == 'add':
        add()
    else:
        print("Invalid Please try again")