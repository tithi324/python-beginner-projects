from datetime import date

def add_expense():
    item = input("enter the item purchased: ")
    expense = input("Enter the amount: Rs.")
    with open('test.txt','a') as f:
        f.write(f"{item} - {expense}\n")

choice = input("Do you want to add(a) or view(v) items?")
if (choice == 'v'):
    with open('test.txt','r') as f:
        for i in f.readlines():
            print(i, end =' ')
        
else:
    present_day = str(date.today())

    with open('test.txt','a') as f:
        f.write(f"{present_day}\n")
    while True:
        add_expense()
        choice2 = input("Press c to continue and e to exit")
        if (choice2 == 'e'):
            exit()
        