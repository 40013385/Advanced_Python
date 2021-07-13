"""
This is a Cafe management billing system project.
Bill for the order is calculated automatically instead of manually.
"""


class Cafe:
    """Details of customer, table number"""
    def __init__(self):
        """Details defined"""
        self.cust_name = 2
        self.no_of_people = 3
        self.table_no = 4
        self.cost = None
        self.quan = None

    def customer(self):
        """Give inputs of customer, people with the customer and table """
        print("Enter name of the customer: ")
        self.cust_name = input()
        print("Enter no. of people: ")
        self.no_of_people = input()
        print("Enter the table no assigned: ")
        self.table_no = input()


class Menu:
    """Items in the Menu defined with price and billing calculation"""
    def __init__(self):
        """Details of cost and quantity defined"""
        self.cost = None
        self.quan = None

    def sweetcornsoup(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 120
        return self.cost

    def garlicbread(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 120
        return self.cost

    def paneerpizza(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 220
        return self.cost

    def paneer65(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 150
        return self.cost

    def paneertikka(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 200
        return self.cost

    def honeychillypotato(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 100
        return self.cost

    def babycornfry(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 150
        return self.cost

    def crispycorn(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 120
        return self.cost

    def alootikki(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 150
        return self.cost

    def manchurian(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 150
        return self.cost

    def frenchfries(self):
        """Provide input and totalling is done"""
        print("Enter the quantity: ")
        self.quan = int(input())
        self.cost = self.quan * 100
        return self.cost


class Selection(Menu):
    """Declaring menu options and price"""
    def __init__(self, option):
        """Menu option and price."""
        self.option = option
        self.price = 0

    def choose(self):
        """Items in the Menu defined"""
        print("1. sweetcornsoup")
        print("2. garlicbread")
        print("3. paneerpizza")
        print("4. paneer65")
        print("5. paneertikka")
        print("6. honeychillypotato")
        print("7. babycornfry")
        print("8. crispycorn")
        print("9. alootikki")
        print("10. manchurian")
        print("11. frenchfries")

        while True:
            try:
                option = int(input("Select the food item: "))
                if option == 1:
                    self.price += obj1.sweetcornsoup()
                elif option == 2:
                    self.price = self.price + obj1.garlicbread()
                elif option == 3:
                    self.price = self.price + obj1.paneerpizza()
                elif option == 4:
                    self.price = self.price + obj1.paneer65()
                elif option == 5:
                    self.price = self.price + obj1.paneertikka()
                elif option == 6:
                    self.price = self.price + obj1.honeychillypotato()
                elif option == 7:
                    self.price = self.price + obj1.babycornfry()
                elif option == 8:
                    self.price = self.price + obj1.crispycorn()
                elif option == 9:
                    self.price = self.price + obj1.alootikki()
                elif option == 10:
                    self.price = self.price + obj1.manchurian()
                elif option == 11:
                    self.price = self.price + obj1.frenchfries()
                else:
                    break
                print("The total price is:", self.price)
            except Exception as error:
                print("Error: Not valid food option", error)
                print("Please provide integer food item number")


obj1 = Menu()
obj2 = Cafe()
obj2.customer()
obj = Selection("")
obj.choose()
