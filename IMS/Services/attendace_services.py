from Database.db import *
from models.attendance import *
from mysql.connector import Error as DBError

def mark_attendeace():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id=int(input("Enter Student Id:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        while True:
            try:
                batch_id=int(input("Enter Batch Id:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        attendance_date=input("Enter Attendence Date:")
        status=input("Absent/Present:")

        a=attendance(student_id,batch_id,attendance_date,status)
        
        conn=get_connection()
        cursor=conn.cursor()
        query="insert into attendance(student_id,batch_id,attendance_date,status) values(%s,%s,%s,%s)"
        values=(student_id,batch_id,attendance_date,status)
        cursor.execute(query,values)
        conn.commit()
        print(f"Attendance Marked Successfully for Student ID:{student_id}")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# view Attendance
def view_attendance():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""select attendance.* from attendance 
                    join students on students.student_id=attendance.student_id
                    join batches on batches.batch_id=attendance.batch_id""")
        
        print("==============================================================")
        print("|attendence_id  student_id  batch_id  attendance_date  status|\n==============================================================")
        rows=cursor.fetchall()
        for i in rows:
            print(f" {i[0]}             |{i[1]}          |{i[2]}        |{i[3]}      |{i[4]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#view Presents Only
def view_present():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("""select attendance.* from attendance 
                    join students on students.student_id=attendance.student_id
                    join batches on batches.batch_id=attendance.batch_id where attendance.status='Present'""")
        
        rows=cursor.fetchall()
        if not rows:
            print("Present Students Are Not Found!")
        else:
            count=len(rows)
            print(f"Presents Students Are:{count}")
            print("==============================================================")
            print("|attendence_id  student_id  batch_id  attendance_date  status|\n==============================================================")
            # rows=cursor2.fetchall()
            for i in rows:
                print(f" {i[0]}             |{i[1]}          |{i[2]}        |{i[3]}      |{i[4]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#view absents Only
def view_absent():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("""select attendance.* from attendance 
                    join students on students.student_id=attendance.student_id
                    join batches on batches.batch_id=attendance.batch_id where attendance.status='Absent'""")
        
        rows=cursor.fetchall()
        if not rows:
            print("Absent Students Are Not Found!")
        else:
            count=len(rows)
            print(f"Absent Students Are:{count}")
            print("==============================================================")
            print("|attendence_id  student_id  batch_id  attendance_date  status|\n==============================================================")
            # rows=cursor2.fetchall()
            for i in rows:
                print(f" {i[0]}             |{i[1]}          |{i[2]}        |{i[3]}      |{i[4]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def search_attendence_id():
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
        cursor.execute("select students.student_name,attendance.attendance_date,attendance.status from attendance join students on students.student_id=attendance.student_id where attendance.student_id=%s",(student_id,))
        rows=cursor.fetchall()
        for i in rows:
            print(f"{i[0]} {i[1]} {i[2]}")
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#update
def update_attendance():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id=int(input("Enter Student ID to Update Attendence:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        attendance_date=input("Enter Date(yyyy-mm-dd):")
        status=input("Enter Attendance Status To Update(Present/Absent):")
        
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("update attendance set status=%s where student_id=%s AND attendance_date=%s",(status,student_id,attendance_date))
        conn.commit()
        print(f"Attendance Updated For Student ID:{student_id}")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#delete
def delete_attendance():
    conn = None
    cursor = None
    try:
        while True:
            try:
                student_id=int(input("Enter Student ID to Delete Attendence:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        attendance_date=input("Enter Date(yyyy-mm-dd):")
        
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("Delete from attendance where student_id=%s AND attendance_date=%s",(student_id,attendance_date))
        conn.commit()
        print("Attendance Deleted Successfully.")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()