from Services.student_services import *
from Services.course_services import *
from Services.batch_services import *
from Services.faculty_services import *
from Services.followups_services import *
from Services.fees_services import *
from Services.fee_transaction_services import *

def receptionist_panel():
    while True:
        print("\n================ Receptionist Panel ================")
        try:
            main_choice = int(input("1. Student Admission\n2. FollowUp\n3. Fees Collection\n4. Search Student\n5. Logout\nEnter Choice: "))
        except ValueError:
            print("\n[Error] Invalid Input! Please enter a number between 1 and 5.")
            continue

        try:
            match main_choice:
                # Student Admission Module
                case 1:
                    while True:
                        print("\n============== Student Admission ================")
                        try:
                            sub_choice = int(input("1. Add student\n2. Update student\n3. Delete student\n4. Show all students\n5. Change Batch\n6. View Student All Details\n7. Exit\nEnter choice: "))
                        except ValueError:
                            print("\n[Error] Invalid input! Please enter a number.\n")
                            continue

                        match sub_choice:
                            case 1: add_students()
                            case 2: update_student()
                            case 3: delete_student()
                            case 4: view_students()
                            case 5: change_batch()
                            case 6: details()
                            case 7:
                                print("Exiting Student Admission Module.....")
                                break
                            case _: 
                                print("[Error] Invalid selection. Please enter a number between 1 and 7.\n")    

                # Followups Module
                case 2:
                    while True:
                        print("\n================== Followups ==================\n")
                        try:
                            sub_choice = int(input("1. Add Followup\n2. View Followup\n3. Update Followup\n4. Search Followup\n5. Delete Followup\n6. Exit\nEnter your choice: "))
                        except ValueError:
                            print("\n[Error] Invalid input! Please enter a number.\n")
                            continue

                        match sub_choice:
                            case 1: add_followup()
                            case 2: view_followup()
                            case 3: update_followup()
                            case 4: search_followup()
                            case 5: delete_followup()
                            case 6:
                                print("Exiting Followup Module....")
                                break   
                            case _:
                                print("[Error] Invalid selection. Please enter a number between 1 and 6.\n")

                # Fees Collection Module
                case 3:
                    while True:
                        print("\n===================== Fees Collection ===================\n")
                        try:
                            sub_choice = int(input("1. Fee\n2. Fee Transactions\n3. Back to Main Menu\nEnter Choice: "))
                        except ValueError:
                            print("\n[Error] Invalid input! Please enter a number.\n")
                            continue  

                        match sub_choice:
                            case 1:
                                while True:
                                    try:
                                        nested_choice = int(input("\n1. Add Fees\n2. View Fees\n3. Update Fees\n4. Search Student Fees\n5. Delete Fees\n6. Exit\nEnter your choice: "))
                                    except ValueError:
                                        print("\n[Error] Invalid input! Please enter a number.\n")
                                        continue

                                    match nested_choice:
                                        case 1: add_fee_record()
                                        case 2: view_fees()
                                        case 3: update_fees()
                                        case 4: search_fee()
                                        case 5: delete_fee()
                                        case 6:
                                            print("Exiting Fees Module....")
                                            break
                                        case _:
                                            print("[Error] Invalid selection. Please enter a number between 1 and 6.\n")

                            case 2:
                                while True:
                                    try:
                                        nested_choice = int(input("\n1. Add Fee Transaction\n2. View Fee Transaction\n3. Update Fee Transaction\n4. Search Fee Transaction\n5. Delete Fee Transaction\n6. Exit\nEnter your choice: "))
                                    except ValueError:
                                        print("\n[Error] Invalid input! Please enter a number.\n")
                                        continue

                                    match nested_choice:
                                        case 1: add_transaction()
                                        case 2: view_transaction()
                                        case 3: update_transaction()
                                        case 4: search_transaction()
                                        case 5: delete_transaction()
                                        case 6:
                                            print("Exiting Fees Transaction Module....")
                                            break 
                                        case _:
                                            print("[Error] Invalid selection. Please enter a number between 1 and 6.\n")
                            case 3:
                                break
                            case _:
                                print("[Error] Invalid selection. Please enter a number between 1 and 3.\n")
                
                # Search Student Directly
                case 4:
                    search_student()
                
                # Logout
                case 5:
                    print("\nLogged Out Safely From Receptionist Panel.")
                    break
                    
                case _:
                    print("\n[Error] Invalid Input! Please choose a number from 1 to 5.")

        except Exception as runtime_error:
            print(f"\n[Error] An operation failed: {runtime_error}")
            print("Returning safely to the panel main menu.")