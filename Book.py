import csv


class Book:

    def __init__(self, ID, Title, Author, Category, quantity, unit_price):
        self.ID = ID
        self.Title = Title
        self.Author = Author
        self.Category = Category
        self.quantity = quantity
        self.unit_price = unit_price
        self.Total_price = quantity * unit_price

    @staticmethod
    def List_Data(Data):
        print(f"Data was read successful \nwe have {Data.shape[0]} books available right now")
        print(Data.head(Data.shape[0]))

    @staticmethod
    def search_by_title(Data, Title):
        return Data.loc[Data['Title'] == Title]

    @staticmethod
    def search_by_Author(Data, Author):
        return Data.loc[Data['Author'] == Author]

    def Add_Book(self):
        with open('Database.csv', mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(
                [self.ID, self.Title, self.Author, self.Category, self.quantity, self.unit_price, self.Total_price])
        f.close()

    @staticmethod
    def Delete_Book(Data, ID):
        r = csv.reader(open('Database.csv'))
        lines = list(r)
        for i in range(Data.shape[0]):
            for j in range(Data.shape[1]):
                if lines[i][j] == str(ID):
                    print("Record Deleted")
                    del lines[i]

        with open('Database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
        f.close()

    @staticmethod
    def AddToStock(ID, Quantity):
        r = csv.reader(open('Database.csv'))
        lines = list(r)
        oldQuantity = int(lines[ID][4])
        Unit_Price = float(lines[ID][5])
        oldQuantity += Quantity
        lines[ID][4] = oldQuantity
        lines[ID][6] = oldQuantity * Unit_Price
        with open('Database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
        f.close()

    @staticmethod
    def RemoveFromStock(ID, Quantity):
        r = csv.reader(open('Database.csv'))
        lines = list(r)
        oldQuantity = int(lines[ID][4])
        Unit_Price = float(lines[ID][5])
        oldQuantity -= Quantity
        lines[ID][4] = oldQuantity
        lines[ID][6] = oldQuantity * Unit_Price
        with open('Database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
        f.close()

    @staticmethod
    def ShowTotalValue(Data):
        Sum = 0
        for i in range(Data.shape[0]):
            Sum += Data.loc[i, 'Total_Price']
        print(Sum)
