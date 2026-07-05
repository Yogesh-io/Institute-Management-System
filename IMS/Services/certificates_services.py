from Database.db import *
from models.certificates import *
from datetime import datetime
import random as r
from mysql.connector import Error as DBError

# add certificate
def generate_certificate():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id=int(input("Enter Student ID:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select pending_amount from fees where student_id=%s",(student_id,))
        criteria1=cursor.fetchone()
        cursor.close()

        if criteria1 is None:
            print(f"Error: No fee record found for Student ID {student_id}.")
            return

        cursor=conn.cursor()
        cursor.execute("select count(status) from attendance where status='Present' and student_id=%s",(student_id,))
        criteria2=cursor.fetchone()
        
        if criteria1[0]==0:
            print("Your All Fee is Completed.")
            if criteria2 and criteria2[0]>5:
                print("Your Attendance Critearia is Satisfied.")
                certificate_no=r.randint(0000,9999)
                issue_date=datetime.now()
                cursor.execute("insert into certificates(student_id,issue_date,certificate_no)values(%s,%s,%s)",(student_id,issue_date,certificate_no))
                conn.commit()
                print("Congratulation Your Certificate Generated Successfully.")
                print(f"Certificate Number : {certificate_no}")
            else:
                print("Your Attendance Critearia is NOT Satisfied.")
        else:
            print("Your Fee is Pending.")
            
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# View Certificates
def view_certificates():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("Select * from certificates")
        print(cursor.fetchall())
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Search Certificate
def search_certificate():
    conn = None
    cursor = None
    try:
        while True:
            try:
                certificate_no=int(input("Enter Certificate Number To Search:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from certificates where certificate_no=%s",(certificate_no,))
        print(cursor.fetchall())
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Verify Certificate Number
def verify_certificate():
    conn = None
    cursor = None
    try:
        while True:
            try:
                certificate_no=int(input("Enter Certificate Number To Verify(4 Digit No):"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select certificate_no from certificates")
        rows=cursor.fetchall()
        ct=0
        for i in rows:
            if certificate_no==int(i[0]):
                print("Certificate Number Verified Successfully.")
                ct+=1
                break
        if ct==0:print("Certificate Number is Not Found.")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Print Certificate
def print_certificate():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id=int(input("Enter Student ID:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        conn=get_connection()
        cursor=conn.cursor()
        query="""select s.student_name,s.student_id,c.course_name,cf.certificate_no,cf.issue_date from 
            students s join courses c on c.course_id=s.course_id
            join certificates cf on cf.student_id=s.student_id where cf.student_id=%s"""
        values=(student_id,)
        cursor.execute(query,values)
        row=cursor.fetchone()
        
        if row is None:
            print(f"No certificate data found for Student ID {student_id}.")
            return
            
        print(row)
        border = "=" * 70
        space = " " * 70
        
        print("\n" + border)
        print(f"|{'':^68}|")
        print(f"|{'*** INSTITUTION OF COMPUTER EXCELLENCE ***':^68}|")
        print(f"|{'':^68}|")
        print(f"|{'CERTIFICATE OF COMPLETION':^68}|")
        print(f"|{'-'*25:^68}|")
        print(f"|{'':^68}|")
        print(f"|{'This is proudly presented to':^68}|")
        print(f"|{'':^68}|")
        
        # Student Name
        print(f"|{row[0]:^68}|")
        print(f"|{'':^68}|")
        print(f"|{'for successfully completing the prescribed course of study in':^68}|")
        print(f"|{'':^68}|")
        
        # Course Name
        print(f"|{f' {row[2]} ':^68}|")
        print(f"|{'':^68}|")
        print(f"|{'':^68}|")
        
        # Certificate No and Date
        footer_text = f" Cert No: {row[3]} | Date: {row[4]} "
        print(f"|{footer_text:^68}|")
        print(f"|{'':^68}|")
        print(border + "\n")
        
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()