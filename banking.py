# Basic Banking Software

data = {"virat": 1234, "hardik": 1111, "rahul": 0000, "rohit": 1212}
data2 = {"virat": 9865, "hardik": 6464, "rahul": 1656, "rohit": 4532}

id = input("Enter ID: ")
pswd = int(input("Enter Password: "))
print("\n")

if id in data and pswd == data[id]:
    print("Welcome", id, "!")
    while True:
        print("How may we help you?")
        print("1. Balance Check")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        print("\n")
        
        if choice == 1:
            print("Current balance is:", data2[id])
        elif choice == 2:
            dep = int(input("Enter amount to deposit: "))
            key = int(input("Enter password again: "))
            if key == pswd:
                data2[id] += dep
                print("Transaction Successful!")
                print("Updated balance:", data2[id])
            else:
                print("Wrong password")
        elif choice == 3:
            wed = int(input("Enter amount to withdraw: "))
            key = int(input("Enter password again: "))
            if key == pswd and wed <= data2[id]:
                data2[id] -= wed
                print("Transaction Successful!")
                print("Updated balance:", data2[id])
            else:
                print("Transaction Failed! Either incorrect password or insufficient balance.")
        elif choice == 4:
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Try again.")
        print("\n")
else:
    print("Invalid credentials. Access denied.")
