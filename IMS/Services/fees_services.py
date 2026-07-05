from Database.db import *
from models.fees import *
from mysql.connector import Error as DBError

# Add Fee Record
def add_fee_record():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id = int(input("Enter student Id: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        while True:
            try:
                total_fee = float(input("Enter Total Fees: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid amount.")

        while True:
            try:
                paid_amount = float(input("Enter Paid Amount: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid amount.")

        pending_amount = total_fee - paid_amount

        f = fees(student_id, total_fee, paid_amount, pending_amount)
        
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO fees (student_id, total_fee, paid_amount, pending_amount)
                   VALUES (%s, %s, %s, %s)"""
        values = (f.student_id, f.total_fee, f.paid_amount, f.pending_amount)
        
        cursor.execute(query, values)
        conn.commit()
        print("Fee Added..")
        
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# view Fees
def view_fees():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT students.student_id, student_name, total_fee, pending_amount FROM fees JOIN students ON fees.student_id=students.student_id;")
        rows = cursor.fetchall()
        
        if not rows:
            print("No fee records found.")
            return
        print("="*67)
        print(f"| {'Stud ID':<10} | {'Student Name':<20} | {'Total Fee':<12} | {'Pending':<12} |")
        print("="*67)   
        for row in rows:
            s_id, s_name, total_fee, pending = row
            print(f"| {s_id:<10} | {s_name:<20} | {total_fee:<12} | {pending:<12} |")
            
        print("="*67)
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Update fees
def update_fees():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id = int(input("Enter Student ID: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        while True:
            try:
                upaid_amount = float(input("Enter Updated Amount: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT total_fee, paid_amount, pending_amount FROM fees WHERE student_id=%s", (student_id,))
        row = cursor.fetchone()
        
        if row is None:
            print(f"No fee record found for Student ID {student_id}.")
            return
            
        paid_amount = upaid_amount + row[1]
        print("Total paid amount is ", paid_amount)
        pending_amount = row[0] - paid_amount
        print("Your Pending fee is ", pending_amount)

        cursor.execute("UPDATE fees SET paid_amount=%s, pending_amount=%s WHERE student_id=%s", (paid_amount, pending_amount, student_id))
        conn.commit()
        print("Data updated!")
        
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# search Fee
def search_fee():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id = int(input("Enter Student ID: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT students.student_id, students.student_name, fee_id, total_fee, paid_amount, pending_amount
                          FROM fees JOIN students ON students.student_id=fees.student_id WHERE fees.student_id=%s""", (student_id,))
        row = cursor.fetchone()
        
        if row is None:
            print(f"No fee details found for Student ID {student_id}.")
        else:
            print("="*95)
            print(f"| {'Stud ID':<10} | {'Student Name':<20} | {'Fee ID':<12} | {'Total Fee':<12} | {'Paid Amount':<12} | {'Pending Amount':<12} |")
            print("="*95)   

            student_id, student_name, fee_id, total_fee,paid_amount,pending_amount = row
            print(f"| {student_id:<10} | {student_name:<20} | {fee_id:<12} | {total_fee:<12} | {paid_amount:<12} | {pending_amount:<12}")
            print("="*95)
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# delete Fee
def delete_fee():
    conn = None
    cursor = None
    try:
        while True:
            try:
                fee_id = int(input("Enter Fee ID to Delete: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM fees WHERE fee_id=%s", (fee_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"No record found with Fee ID {fee_id}. Nothing deleted.")
        else:
            print("Fee Record Deleted Successfully....")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()