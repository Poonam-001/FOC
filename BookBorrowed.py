import Book #imported book module
import DateTime #imported DateTime module

def borrow():
    success=False
    while(True):
        fName=input("Enter the first name of the borrower: ")#input first name of the borrower
        if fName.isalpha():
            break
        print("Enter a valid input.")
    while(True):
        lName=input("Enter the last name of the borrower: ")#input last name of the borrower
        if lName.isalpha():
            break
        print("Enter a valid input.")
            
    t="Borrow-"+fName+".txt"
    with open(t,"w+") as file:
        file.write("Library \n")# topic of the text file
        file.write("Borrowed By: "+ fName+" "+lName+"\n")# first and last name of the borrower
        file.write("Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")#Write Date and time of the borrow day
        file.write("S.N.      Bookname              Authorname         Price\n" )# Title of the table

   #code for borrowing a book 
    while success==False:
        print("Please select a option below:")
        for i in range(len(Book.book_name)):
            print("Enter", i, "to borrow book", Book.book_name[i])
    
        try:   
            a=int(input())
            try:
                if(int(Book.quantity[a])>0):# book available if quantity is greater than 0
                    print("Book is available. You can get one.")
                    with open(t,"a") as file:
                        file.write("1.     "+ Book.book_name[a]+"      "+Book.author_name[a]+"          "+"$"+Book.price[a]+"\n")

                    Book.quantity[a]=int(Book.quantity[a])-1#deduction of the quantity after borrowing
                    with open("BookStock.txt","w+") as file:
                        for i in range(5):
                            file.write(Book.book_name[i]+","+Book.author_name[i]+","+str(Book.quantity[i])+","+"$"+Book.price[i]+"\n")


                    #code for borrowing multiple books
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? Enter Y(Yes) or N(No)."))# selecting choice
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Select an option below:")
                            
                            for i in range(len(Book.book_name)):
                                print("Enter", i, "to borrow book", Book.book_name[i])# input for borrowing book
                                
                            a=int(input())
                            if(int(Book.quantity[a])>0):# book available if greater than 0
                                print("Book is available.You can get one.")
                                with open(t,"a") as file:
                                    file.write(str(count) +".     "+ Book.book_name[a]+"      "+Book.author_name[a]+"      "+Book.price[a]+"\n")

                                Book.quantity[a]=int(Book.quantity[a])-1# deduct quantity of borrowed books
                                with open("BookStock.txt","w+") as file:
                                    for i in range(5):
                                        file.write(Book.book_name[i]+","+Book.author_name[i]+","+str(Book.quantity[i])+","+"$"+Book.price[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                            
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books.")
                            print("")
                            loop=False
                            success=True
                            
                        else:
                            print("Choose as instructed")
                        
                else:
                    print("Sorry! Book is not available")
                    borrowBook()
                    success=False
                    
            except IndexError:
                print("")
                print("Choose valid number of books.")
                
        except ValueError:
            print("")
            print("Please select as suggested.")
