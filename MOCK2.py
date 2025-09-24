def Vowel_Consonant():
    '''Taking a string from the user'''
    str1=input("Enter a string to find no. of vowels and consonants:")
    VOWELS="AEIOUaeiou"
    vowel=0
    consonant=0
    for char in str1[::]:
        if char in VOWELS: # Counting the no. of vowels and consonants
            vowel+=1
        else:
            consonant+=1
    print("No. of vowels in str1:",vowel)
    print("No. of consonants in str1:",consonant)
def Palindrome():
    '''Checking whether the string is a palindrome or not'''
    str2=input("Enter a string to checkk whether it's a palindrome or not:")
    f_string=str2[::]
    b_string=str2[::-1]
    if (f_string==b_string): # Determining a palindrome by string slicing
        print("It's a palindrome")
    else:
        print("Not a palindrome")
def Upper_Lower():
    '''Converting a string into uppercase and lowercase'''
    str3=input("Enter a string to convert into uppercase and lowercase:")
    Upper_str=str3.upper() # Converting into uppercase letters
    Lower_str=str3.lower() # Converting into lowercase letters
    print("Uppercased string:",Upper_str)
    print("Lowercased string:",Lower_str)
def MAIN():
    '''MENU DRIVEN PROGRAM'''
    while True:
        print("")
        print("1. To count no. of vowels and consonants in a string")
        print("2. To determine whether a string is a palindrome or not")
        print("3. To convert a string into uppercase and lowercase forms")
        print("4. Exit!!!")
        choice=int(input("Enter a choice from the menu:")) # Giving a choice to perform any of the functions
        if choice==1:
            Vowel_Consonant()
        elif choice==2:
            Palindrome()
        elif choice==3:
            Upper_Lower()
        elif choice==4:
            print("Exiting the Program!!!!!")
            break
        else:
            print("Invalid choice! Retype a number from the menu")
MAIN()