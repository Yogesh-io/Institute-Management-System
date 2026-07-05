from Services.faculty_services import *
from Services.student_services import *
from Services.attendace_services import *
from Services.batch_services import *

def faculty_panel():
    while True:
        print("\n================ Faculty Panel ================")
        try:
            choice = int(input("1. View Students\n2. Mark Attendance\n3. View Attendance\n4. View Batch\n5. Logout\nEnter Choice: "))
        except ValueError:
            print("\n[Error] Invalid Input! Please enter a number between 1 and 5.")
            continue 

        match choice:
            case 1:
                try:
                    view_students()
                except Exception as e:
                    print(f"\n[Error] Failed to load students: {e}")
            case 2:
                try:
                    mark_attendeace()
                except Exception as e:
                    print(f"\n[Error] Failed to mark attendance: {e}")
            case 3:
                try:
                    view_attendance()
                except Exception as e:
                    print(f"\n[Error] Failed to load attendance: {e}")
            case 4:
                try:
                    faculty_batches()
                except Exception as e:
                    print(f"\n[Error] Failed to load batches: {e}")
            case 5:
                print("\nLogging out cleanly from Faculty Panel...")
                break 
            case _:
                print("\n[Invalid Choice] Please select an option between 1 and 5.")