from Services.student_services import *
from Services.course_services import *
from Services.batch_services import *
from Services.faculty_services import *
from Services.fees_services import *
from Services.fee_transaction_services import *
from Services.attendace_services import *
from Services.followups_services import *
from Services.certificates_services import *

def admin_panel():
    while True:
        print("\n================ Admin Panel ================")
        print("1. Course\n2. Batch\n3. Faculty\n4. Student\n5. Attendance\n6. Fees\n7. Fees Transactions\n8. Followups\n9. Certificates\n10. Logout")
        print("=============================================")
        
        # Secured Main Panel input
        try:
            main_choice = int(input("Enter Choice: "))
        except ValueError:
            print("\n[Error] Invalid input! Please enter a number between 1 and 10.")
            continue

        match main_choice:
            # Course Module
            case 1:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add single course\n2. Add multiple courses\n3. View courses\n4. Update courses\n5. Delete a course\n6. Exit\nEnter choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_course()
                        case 2: add_multiple_course()
                        case 3: view_course()
                        case 4: update_course()
                        case 5: delete_course()
                        case 6:
                            print("Exiting Course Section......")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 6.")

            # Batch Module
            case 2:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add batch\n2. View batches\n3. Update batches\n4. Delete batches\n5. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_batch()
                        case 2: view_batch()
                        case 3: update_batch_details()
                        case 4: delete_batch()
                        case 5:
                            print("Exiting Batch Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 5.")

            # Faculty Module
            case 3:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add Faculty\n2. View All Faculty\n3. Update Faculty\n4. Search Faculty\n5. Delete Faculty\n6. View Faculty Batches\n7. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_faculty()
                        case 2: view_faculty()
                        case 3: update_faculty()
                        case 4:
                            print("\n1. Search Faculty By ID\n2. Search Faculty By Name")
                            try:
                                ch = int(input("Enter Your Choice: "))
                                if ch == 1: search_faculty_id()
                                elif ch == 2: search_faculty_name()
                                else: print("[Error] Invalid choice selected.")
                            except ValueError:
                                print("\n[Error] Invalid input! Please enter numbers only.")
                        case 5: delete_faculty()
                        case 6: faculty_batches()
                        case 7:
                            print("Exiting From Faculty Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 7.")    

            # Student Module
            case 4:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add student\n2. Update student\n3. Delete student\n4. Search student\n5. Show all students\n6. Change Batch\n7. View Student All Details\n8. Exit\nEnter choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_students()
                        case 2: update_student()
                        case 3: delete_student()
                        case 4: search_student()
                        case 5: view_students()
                        case 6: change_batch()
                        case 7: details()
                        case 8:
                            print("Exiting Student Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 8.")

            # Attendance Module
            case 5:
                while True:
                    try:
                        sub_choice = int(input("\n1. Mark Attendance\n2. View Attendance\n3. Search Attendance\n4. Update Attendance\n5. Delete Attendance\n6. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: mark_attendeace()
                        case 2:
                            print("\n1. View All Student Attendance\n2. View Present Students\n3. View Absent Students\n4. Exit")
                            try:
                                ch = int(input("Enter Your Choice: "))
                                if ch == 1: view_attendance()
                                elif ch == 2: view_present()
                                elif ch == 3: view_absent()
                                elif ch == 4: continue
                                else: print("[Error] Invalid Choice selected.")
                            except ValueError:
                                print("\n[Error] Invalid input! Please enter numbers only.")
                        case 3: search_attendence_id()
                        case 4: update_attendance()
                        case 5: delete_attendance()
                        case 6:
                            print("Exiting Attendance Section.....")
                            break
                        case _: print("[Error] Invalid option!")

            # Fees
            case 6:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add Fees\n2. View Fees\n3. Update Fees\n4. Search Student Fees\n5. Delete Fees\n6. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_fee_record()
                        case 2: view_fees()
                        case 3: update_fees()
                        case 4: search_fee()  
                        case 5: delete_fee()  
                        case 6:
                            print("Exiting Fees Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 6.")

            # Fees Transactions
            case 7:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add Fee Transaction\n2. View Fee Transaction\n3. Update Fee Transaction\n4. Search Fee Transaction\n5. Delete Fee Transaction\n6. Exit\nEnter Your Choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_transaction() 
                        case 2: view_transaction() 
                        case 3: update_transaction() 
                        case 4: search_transaction() 
                        case 5: delete_transaction() 
                        case 6:
                            print("Exiting Fees Transaction Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 6.")

            # Followup
            case 8:
                while True:
                    try:
                        sub_choice = int(input("\n1. Add Followup\n2. View Followup\n3. Update Followup\n4. Search Followup\n5. Delete Followup\n6. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: add_followup()
                        case 2: view_followup()
                        case 3: update_followup()
                        case 4: search_followup()
                        case 5: delete_followup()
                        case 6:
                            print("Exiting Followup Section.....")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 6.")

            # Certificates
            case 9:
                while True:
                    try:
                        sub_choice = int(input("\n1. Generate certificate\n2. View Certificates\n3. Search Certificate\n4. Verify Certificate Number\n5. Print Certificate\n6. Exit\nEnter your choice: "))
                    except ValueError:
                        print("\n[Error] Invalid input! Please enter a number.")
                        continue

                    match sub_choice:
                        case 1: generate_certificate()
                        case 2: view_certificates()
                        case 3: search_certificate()
                        case 4: verify_certificate()
                        case 5: print_certificate()
                        case 6:
                            print("Exiting Certificate Section.....\n")
                            break
                        case _: print("[Error] Invalid option! Choose a number between 1 and 6.")
           
            case 10:
                print("Logging out cleanly...")
                break # Safely exits the admin panel loop instead of cutting execution via exit()
            
            case _:
                print("\n[Error] Selection out of bounds! Choose a number between 1 and 10.")