## short intro
## Author: Menlam Choden
## Date created: 20 Sept 2022
## Date last changed: 04 Sept 2022
## This program will calculate the product by Russian Peasant method
## learning constants, functions, loops, conditional structure

DIVISOR = 2


def main():
    print("Welcome to Russian Peasant App\n")
    printMenu()


def printMenu():
    print("Please make a choice")
    print("A) Calculate Product Using Peasant Method")
    print("B) Print The Help Table")
    print("C) Exit the APP")
    choice = input()

    if choice == 'A' or choice == 'a':
        tryMultiply = 1
       
        while tryMultiply != 0:
            print("We will use Peasant method to calculate the product\n")
            print("Please give first integer")
           
            ifirstInt = int(input())
            print("Please give second integer")
            isecondInt = int(input())
            print("The product of given integers is","=",calculateProduct(ifirstInt,isecondInt))
            print("Do you want to do another multiplication? Y or N")
            option = input()
            if option == 'Y' or option == 'y':
                tryMultiply = 1
            elif option == 'N' or option == 'n':
                tryMultiply = 0
        printMenu()
    
    elif choice == 'B' or choice == 'b':
        printHelpTable()
    
    elif choice == 'C' or choice == 'c':
        exitApp()
    
    else:
        print("Invalid choice,exiting app")



def calculateProduct(ifirstInt,isecondInt):
    product = 0
    while isecondInt!= 0:
      
        if isecondInt % DIVISOR!=0:
            product = product + ifirstInt
            ifirstInt = int(ifirstInt * DIVISOR)
            isecondInt = int(isecondInt / DIVISOR)
        else:
            ifirstInt = ifirstInt * DIVISOR
            isecondInt = isecondInt / DIVISOR

    return(product)
    

 
def printHelpTable():
    help_tbl = {
        1 : [34,19,'add A to the product, B is odd'],
        2 : [68,9, 'add A to the product, B is odd'],
        3 : [136,4,'ignore this A value, B is even'],
        4 : [272,2,'ignore this A value, B is even'],
        5 : [544,1,'add A to the product, B is odd'],
         }
    print("{:<8} | {:<15} | {:<10}".format('A','B','Comments'))
    print("-------------------------------------------------")
    for k,v in help_tbl.items():
        a,b,c = v
        print("{:<8} | {:<15} | {:<10}".format(a,b,c))
    print("Sum up all the A values that had odd B values and you get: 34+68+544 = 646 => Final product.\n")
        
    printMenu()

def exitApp():
    print("You are exiting the program")
    

main()
