from Database.db import *
from models.users import *
from Services.admin_menu import *
from Services.faculty_menu import *
from Services.receptionist_menu import *
from Services.student_menu import *

def add_mgt_user():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        role = input("Enter role (admin/faculty/receptionist): ").strip().lower()
        
        if role not in ['admin', 'faculty', 'receptionist']:
            print("[Error] Invalid role assigned! Use admin, faculty, or receptionist.")
            return

        u = users(username, password, role)
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        values = (u.username, u.password, u.role)
        
        cursor.execute(query, values)
        conn.commit()
        print("\n>>> User added successfully! <<<")
        
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"\n[Database Error] Failed to add user: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def mgt_login():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        username = input("Enter Your Username: ").strip()
        password = input("Enter Your Password: ").strip()
        role = input("Enter Your Role (admin/faculty/receptionist): ").strip().lower()
        
        query = "SELECT username, password, role FROM users WHERE username = %s AND password = %s AND LOWER(role) = %s"
        cursor.execute(query, (username, password, role))
        user_record = cursor.fetchone() 
        
        if user_record:
            print(f"\n>>> Login success! Welcome {username} <<<")
            
            if role == "admin":
                admin_panel()
            elif role == "faculty":
                faculty_panel()
            elif role == "receptionist":
                receptionist_panel()
        else:
            print("\n[Access Denied] Invalid credentials! Please try again.")
            
    except Exception as e:
        print(f"\n[System Error] Login sequence interrupted: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def student_login():
    conn=None
    cursor=None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        username=input("Enter User Name:").strip()
        password=input("Enter Password:").strip()
        student_id =int(input("Enter Student ID:"))

        query = "SELECT username, password, student_id FROM student_login WHERE username = %s AND password=%s and student_id=%s"
        cursor.execute(query, (username, password, student_id))
        user_record = cursor.fetchone()
        
        if user_record:
            print(f">> Login Successfull, Welcome {username} <<")
            student_panel(student_id)
        else:
            print("\n[Access Denied] Invalid credentials! Please try again.")
        
    except ValueError:
        print("[Error] Enter Valid Input.")
    

def add_stud_user():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        username = input("Set Username: ").strip()
        password = input("Set Password: ").strip()
        student_id =int(input("Enter Student ID:"))


        u = stu_users(username, password,student_id)
        query = "INSERT INTO student_login(username, password,student_id) VALUES (%s, %s, %s)"
        values = (u.username, u.password, u.student_id)
        
        cursor.execute(query, values)
        conn.commit()
        print("\n>>> User added successfully! <<<")
        
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"\n[Database Error] Failed to add user: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()