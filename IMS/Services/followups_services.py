from models.followups import *
from Database.db import *
from mysql.connector import Error as DBError

# Add followup
def add_followup():
    conn = None
    cursor = None
    try:
        student_id = int(input(("Enter Student ID: ")))
        followup_date = input("Enter Followup Date(yyyy-mm-dd): ")
        reason = input("Enter Reason: ")
        next_followup = input("Enter Next Followup Date(yyyy-mm-dd): ")
        remarks = input("Enter Remark: ")

        f = followups(student_id, followup_date, reason, next_followup, remarks)
        
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO followups (student_id, followup_date, reason, next_followup, remarks) VALUES (%s, %s, %s, %s, %s)"
        values = (f.student_id, f.followup_date, f.reason, f.next_followup, f.remarks)
        
        cursor.execute(query, values)
        conn.commit()
        print("Follow Up Added...")
        
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# View
def view_followup():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM followups")
        rows = cursor.fetchall()
        
        if not rows:
            print("No followup records found.")
            return

        print("="*115)
        print(f"| {'Follow ID':<10} | {'Stud ID':<10} | {'Follow Date':<12} | {'Reason':<25} | {'Next Date':<12} | {'Remarks':<25} |")
        print("="*115)  
        for i in rows:
            followup_id, student_id, followup_date, reason, next_followup, remarks = i
            print(f"| {followup_id:<10} | {student_id:<10} | {str(followup_date):<12} | {reason:<25} | {str(next_followup):<12} | {remarks:<25} |")
        
        print("="*115)
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Update
def update_followup():
    conn = None
    cursor = None
    try:
        student_id = int(input(("Enter Student ID to Update Followup: ")))
        followup_date = input("Enter Followup Date(yyyy-mm-dd) to update: ")
        reason = input("Enter Reason to update: ")
        next_followup = input("Enter Next Followup Date(yyyy-mm-dd) to update: ")
        remarks = input("Enter updated Remark: ")

        f = followups(student_id, followup_date, reason, next_followup, remarks)
        
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """UPDATE followups SET 
                   followup_date=%s, reason=%s, next_followup=%s, remarks=%s 
                   WHERE student_id=%s"""
        values = (f.followup_date, f.reason, f.next_followup, f.remarks, f.student_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"No followup records found for Student ID {student_id}. Update skipped.")
        else:
            print("Follow Up Updated...")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Search
def search_followup():
    conn = None
    cursor = None
    try:
        student_id = int(input("Enter Student ID to Search Followup: "))
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM followups WHERE student_id=%s", (student_id,))
        rows = cursor.fetchall()
        
        if not rows:
            print(f"No followup records found for Student ID {student_id}.")
            return
        print("="*115)
        print(f"| {'Follow ID':<10} | {'Stud ID':<10} | {'Follow Date':<12} | {'Reason':<25} | {'Next Date':<12} | {'Remarks':<25} |")
        print("="*115) 
        for i in rows:
            followup_id, student_id, followup_date, reason, next_followup, remarks = i
            print(f"| {followup_id:<10} | {student_id:<10} | {str(followup_date):<12} | {reason:<25} | {str(next_followup):<12} | {remarks:<25} |")
        
        print("="*115)
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Delete
def delete_followup():
    conn = None
    cursor = None
    try:
        student_id = int(input(("Enter Student ID to Delete Followups: ")))

        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM followups WHERE student_id=%s"
        values = (student_id,)

        cursor.execute(query, values)
        conn.commit()
        print("Followup Deleted Successfully.")
        
        if cursor.rowcount == 0:
            print(f"No followup records found for Student ID {student_id}. Nothing deleted.")
        else:
            print("Follow up records deleted successfully.")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()