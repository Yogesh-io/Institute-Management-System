from Database.db import *
from models.faculty import faculty
# Replace with your specific database engine error module if not using mysql-connector
from mysql.connector import Error as DBError

# add faculty
def add_faculty():
    faculty_name=input("Enter Faculty Name:")
    mobile = input("Enter Mobile No:")
    email=input("Enter Email:")
    skill=input("Enter Skill:")
    joining_date=input("Enter Joining Date yyyy-mm-dd:")
    
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        f=faculty(faculty_name,mobile,email,skill,joining_date)
        query= "insert into faculty (faculty_name,mobile,email,skill,joining_date) values (%s,%s,%s,%s,%s)"
        values=(f.faculty_name,f.mobile,f.email,f.skill,f.joining_date)
        cursor.execute(query,values)
        conn.commit()
        print("Faculty Added Successfully.")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def search_faculty_id():
    conn = None
    cursor = None
    try:
        while True:
            try:
                faculty_id=int(input("Enter Faculty Id to Search:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        # cursor.execute("select * from faculty")
        # row=cursor.fetchall()
        # if not row:
        #     print("Faculty Not Found..!")
        #     cursor.close()
        #     conn.close()
        #     return
        
        cursor.execute("select * from faculty where faculty_id=%s",(faculty_id,))
        row=cursor.fetchone()
        faculty_id, faculty_name, mobile, email, skill, joining_date = row
        print("="*100)
        print(f"| {'faculty_id':<10} | {'faculty_name':<15} | {'mobile':<12} | {'email':<20} | {'skill':<12} | {'joining_date':<12} |")
        print("="*100)

        print(f"| {faculty_id:<10} | {faculty_name:<15} | {mobile:<12} | {email:<20} | {skill:<12} | {str(joining_date):<12} |")
        print("="*100)
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def search_faculty_name():
    conn = None
    cursor = None
    try:
        faculty_name=input("Enter Name to Search:")
        
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from faculty where faculty_name=%s",(faculty_name,))
        row=cursor.fetchone()
        if not row:
            print("Faculty Not Found....!")
        else:
            faculty_id, faculty_name, mobile, email, skill, joining_date = row
            print("="*100)
            print(f"| {'faculty_id':<10} | {'faculty_name':<15} | {'mobile':<12} | {'email':<20} | {'skill':<12} | {'joining_date':<12} |")
            print("="*100)

            print(f"| {faculty_id:<10} | {faculty_name:<15} | {mobile:<12} | {email:<20} | {skill:<12} | {str(joining_date):<12} |")
            print("="*100)
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def faculty_batches():
    conn = None
    cursor = None
    try:
        while True:
            try:
                faculty_id=int(input("Enter Faculty ID:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT batches.* FROM batches INNER JOIN faculty ON batches.faculty_id= faculty.faculty_id WHERE faculty.faculty_id = %s",(faculty_id,))
        row=cursor.fetchone()
        if not row:
            print("Batches not Found")
        else:
            batch_id,batch_name,timing,course_id,start_date,faculty_id=row
            print("=" * 76)
            print(f"| {'batch_id':<10} | {'batch_name':<15} | {'timing':<12} | {'course_id':<12} | {'start_date':<12} |")
            print("=" * 76)
            print(f"| {batch_id:<10} | {batch_name:<15} | {timing:<12} | {course_id:<12} | {str(start_date):<12} |")
            print("=" * 76)

    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def view_faculty():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("select * from faculty")
        rows= cursor.fetchall()
        
        print("="*100)
        print(f"| {'faculty_id':<10} | {'faculty_name':<15} | {'mobile':<12} | {'email':<20} | {'skill':<12} | {'joining_date':<12} |")
        print("="*100)

        for i in rows:
            faculty_id, faculty_name, mobile, email, skill, joining_date = i
            print(f"| {faculty_id:<10} | {faculty_name:<15} | {mobile:<12} | {email:<20} | {skill:<12} | {str(joining_date):<12} |")
        print("="*100)
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def update_faculty():
    conn = None
    cursor = None
    try:
        while True:
            try:
                faculty_id=int(input(("Enter Faculty ID to Update:")))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("Select * from faculty where faculty_id=%s",(faculty_id,))
        row=cursor.fetchone()

        if not row:
            print(f"{faculty_id} is not found")
            return

        faculty_name=input("Enter New Faculty Name:")
        mobile = input("Enter New Mobile Number:")
        email = input("Enter New Email ID:")
        skill = input("Enter New Skill:")
        joining_date = input("Enter New Joining-Date yyyy-mm-dd:")

        f=faculty(faculty_name,mobile,email,skill,joining_date)
        query="UPDATE faculty set faculty_name=%s,mobile=%s,email=%s,skill=%s,joining_date=%s where faculty_id=%s"
        values=(f.faculty_name,f.mobile,f.email,f.skill,f.joining_date,faculty_id)

        cursor.execute(query,values)
        conn.commit()
        print("Faculty Updated Successfully....")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def delete_faculty():
    conn = None
    cursor = None
    try:
        while True:
            try:
                faculty_id=int(input("Enter Faculty Id To Delete:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        query="DELETE from faculty where faculty_id=%s"
        values=(faculty_id,) 
        cursor.execute(query,values)
        conn.commit()
        print("Faculty Deleted Successfully.....")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()