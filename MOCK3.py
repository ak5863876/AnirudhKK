def MAX_min():
    list1=[10,39,52,7,4,33,22,57,63,86]
    max_num=max(list1)
    min_num=min(list1)
    print("Maximum number from list:",max_num)
    print("Minimum number from list:",min_num)
def Sum():
    list2=[23,3,41,5,56,74,19,98]
    Sum=0
    for num in list2[::]:
        Sum=Sum+num
    print("Sum of numbers in list:",Sum)
def Average():
    list3=[1,45,32,6,59,78,93,13]
    SUM=0
    l=len(list3)
    for num in list3[::]:
        SUM=SUM+num
        Avg=SUM/l
    print("Average of numbers from list:",Avg)
def Even_Odd():
    list4=[45,66,87,34,76,23,51,90]
    even=0
    odd=0
    for num in list4[::]:
        if num%2==0:
            even += 1
        else:
            odd += 1
    print("Even numbers from list:",even)
    print("Odd numbers from list:",odd)
def MAIN():
    while True:
        print("=====MENU=====")
        print("1. Maximum and Minimum numbers from list")
        print("2. Sum of numbers from list")
        print("3. Average of numbers from list")
        print("4. Number of Even and Odd from list")
        print("5. Exit!!")
        choice=int(input("Enter choice from menu:"))
        if choice==1:
            MAX_min()
        elif choice==2:
            Sum()
        elif choice==3:
            Average()
        elif choice==4:
            Even_Odd()
        elif choice==5:
            print("Exiting the Program!!!!!")
            break
        else:
            print("Invalid choice! Retype a number from the menu")
MAIN()