import Book# imported Book module
import DateTime#imported DateTime module
def return_():
    name = input("Enter name of borrower: ")#input name of the borrower who came to return book
    a = "Borrow-" + name + ".txt"#read text file of the borrower
    try:
        with open(a,"r") as file:
            lines = file.readlines()#read line of the BookStock
            lines = [a.strip("$") for a in lines]
    
        with open(a,"r") as file:
            data=file.read()
            print(data)
    except:
        print("Sorry! this is not a valid borrower name.")
        return_()

    b = "Return-" + name + ".txt"#create text file of the user while returning
    with open(b,"w+")as file:
        file.write("Library  \n")# title of the scenario
        file.write("Returned By: "+ name+"\n")#name of the user while returning
        file.write("Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")#get date time and store in textfile
        file.write("S.N.    Bookname       Price \n")# title of the list or table contents


    total=0.0
    for i in range(5):
        if Book.book_name[i] in data:
            with open(b,"a") as file:
                file.write(str(i+1)+"    "+Book.book_name[i]+"    $"+Book.price[i]+"\n")
                Book.quantity[i]=int(Book.quantity[i])+1
            total+=float(Book.price[i])
            
    print("Rate of books that is borrowed: "+" "+"$"+str(total))#display rate of the books that is borrowed
    print("Is return date of the book expired?")#Ask for valid choice
    print("Enter Yes(Y) or No(N)")
    
    choice=input()
    if(choice.upper()=="Y"):
        print("How many days was late to return book?")
        day=int(input())#input number of days that exceed the deadline
        fine = 2*day#fine is $2 times number of days after deadline
        with open(b,"a")as file:
            file.write("Fine: $"+ str(fine)+"\n")# fine is written in text file
            total=total+fine
            print("Total fine: "+ "$"+str(total))
        with open(b,"a")as file:
            file.write("Total: $"+ str(total))
            print("In upcoming days submit your book on time. Thank you!")
            print("")
            
        with open("BookStock.txt","w+") as file:
            for i in range(5):
                file.write(Book.book_name[i]+","+Book.author_name[i]+","+str(Book.quantity[i])+","+"$"+Book.price[i]+"\n")
    else:
        print("Thank you for submitting the book on time.")
        print("")
