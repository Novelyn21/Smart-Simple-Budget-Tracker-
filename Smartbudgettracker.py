while True:
    try:
        user_input = input("Please enter your monthly budget: ")
        if ":\\" in user_input or "python" in user_input.lower():
            continue
        monthly_budget = float(user_input)
        break
    except ValueError:
        print("Invalid input! Please type a number only.")

remaining_balance = monthly_budget
expenses = []

while True: 
    print("--------Simple Monthly Budget--------") 
    print("1. Add Expenses") 
    print("2. See Summary") 
    print("3. Exit") 
    print("-------------------------------------") 
    
    choice = input("Enter your choice: ") 
    
    if choice == "1": 
        category = input("Category's name [example: Rent, bills, fare]: ") 
        
        while True:
            try:
                cost_input = input("Enter the cost: ")
                cost = float(cost_input)
                break
            except ValueError:
                print("Invalid price! Please enter a number.")
        
        if cost > remaining_balance:
            print(f"WARNING: This expense exceeds your remaining budget of ₱{remaining_balance:.2f}!")
            proceed = input("Do you still want to add this expense? (yes/no): ").strip().lower()
            if proceed != 'yes':
                print("Expense cancelled.")
                continue  
        
        remaining_balance -= cost 
        new_expense = {"category": category, "cost": cost} 
        expenses.append(new_expense) 
        
        print("Expense added successfully!") 
        print(f"Added ₱{cost:.2f} to {category}.") 
        print(f"Remaining Budget: ₱{remaining_balance:.2f}") 
        
        spent = monthly_budget - remaining_balance 
        if spent >= monthly_budget * 0.5 and remaining_balance >= 0: 
            print("Warning: You've used 50% or more of your monthly budget!") 
            
    elif choice == "2": 
        print("-------------Summary--------------") 
        total_expense = sum(item['cost'] for item in expenses) 
        
        if not expenses: 
            print("No expenses recorded!") 
        else:
            category_totals = {}
            for item in expenses:
                cat = item['category']
                category_totals[cat] = category_totals.get(cat, 0) + item['cost']

            for item in expenses: 
                print(f"- {item['category']}: ₱{item['cost']:.2f}") 
            print("-------------------------------------")
            
            most_expensive_category, most_expensive_cost = max(category_totals.items(), key=lambda x: x[1])
            print(f"Most Expensive Category: {most_expensive_category} (₱{most_expensive_cost:.2f})")
            print(f"Total Spent: ₱{total_expense:.2f}")
            print(f"Remaining Balance: ₱{remaining_balance:.2f}") 
            
    elif choice == "3": 
        print("Thanks! Exiting...") 
        break 
        
    else: 
        print("Invalid choice. Please enter 1, 2, or 3.")
