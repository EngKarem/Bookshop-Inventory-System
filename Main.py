from Book import Book
import pandas as pd

Data = pd.read_csv('Database.csv')

print("Bookshop Inventory System")
print("=" * 30)
while True:
    book = Book
    print("1- Add New Book\n"
          "2- Search by Title\n"
          "3- Search by Author\n"
          "4- List of Books\n"
          "5- Delete Book\n"
          "6- Add to the current Stock of a Book\n"
          "7- Remove from the current Stock of a Book\n"
          "8- Show Total Value of the Books\n"
          "9- Exit")

    choice = int(input())
    if choice == 1:
        Title = input("Enter the Book Title: ")
        Author = input("Enter the Book Author: ")
        Category = input("Enter the Book Category: ")
        quantity = int(input("Enter the Book Quantity: "))
        unit_price = int(input("Enter the unit Price: "))
        book = Book(Data.shape[0]+1, Title, Author, Category, quantity, unit_price)
        book.Add_Book()

    elif choice == 2:
        Title = input("Enter the Book Title: ")
        print(book.search_by_title(Data, Title))
        print("=" * 30)

    elif choice == 3:
        Author = input("Enter the Book Author: ")
        print(book.search_by_Author(Data, Author))
        print("=" * 30)

    elif choice == 4:
        book.List_Data(Data)
        print("=" * 30)

    elif choice == 5:
        ID = int(input("Enter the Book ID You Want To Delete: "))
        book.Delete_Book(Data, ID)

    elif choice == 6:
        ID = int(input("Enter the Book ID: "))
        Quan = int(input("Enter Quantity you want to add: "))
        book.AddToStock(ID, Quan)

    elif choice == 7:
        ID = int(input("Enter the Book ID: "))
        Quan = int(input("Enter Quantity you want to add: "))
        book.RemoveFromStock(ID, Quan)

    elif choice == 8:
        book.ShowTotalValue(Data)

    elif choice == 9:
        print("Good-by")
        break
    else:
        print("Enter Valid Input")
