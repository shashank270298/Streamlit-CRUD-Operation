import sqlite3
import streamlit as st

# Connecting database

def get_connection():
    return sqlite3.connect("Students.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute( """
                CREATE TABLE IF NOT EXISTS students(
                    Roll_No INTEGER PRIMART KEY,
                    First_Name TEXT NOT NULL,
                    Last_Name TEXT,
                    Class INTEGER,
                    City TEXT
                )
                """
    )
    conn.commit()
    conn.close()
    
def insert_student(roll, fname, lname, clas, city):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
                    INSERT INTO students(Roll_No, First_Name, Last_Name, Class, City) VALUES (?,?,?,?,?)
                    """, (roll, fname, lname, clas, city)
        )
        conn.commit()
        st.success("✅ Student added successfully!")
    except sqlite3.IntegrityError:
        st.error("⚠ Roll number already exists!")
    conn.close()
    
def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return data

def update_student(roll, column, new_value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE students SET {column}=? WHERE Roll_no=?", (new_value, roll))
    conn.commit()
    if cur.rowcount>0:
        st.success("✅ Record updated successfully!")
    else:
        st.error("⚠ No record found!")
    conn.close()

def delete_student(roll):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE from students WHERE Roll_no = ?",(roll,))
    conn.commit()
    if cur.rowcount>0:
        st.success("🗑 Record deleted successfully!")
    else:
        st.error("⚠ No record found!")
    conn.close()
    
def main():
    st.set_page_config(page_title="Student CRUD App", page_icon="🗂", layout="wide")
    st.title("🗂 Student CRUD Operations (SQLite + Streamlit)")
    
    menu = ["Insert", "Read", "Update", "Delete"]
    choice = st.sidebar.radio("Select Operation",menu)
    
    init_db()
    
    if choice == "Insert":
        st.subheader("➕ Add Student Record")
        roll = st.number_input("Roll No", min_value=1)
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        clas = st.number_input("Class",min_value=1)
        city = st.text_input("City")
        if st.button("Add Student"):
            insert_student(roll, fname, lname, clas, city)
    
    elif choice=="Read":
        st.subheader("📄 View Student Records")
        data = view_students()
        if data:
            st.dataframe(data)
        else:
            st.warning("⚠ No records found!")
    
    elif choice=="Update":
        st.subheader("✏️ Update Student Record")
        roll = st.number_input("Enter Roll No", min_value=1)
        columns = ["First_Name", "Last_Name", "Class", "City"]
        column = st.selectbox("Select Column to Update", columns)
        new_value = st.text_input("Enter New Value")
        if st.button("Update"):
            update_student(roll, column, new_value)
        
    elif choice == "Delete":
        st.subheader("🗑 Delete Student Record")
        roll = st.number_input("Enter Roll No", min_value=1)
        if st.button("Delete"):
            delete_student(roll)
            
if __name__ == '__main__':
    main()