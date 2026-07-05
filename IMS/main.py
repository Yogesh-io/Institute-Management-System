from Services.users_services import *

while True:
    try:
        print("\n" + "="*35)
        print("         MAIN MENU")
        print("="*35)
        choice = int(input("1. Management Portal\n2. Student Portal\n3. Exit\nEnter Choice: "))
    except ValueError:
        print("\n[Error] Invalid input! Please enter numbers only.")
        continue  

    match choice:
        case 1:
            while True:
                try:
                    print("\n" + "="*15 + " Management Portal " + "="*15)
                    ch = int(input("1. Login\n2. Add Management User (Register)\n3. Back to Main Menu\nEnter Choice: "))
                    
                    if ch == 1:
                        mgt_login()
                    elif ch == 2:
                        add_mgt_user()
                    elif ch == 3:
                        print("Going back to Main Menu...")
                        break
                    else:
                        print("[Invalid] Please select a valid option (1, 2, or 3).")
                except ValueError:
                    print("\n[Error] Please enter numbers only.")
                except Exception as e:
                    print(f"\n[Management Error] Something went wrong: {e}")
                
        case 2:
            while True:
                try:
                    print("\n" + "="*17 + " Student Portal " + "="*17)
                    ch = int(input("1. Login\n2. Register New Student\n3. Back to Main Menu\nEnter Choice: "))
                    
                    if ch == 1:
                        student_login() 
                    elif ch == 2:
                        add_stud_user()
                    elif ch == 3:
                        print("Going back to Main Menu...")
                        break
                    else:
                        print("[Invalid] Please select a valid option (1, 2, or 3).")
                except ValueError:
                    print("\n[Error] Please enter numbers only.")
                except Exception as e:
                    print(f"\n[Student Error] Something went wrong: {e}")
                    
        case 3:
            print("\nExiting the application. Thank you!")
            break  
            
        case _:
            print("\n[Invalid Choice] Please select a valid option (1, 2, or 3).")