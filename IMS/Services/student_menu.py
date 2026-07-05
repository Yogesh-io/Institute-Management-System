from Database.db import get_connection
from Services.batch_services import *
# from Services.users_services import *


def student_panel(student_id):
    while True:
        print("\n================ Student Portal ================")
        print("1.View Batch\n2.View Attendance\n3.View Fees\n4.Logout")
        print("=============================================")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("\n[Error] Invalid input! Please enter a number between 1 and 10.")
            continue
        match choice:
            case 1:view_student_batch(student_id)
            case 2:view_attendance(student_id)
            case 3:view_student_fees(student_id)
            case 4:
                print("Exiting Student Portal......")
                break
            case _: print("[Error] Invalid option! Choose a number between 1 and 4.")
    

def view_student_batch(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT batches.* from batches join students on students.batch_id = batches.batch_id where students.student_id=%s",(student_id,))
        row = cursor.fetchone()
        if not row:
            print("Batch Not Assigned For Student ID:{student_id}")
            return
        print("\n" + "="*80)
        print(f"{'Batch ID':<10} | {'Batch Name':<20} | {'Timing':<12} | {'Start Date':<12} | {'Course ID':<10}")
        print("="*80)
        print(f"{row[0]:<10} | {row[1]:<20} | {row[2]:<12} | {str(row[3]):<12} | {row[4]:<10}")
        print("="*80)
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def view_attendance(student_id):
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""select attendance.* from attendance 
                    join students on students.student_id=attendance.student_id
                    join batches on batches.batch_id=attendance.batch_id where students.student_id=%s""",(student_id,))
        
        print("====================================================")
        print("|student_id  batch_id  attendance_date  status|\n=====================================================")
        rows=cursor.fetchall()
        for i in rows:
            print(f" {i[1]}             |{i[2]}          |{i[3]}        |{i[4]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def view_student_fees(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT students.student_id, student_name, total_fee, pending_amount FROM fees JOIN students ON fees.student_id=students.student_id where students.student_id=%s",(student_id,))
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
