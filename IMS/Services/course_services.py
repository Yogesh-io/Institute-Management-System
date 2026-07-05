from Database.db import *
from Services.student_services import *
from models.courses import courses
# Replace with your specific database engine error module if not using mysql-connector
from mysql.connector import Error as DBError

def add_course():
    conn = None
    cursor = None
    try:
        course_name = input("Enter course name: ")
        duration = input("Enter duration of course in months: ")
        fees = input("Enter fees: ")

        c = courses(course_name, duration, fees)

        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO courses(course_name,duration,fees) values(%s,%s,%s)"
        values = (c.course_name, c.duration, c.fees)

        cursor.execute(query, values)
        conn.commit()
        print("Course added")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def add_multiple_course():
    conn = None
    cursor = None
    try:
        while True:
            try:
                n = int(input("how many courses do you want to add: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        conn = get_connection()
        cursor = conn.cursor()
        for _ in range(1, n + 1):
            course_name = input("Enter course name: ")
            duration = input("Enter duration of course in months: ")
            fees = input("Enter fees: ")

            c = courses(course_name, duration, fees)

            query = "INSERT INTO courses(course_name,duration,fees) values(%s,%s,%s)"
            values = (c.course_name, c.duration, c.fees)

            cursor.execute(query, values)
            conn.commit()
        print("courses added")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def view_course():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * from courses")
        rows = cursor.fetchall()

        if not rows:
            print("No courses found in the database.")

        print("\n" + "="*75)
        print(f"| {'ID':<9} | {'Course Name':<25} | {'Duration':<15} | {'Fees':<12} |")
        print("="*75)
        for row in rows:
            
            course_id, course_name, duration, fees = row
            print(f"| {course_id:<9} | {course_name:<25} | {duration:<15} | {fees:<12} |")
        print("="*75)
            
            
    except DBError as e:
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def update_course():
    conn = None
    cursor = None
    try:
        course_id = int(input("Enter course id: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT course_name, duration, fees FROM courses WHERE course_id=%s", (course_id,))
        row = cursor.fetchone()

        if not row:
            print(f"No course found with ID: {course_id}")
            return 

        print(f"\nCurrent Details:\nName: {row[0]} | Duration: {row[1]} | Fees: {row[2]}\n")

        course_name = input("Enter New Course Name: ")
        duration = input("Enter New Course Duration (in Months): ")
        
        while True:
            try:
                fees_float = float(input("Enter New Fees: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid decimal number for fees.")

        query = "UPDATE courses SET course_name=%s, duration=%s, fees=%s WHERE course_id=%s"
        cursor.execute(query, (course_name, duration, fees_float, course_id))
        conn.commit()
        print("Details updated successfully!")

    except (ValueError, DBError) as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def delete_course():
    conn = None
    cursor = None
    try:
        while True:
            try:
                course_id = input("Enter course id: ")
                course_id = int(course_id)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM courses where course_id=%s"
        values = (course_id,)

        cursor.execute(query, values)
        conn.commit()
        print("Course Deleted Successfully!")
    except DBError as e:
        if conn: conn.rollback()
        print(f"Database Error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()