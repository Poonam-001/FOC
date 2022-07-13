
import Book#imported Book module
import BookBorrowed#imported BookBorrowed module
import BookReturned#imported BookReturned module
import DateTime#imported DateTime module

def final():
    while(True):
        print("Welcome")#display message
        print(" ")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow")
        print("Enter 3. To Return")
        print("Enter 4. To Exit")
        try:
            a=int(input("Select a paticular number:"))#input valid number
            print()
            if(a==1):#if user choice is 1 do the following
                with open("BookStock.txt","r") as file:#open BookStock
                    lines=file.read()#read BookStock
                    print(lines)#display books in the BookStock
                    print()
   
            elif(a==2):#if user choice is 2 continue the borrow process
                Book.book()
                BookBorrowed.borrow()
            elif(a==3):#if user choice is 3 continue the return process
                Book.book()
                BookReturned.return_()
            elif(a==4):#if user choice is 4 terminate the program
                print("Thank you! Visit Again.")#Display message
                break
            else:
                print("Enter a valid choice.")
        except ValueError:
            print("Enter a valid input")
final()
