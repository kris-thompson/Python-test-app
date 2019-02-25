option = int(0)
while option == 0 or option > 4: 
        
    print ("1: calculator")
    print ("2: picture")
    print ("3: clock")
    print ("4: Quit")
    try:
        option = int(input("Please select an option:  "))

        if option == 1:
            import Calculator
        elif option == 2:
            import picture
        elif option == 3:
            import clock
        elif option == 4:
            exit()
        else:
            print ("Please enter a number from the list")
    except ValueError:
        print("You must enter a number, try again.")

print ("all done!")        
    
