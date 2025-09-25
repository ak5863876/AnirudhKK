# Name: Anirudh Krishnamoorthy
# ID: 433007975
def triangle_type_checker():
    """Determining the type of a triangle from its sides"""
    A=int(input("Enter the value for side A:")) # Entering the value for side A
    B=int(input("Enter the value for side A:")) # Entering the value for side B
    C=int(input("Enter the value for side A:")) # Entering the value for side C1
    if A==B and B==C and C==A:
        print("It's an equilateral triangle!!!") # If sides are equal, then, equilateral triangle
    elif A==B or B==C or C==A:
        print("It's an isoceles triangle") # If two sides are equal, then, isoceles triangle
    else:
        print("It's a scalene triangle") # If sides are unequal, then, scalene triangle
def MAIN():
    """Executing the program within the main function"""
    while True:
        print("===STEPS===") # Step by Step Procedure
        print("1. Determining the type of triangle by its sides.")
        print("2. Exit!!")
        choice=int(input("Enter the choice from the above steps:"))
        if choice==1:
            triangle_type_checker() # Peforming the function
        elif choice==2:
            print("Exiting the program!!!") # Exit the function
            break
        else:
            print("Invalid choice!!! Please try again!!!")
MAIN()