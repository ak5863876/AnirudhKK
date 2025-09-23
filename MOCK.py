def Even_Odd():
    '''To check whether the number is even or odd'''
    num=int(input("Enter number to check whether it's even or odd:"))
    if num%2==0: #To check whether the number is divisible by 2
        print("Even number")
    else:
        print("Odd number")
def Pos_Neg():
    '''To check whether the number is positive or negative'''
    num=int(input("Enter number to check whether it's positive or negative:"))
    if num>0: #To check whether the number is greater than 0
        print("Positive number")
    else:
        print("Negative number")
def SQUARE():
    '''To find the square of the number'''
    num=int(input("Enter number to find its square:"))
    square_num=num**2 #To find square of the number
    print("Square of number:",square_num)
def CUBE():
    '''To find the cube of the number'''
    num=int(input("Enter number to find its cube:"))
    cube_num=num**3 #To find cube of the number
    print("Cube of number:",cube_num)
def MAIN():
    '''Menu-Driven Program for performing the function'''
    while True:
        print("=====MENU=====") #To perform the menu-driven program
        print("1. Check the number whether it is even or odd.")
        print("2. Check the number whether it is positive or negative.")
        print("3. Finding number's square value.")
        print("4. Finding number's cube value.")
        print("5. Exiting the program!!!!")
        choice=int(input("Enter the choice from the menu:"))
        if choice==1:
            Even_Odd()
        elif choice==2:
            Pos_Neg()
        elif choice==3:
            SQUARE()
        elif choice==4:
            CUBE()
        elif choice==5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
MAIN()