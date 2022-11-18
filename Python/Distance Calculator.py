# Input of user
loop = True

while loop:
    x1 = float(input("Enter x1: "))
    y1 = float(input("\nEnter y1: "))
    x2 = float(input("\nEnter x2: "))
    y2 = float(input("\nEnter y2: "))
    
    # Calculations
    result = ((((x2-x1)**2) + ((y2-y1)**2))**0.5)
    # Output
    print("\nThe Distance Between The Points Are : " + str(result))
