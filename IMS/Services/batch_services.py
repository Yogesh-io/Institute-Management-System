from Database.db import *
from models.batches import batches
from mysql.connector import Error as DBError

# add batch
def add_batch():
    conn = None
    cursor = None
    try:
        batch_name = input("enter batch name:")
        timing = input("enter batch timing( M for morning / E for evening): ")
        start_date = input("Enter batch start date(format:yyyy-mm-dd): ")
        
        while True:
            try:
                course_id = int(input("Enter course ID: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        while True:
            try:
                faculty_id = int(input("Enter Faculty ID: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        b = batches(batch_name, timing, start_date, course_id, faculty_id)

        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO batches(batch_name,timing,start_date,course_id,faculty_id) values(%s,%s,%s,%s,%s)"
        values = (b.batch_name, b.timing, b.start_date, b.course_id, b.faculty_id)

        cursor.execute(query, values)
        conn.commit()
        print("batch added")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# view batches
def view_batch():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * from batches")
        rows = cursor.fetchall()
        if not rows:
            print("Empty Batches List.")
        for row in rows:
            print(f"batch id: {row[0]} | batch name: {row[1]} | timing: {row[2]} | start date: {row[3]} | course id: {row[4]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# update batch details
def update_batch_details():
    conn = None
    cursor = None
    try:
        while True:
            try:
                batch_id = int(input("Enter batch id:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        batch_name = input("Enter new updated batch name:")
        timing = input("enter new timing:")
        course_id = input("New course id:")
        start_date = input("New start date for course:")
        
        while True:
            try:
                faculty_id = int(input("Enter Faculty Id: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid Number.")

        b = batches(batch_name, timing, start_date, course_id, faculty_id)

        conn = get_connection()
        cursor = conn.cursor()

        query = "UPDATE batches SET batch_name=%s, timing=%s, start_date=%s, course_id=%s, faculty_id=%s WHERE batch_id=%s"   
        value = (b.batch_name, b.timing, b.start_date, b.course_id, b.faculty_id, batch_id)

        cursor.execute(query, value)
        conn.commit()
        print("details updated!!!")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# delete batch
def delete_batch():
    conn = None
    cursor = None
    try:
        while True:
            try:
                batch_id = int(input("enter batch id: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM batches WHERE batch_id=%s"
        values = (batch_id,)

        cursor.execute(query, values)
        conn.commit()
        print("Batch Deleted!!!")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()