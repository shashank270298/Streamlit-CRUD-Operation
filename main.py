from crud import create_table, insert_records, read_records, update_record, delete_record

def menu():
    while True:
        print("\n========== STUDENT CRUD MENU ==========")
        print("1. Create Table")
        print("2. Insert Records")
        print("3. View Records")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        print("=======================================")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_table()
        elif choice == "2":
            n = int(input("How many records you want to insert? : "))
            insert_records(n)
        elif choice == "3":
            read_records()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please try again.")
        
if __name__ == "__main__":
    menu()