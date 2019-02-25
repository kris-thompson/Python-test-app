class calculator:
    def add(a,b):
        x = int(a) + int(b)
        return x
    def subtract(a,b):
        x = int(a) - int(b)
        return x
    def multiply(a,b):
        x = int(a) * int(b)
        return x
    def divide(a,b):
        x = int(a) / int(b)
        return x
class messages:        
    def getInput():
        chk = ""
        while chk == "":
            a = input("Enter the first number:  ")
            try:
                val = int(a)
                if val == int(a):
                    chk = "1"
            except ValueError:
                print("Numeric input only")
                
        chk = ""
        while chk == "":
            b = input("Enter the second number:  ")
            try:
                val = int(b)
                if val == int(b):
                    chk = "1"
            except ValueError:
                print("Numeric input only")
                
        return a, b       


option = ""
while option not in ["add","subtract","multiply","divide"]:#!= "add" or option != "subtract" or option != "multiply" or option != "divide":   
       
    try:
        option = input("Would you like to add,subtract,multiply or divide?  ")

        if option == "add":
            a, b = messages.getInput()
            x = calculator.add(a,b)
        elif option == "subtract":
            a, b = messages.getInput()
            x = calculator.subtract(a,b)
        elif option == "multiply":
            a, b = messages.getInput()
            x = calculator.multiply(a,b)
        elif option == "divide":
            a, b = messages.getInput()
            x = calculator.divide(a,b)
        else:
            print ("Please enter an option from the list")
    except ValueError:
        print("You must enter an option from the list, try again.")
print (a, option, b, "equals", x)
                    
