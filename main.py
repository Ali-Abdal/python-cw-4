def my_name():
    print(' Hi My Nmae Is Abdal')

my_name()

def my_meal(food,drink):
    print(f"I like to eat {food} while drinking {drink}")

my_meal("Shawrma","Pepsi max")

def cube(number):
    return number ** 3

def by_three(number):
    
    if number % 3 == 0:
        print(cube(number))
    
    else:
        print("false")

total = by_three(int(input("Random number: ")))

