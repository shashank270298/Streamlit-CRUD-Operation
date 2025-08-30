from database import get_connection
from tabulate import tabulate

def create_table():
    from database import init_db
    init_db()
    print("✅ Table is ready!")
    
def insert_records(n):
    with get_connection() as conn:
        cur = conn.cursor()
        for i in range(n):
            try:
                roll = int(input("Enter Roll No: "))
                fname = input("Enter Your First Name: ")
                lname = input("Enter Your Last Name: ")
                clas = int(input("Enter Class: "))
                city = input("Enter city: ")
                
                cur.execute("""
                            INSERT INTO students(Roll_no, First_Name, Last_Name, Class, City)
                            VALUES(?,?,?,?,?)
                            """, (roll, fname, lname, clas, city))
                conn.commit()
                print(f"✅ Record {i+1} inserted successfully!")
            except Exception as e:
                print(f"❌ Error inserting record: {e}")

def read_records():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=["Roll No", "First_Name", "Last_name", "Class", "City"], tablefmt="fancy_grid"))
        else:
            print("⚠ No records found!")

def update_record():
    with get_connection() as conn:
        cur = conn.cursor()
        roll = int(input("Enter Roll No to update: "))
        print("Choose column to update: ")
        print("1. First Name\n2. Last Name\n3. Class\n4. City")
        choice = input("Enter your choice: ")
        
        columns = {"1": "First_Name", "2": "Last_Name", "3": "Class", "4": "City"}
        if choice not in columns:
            print("⚠ Invalid choice!")
            return
        
        new_value = input(f"Enter new {columns[choice]}: ")
        cur.execute(f"UPDATE students SET {columns[choice]} = ? WHERE Roll_no = ?", (new_value, roll))
        conn.commit()
        
        if cur.rowcount>0:
            print("✅ Record updated successfully!")
        else:
            print("⚠ No record found with that Roll No.")
            
def delete_record():
    with get_connection() as conn:
        cur = conn.cursor()
        choice = choice = input("Press W to delete whole table or R to delete a specific record: ").upper()
        
        if choice == "W":
            cur.execute("DROP TABLE IF EXISTS students")
            conn.commit()
            print("🗑 Table deleted successfully!")
        elif choice=="R":
            roll = int(input("Enter Roll no to delete: "))
            cur.execute("DELETE FROM students WHERE Roll_no = ?",(roll,))
            conn.commit()
            if cur.rowcount>0:
                print("✅ Record deleted successfully!")
            else:
                print("⚠ No record found with that Roll No.")
        else:
            print("⚠ Invalid choice!")
            