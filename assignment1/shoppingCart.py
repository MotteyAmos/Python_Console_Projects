'''class ShopItems:
    _items_with_price ={
            "shirt":50,
            "pant": 10,
            "dress":40,
            "jewelry":80,
            "hats":20,
            "fruit":20,
            "televisions":90
        }

    def getItemsWithPrice():
        return ShopItems._items_with_price

class ShoppingCart(ShopItems):
    shopItems = ShopItems.getItemsWithPrice()
    def __init__(self):
        self.items = []
        self.total_price = 0

    #add one item
    def addItem(self, item):
        key_value=item
        while True:
            key_value 
            if item.lower() in ShoppingCart.shopItems.keys() :
                self.items.append(item)
                print("inserted")
                break
            else:
                print(key_value, " not in shope items")
                print(ShoppingCart.shopItems)
                item = input("Enter item again: ")
                continue
   
    #add multiple items at once
    def addItems(self):
        while True:
            self.addItem(input("Enter item name: "))
            if (input("Type done after selecting all items or any other key to continue: ").lower() == "done"):
                break
            else:
                continue

    #get total price of items picked
    def getTotalPrice(self):
        for pickedItems in self.items:
            self.total_price += ShoppingCart.shopItems[pickedItems] 
        print("Total price of your items is: ", self.total_price)

    # remove an item from items picked
    def removeItem(self,item):
        if(item in self.items):
            self.items.remove(item)
            print(item, " is removed")
        else:
            print(item " not in list")
            print(self.items)
 
    

shoppingCart1 = ShoppingCart()
shoppingCart1.addItems()
shoppingCart1.getTotalPrice()

 '''   
'''
class Employee:
    def __init__(self):
        self.__name =""
        self.__age = 0
        self.__salary=0.0
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    def setSalary(self,salary):
        self.salary = salary
    
    def getSalary(self):
        return self.salary
'''
'''
class Student:
    def __init__(self):
        self.__name = ""
        self.__studentID = ""
        self.__courseList = []
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setStudentID(self, studentID):
        self.__studentID = studentID
    
    def getStudentID(self):
        return self.__studentID

    def addCourse(self, *courses):
        if courses:
            for course in courses:
                self.__courseList.append(course)
        else:
            return
    
    def removeCourse(self, course):
        if course in self.__courseList:
            self.__courseList.remove(course)
        else:
            print(course, " not in courses")
    
    def displayCourses(self):
        for course in self.__courseList:
            print(course.title())

student1 = Student()
student1.setName("Router")
student1.setStudentID('10987142')
student1.addCourse("introduction to computer science", "hacking", "software Engineering", "machine learning")
student1.removeCourse("machine leaning")
student1.displayCourses()
'''



from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self):
        self.owner = ''
        self.balance = 0.0
    
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def setOwner(self, owner):
        self.owner = owner
    
    def getOwner(self):
        return self.owner

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()
    
    def withdraw(self, amount):
        transaction_fee = 0.50
        if (transaction_fee + amount < self.balance):
            balance -= (amount + transaction_fee)
            print("Your current balance is: ", balance)
        else:
            print("You have insufficient amount in your account")


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def withdraw(amount):
         if (amount < self.balance):
            balance -= (amount + transaction_fee)
            print("Your current balance is: ", balance)
        else:
            print("You have insufficient amount in your account")