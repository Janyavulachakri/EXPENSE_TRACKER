import csv
from datetime import date

expenses = []
next_id = 1


def save_expenses():
    with open("expenses.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id","date","category","amount"])

        for expense in expenses:
            writer.writerow([
                expense["id"],
                expense["date"],
                expense["category"],
                expense["amount"]
            ])

def load_expenses():
    global next_id 
    try:
            with open("expenses.csv","r",newline="") as file:
                reader = csv.reader(file)
                next(reader,None)

                for row in reader:
                   if not row:
                       continue

                   try:
                        expense = {
                            "id": int(row[0]),
                            "date": row[1],
                            "category": row[2],
                            "amount":int(row[3])
                       
                            }
                       
                        expenses.append(expense)
                       
                        if expense["id"] >= next_id:
                            next_id = expense["id"] + 1
                   except (ValueError,IndexError):
                       print("Warning: Skipping invalid expense record.")
                       
                   
    except FileNotFoundError:
        print("No expense file found. Starting with an empty tracker.")

            
            

def add_expense(category,amount):
    global next_id
    expense = {
        "id": next_id,
        "date": date.today().isoformat(),
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    next_id += 1
    


def view_expenses():
    print("="*60) 
    print("                  YOUR EXPENSES")
    print("="*60)

    if not expenses:
        print("                 No expenses found.")
    else:
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':>10}")
        print("-"*60)

    
        for expense in expenses:
            print(
                f"{expense['id']:<5}"
                f"{expense['date']:<15}"
                f"{expense['category']:<15}"
                f"{expense['amount']:>10}"

            )
    print("="*60)
    input("\nPress Enter to Continue...")


def get_total(category=None):
    if category:
        return sum(
            expense["amount"]
            for expense in expenses
            if expense["category"].lower() == category.lower()
        )

    return sum(expense["amount"] for expense in expenses)

def update_expense(expense_id,new_category,new_amount):
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["category"]= new_category
            expense["amount"] = new_amount
            print("Expense updated successfully")
            input("\nPress Enter to Continue...")
            return True
    print("Expense not found")
    input("\nPress Enter to continue...")
    return False

def delete_expense(expense_id):

    for expense in expenses:

        if expense["id"] == expense_id:

            print("\nExpense Found:")
            print(f"ID       : {expense['id']}")
            print(f"Date     : {expense['date']}")
            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']:,.2f}")

            while True:
                confirm = input(
                    "\nAre you sure you want to delete this expense? (y/n): "
                ).strip().lower()

                if confirm == "y":
                    expenses.remove(expense)

                    print("\n✅ Expense deleted successfully.")
                    input("\nPress Enter to Continue...")
                    return True

                elif confirm == "n":
                    print("\n❌ Delete cancelled.")
                    input("\nPress Enter to Continue...")
                    return False

                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")

    print("\n❌ Expense not found.")
    input("\nPress Enter to Continue...")
    return False
    
    

def main():
    load_expenses()
    while True:
        print("\n" + "=" * 40)
        print("          EXPENSE TRACKER")
        print("="*40)
        print()
        print("1. ADD EXPENSE")
        print("2. VIEW EXPENSES")
        print("3. TOTAL EXPENSES")
        print("4. UPDATE EXPENSES")
        print("5. DELETE EXPENSES")
        print("6. EXIT")
        print()
        print("="*40)
        choice = input("Choose an option")

        if choice == "1":
            while True:
                category = input("Enter category: ").strip().title()

                if not category:
                    print("Category cannot be empty.")
                    continue
                while True:
                    try:
                        amount = int(input("Enter amount: "))
                        if amount<=0:
                            print("Amount must be greater than 0.")
                            continue
                        add_expense(category,amount)
                        save_expenses()
                        print("Expense added successfully")
                        break
                    except ValueError:
                        print("Please enter a valid number.")




                more = input("Do you want to add another expense? (yes/no): ").strip().lower()
                if more!="yes" and more!="y":
                    break
                    
                
                

                
                
        
            

        elif choice == "2":
            view_expenses()


        elif choice == "3":
            print("=" * 40)
            print("     TOTAL EXPENSES")
            print("=" * 40)

            print(f"Overall Total: ₹{get_total():,.2f}")

            category = input(
                "\nEnter category for category total "
                "(or press Enter to skip): "
            ).strip()

            if category:
                print(f"{category} Total: ₹{get_total(category):,.2f}")

            print("=" * 40)
            input("\nPress Enter to Continue")


        elif choice == "4":
            while True:
                try:
                    expense_id = int(input("Enter expense ID: "))

                    if expense_id<=0:
                        print("Expense ID must be greater than 0.")
                        continue

                    new_amount = int(input("Enter new amount: "))
                    new_category = input("Enter new category: ").strip().title()

                    if new_amount<=0:
                        print("Amount must be greater than 0. ")
                        continue
                    if not new_category:
                        print("Category cannot be empty.")
                        continue

                    if update_expense(expense_id,new_category,new_amount):
                        save_expenses()
                    break
                except ValueError:
                    print("Please enter valid number.")

            
            
            


        elif choice == "5":
            while True:
                try:
                    expense_id = int(input("Enter expense ID: "))

                    if expense_id<=0:
                        print("Expense ID must be greater than 0.")
                        continue

                    if delete_expense(expense_id):
                        save_expenses()

                    break
                except ValueError:
                    print("Please enter a valid expense ID")
            

        elif choice == "6":
            print("\nThankyou for using Expense Tracker!")
            break

        else:
            print("Invalid option.Please choose between 1 and 6.")
            input("\nPress Enter to Continue")

    save_expenses()
if __name__ == "__main__":
    main()
