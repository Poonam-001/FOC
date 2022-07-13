def book(): #defined class
    global book_name
    global author_name
    global quantity
    global price
    book_name = [] #created bookname list
    author_name = [] #created authorname list
    quantity = [] #created quantity list
    price = [] #created price list
    with open("BookStock.txt","r") as file: # dependent on text file
        lines = file.readlines() #read text file
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            p = 0 # initialized variable
            for a in lines[i].split(','):
                if(p == 0):
                    book_name.append(a)
                elif(p == 1):
                    author_name.append(a)
                elif(p == 2):
                    quantity.append(a)
                elif(p == 3):
                    price.append(a.strip("$"))
                p += 1
