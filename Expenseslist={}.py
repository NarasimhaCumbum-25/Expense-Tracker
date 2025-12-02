Expenseslist={}
print ("Welcome to Your Expense Tracker!")

while True:
    print("======== MENU =======")
    print("1.Add Expense")
    print("2.veiw all Expenses")
    print("3.calculate the amount spent")
    print("4.EXIT")
    
    choice=int(input("Enter your choice:")) 
    
    # add expense:
    
    if(choice==1):
        date=input("Enter date:")
        category=input("Enter category of item:")
        description=input("Enter more details of item:")
        amount=input("Enter the price:")
        
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        print("Expense is added successfully")
        
        # view all expenses
        
    elif(choice==2):
        if(expense==0):
            print("No expense til now")
        else:
            print("your expenses are here")
            count=1
            for eachexpense in Expenseslist:
                print(f"expense number {count}-> {eachexpense['date']},{eachexpense['category']},{eachexpense['description']},{eachexpense['amount']}")
                count+=1
                
                
    #calculate all expenses
    elif(choice==3):
        total=0
        for eachexpense in Expenseslist:
            total=total+ expense["amount"]
        print("This is total expense",total)
        
        #Exit
    elif(choice==4):
        print("thanks for use")
        break
    else:
        print("Invalid choice")    
                            
