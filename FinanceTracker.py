transactions = []
balance = 0.0

print("Welcome to Your Simple Money Tracker!")

while True:
    print("\nWhat do you want to do today?")
    print("1. Add some money ")
    print("3. Check how much money you have")
    print("4. Look at past records")
    print("5. Exit the app")

    choice = input("Type a number (1-5): ")

    if choice == "1":
        amount = float(input("How much money did you get? $"))
        balance += amount
        transactions.append({"type": "Income", "amount": amount})
        print("Ur money is added!")

    elif choice == "2":
        amount = float(input("How much did you spend? $"))
        balance -= amount
        transactions.append({"type": "Expense", "amount": amount})
        print(" Expense saved!")

    elif choice == "3":
        print(f"\nYou currently have: ${balance:.2f}")

    elif choice == "4":
        print("\n Here’s your list of transactions:")
        if not transactions:
            print("No records yet.")
        else:
            for i, t in enumerate(transactions, 1):
                print(f"{i}. {t['type']} - ${t['amount']:.2f}")

    elif choice == "5":
        print(" Bye!")
        break

    else:
        print(" Please enter a number between 1 and 5.")
