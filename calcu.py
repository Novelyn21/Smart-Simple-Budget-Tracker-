def addition(x,y):
    return x + y 
def substract(x,y):
    return x - y
def product(x,y):
    return x * y
def divide(x,y):
    return x/y

while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. substract")
    print("3. Product")
    print("4. Division")
    print("5. Exit")


    choice = input("Enter choice (1-5): ")
    if choice == '5':
        print("Exit")
        break
    
    if choice in('1', '2', '3', '4'):
        try:
           num1 = float(input("Enter 1st num: "))
           num2 = float(input("Enter 2nd num: "))
        except ValueError:
            print("Invalid, enter numbers only.")
            continue

        if choice == '1':
            print(f"Results {num1} + {num2} = {addition(num1, num2)}")
        
        elif choice == '2':
             print(f"Results {num1} - {num2} = {substract(num1, num2)}")
        
        elif choice == '3':
             print(f"Results {num1} * {num2} = {product(num1, num2)}")
        
        elif choice == '4':
             print(f"Results {num1} / {num2} = {divide(num1, num2)}")

    else:
            print("Please enter the correct numbers")