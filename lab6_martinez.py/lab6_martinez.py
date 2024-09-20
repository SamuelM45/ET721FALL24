'''
Samuel Martinez
Sep 20, Python Classes
'''

print("\n --- Example 1: Exception Handling ---")

def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        
        hours /= h  # hours = hours / h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined")
    except ValueError:
        print(f"Input value was not a number.")
    except:
        print("Program has error")
# calling the function

print(hour_ratio())
print("\n === END OF PROGRAM 1 ===")

print("\n --- Example 2: Classes --- ")
# define a class named 'Complex'
class Complex: 
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart

#c create an instance of the class
point1 = Complex(3.0, -4.5)

#calling the instance object
real1 = point1.r
imag1 = point1.r

#prompt result
print(f"real number = {real1} with imaginary number = {imag1}")

print("\n --- Example 3: Classes with properties and methods --- ")
class Car:
    # properties, attributes, of class Car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # methods of class Car
    # method 1: print of description of the class Car
    def get_descriptive_name(self):
        full_name = f"{self.year}, {self.make}, {self.model}"
        return full_name
    
    # method 2: read and print the odometer
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    
    # method 3: update and print odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    # method 4: increment odometer
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# create an instance of class Car
usercar1 = Car("audi", "a4", 2020)

# accessing properties and methods
print(usercar1.year)

# accessing the method 'get_descriptive_name'
print(usercar1.get_descriptive_name())
usercar1.read_odometer()    
usercar1.update_odometer(100)
usercar1.read_odometer()
usercar1.update_odometer(20)
usercar1.read_odometer()

usercar1.increment_odometer(35)
usercar1.read_odometer() 


print("\n --- Exercise --- ")

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0 

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print(f"Insufficient funds. Cannot withdraw ${amount:.2f}.")


useraccount = BankAccount("123456789", "Samuel Martinez")

useraccount.withdraw(700)  
useraccount.deposit(1000)
useraccount.withdraw(500)

print(f"Final balance: ${useraccount.balance:.2f}")