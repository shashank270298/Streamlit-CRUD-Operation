import sqlite3

DB_NAME = "Students.db"
print("Database created successfully!!!!!")

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
                    CREATE  TABLE IF NOT EXISTS students(
                        Roll_no INTEGER PRIMARY KEY,
                        First_Name TEXT NOT NULL,
                        Last_Name TEXT,
                        CLass INTEGER,
                        City TEXT
                        )
                """)
        print("Table created successfully!!!!!")
        conn.commit()