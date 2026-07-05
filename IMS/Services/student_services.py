# functions
from Database.db import *
from models.student import student
from models.batches import batches
from mysql.connector import Error as DBError 


# Add student 
def add_students():
    conn = None
    cursor = None
    try:
        student_name = input("Enter Student Name: ")
        mobile = input("Enter Student Mobile No: ")
        email = input("Enter Student Email: ")
        address = input("Enter Student Address: ")
        admission_date = input("Enter Admission date (yyyy-mm-dd): ")
        batch_id = int(input("Enter Batch ID: "))
        course_id = int(input("Enter Course ID: "))
        
        s = student(student_name, mobile, email, address, admission_date, batch_id, course_id)
        
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO students (student_name, mobile, email, address, admission_date, batch_id, course_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (s.student_name, s.mobile, s.email, s.address, s.admission_date, s.batch_id, s.course_id)
        
        cursor.execute(query, values)
        conn.commit()
        print("Student Added Successfully!")
        
    except DBError as e:
        if conn:
            conn.rollback()  
        print(f"Database Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# view 
def view_students():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        
        if not rows:
            print("No records found in the students table.")
            return

        header_format = "| {:<10} | {:<14} | {:<13} | {:<16} | {:<8} | {:<14} | {:<9} | {:<8} |"
        
        print("=" * 115)
        print(header_format.format("student_id", "student_name", "mobile", "email", "address", "adm_date", "course_id", "batch_id"))
        print("=" * 115)
        
        for row in rows:
            print(header_format.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])))
        
        print("=" * 115)
        
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# search 
def search_student():
    conn = None
    cursor = None
    try:
        sid = int(input(("Enter Student ID to Search: ")))
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id=%s", (sid,))
        row = cursor.fetchone()
        
        if row is None:
            print(f"No student found with ID: {sid}")
            return

        header_format = "| {:<10} | {:<14} | {:<13} | {:<16} | {:<8} | {:<14} | {:<9} | {:<8} |"
          
        print("=" * 115)
        print(header_format.format("student_id", "student_name", "mobile", "email", "address", "adm_date", "course_id", "batch_id"))
        print("=" * 115)
        print(header_format.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])))
        print("=" * 115)
          
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
  
def delete_student():
    conn = None
    cursor = None
    try:
        sid = int(input(("Enter Student ID to Delete Student: ")))
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM students WHERE student_id=%s"
        values = (sid,)
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"No student found with ID {sid}. Nothing deleted.")
        else:
            print(f"Student with ID {sid} Deleted Successfully.")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def update_student():
    conn = None
    cursor = None
    try:
        sid = int(input(("Enter Student Id to Update: ")))
        student_name = input("Enter New Student Name: ")
        mobile = input("Enter New Student Mobile: ")
        email = input("Enter Student New Email: ")
        address = input("Enter Student New Address: ")
        admission_date = input("Enter Student New Admission Date: ")
        batch_id = int(input(("Enter Student New Batch ID: ")))
        course_id = int(input(("Enter Student New Course ID: ")))

        s = student(student_name, mobile, email, address, admission_date, batch_id, course_id)
        
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """UPDATE students SET 
                   student_name=%s, mobile=%s, email=%s, address=%s, admission_date=%s, batch_id=%s, course_id=%s 
                   WHERE student_id=%s"""
        values = (s.student_name, s.mobile, s.email, s.address, s.admission_date, s.batch_id, s.course_id, sid)
        
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"No student found with ID {sid}. Update skipped.")
        else:
            print("Student Updated Successfully.")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def change_batch():
    conn = None
    cursor = None
    try:
        student_id = int(input(("Enter Student ID: ")))
        batch_id = int(input(("Enter Batch ID to Change: ")))
        
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "UPDATE students SET batch_id=%s WHERE student_id=%s"
        values = (batch_id, student_id)
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"No student found with ID {student_id}. No batch changed.")
        else:
            print(f"Student with ID {student_id} updated to Batch {batch_id} successfully.")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def details():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM students 
                          INNER JOIN batches ON students.batch_id=batches.batch_id 
                          INNER JOIN courses ON batches.course_id=courses.course_id""")
        rows = cursor.fetchall()
        
        if not rows:
            print("No joint details found.")
            return
            
        for row in rows:
            print(row)
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()