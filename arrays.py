from array import *
x = 0
while(True):
        print(" 0. Exit \n 1. Input elements \n 2. Search the value \n 3. Remove the value \n 4. Sort the array")
        print("Enter your choice:")
        i= int(input())
        

        if i== 1:
            total = int(input("enter the total number of elements in array"))
            a=0
            val_2 = 0
            for a in range(total):
                val_2 = int(input('Enter the number'))
                if a == 0 and x==0:
                    x=1
                    val_1= array('i',[val_2])
                else:
                    val_1.append(val_2)
            print(val_1)


        if i==2 :
            x = int(input("enter the number you want to search"))
            if x in val_1:
                print("yes " ,x, " is present in the list")
                        
            else:
                print("no ",x, " is present in the list") 
                    
              
        if i== 3:
            n = int(input("enter the number to delete"))
            if n in val_1:
                val_1.remove(n)
            print( n,"deleted")
            print(val_1)


        if i== 4 :
            print("sorted list: " ,sorted(val_1))



        if i == 0:
            break
         