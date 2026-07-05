from Database.db import *
from models.fee_transaction import fee_transaction
from mysql.connector import Error as DBError

#add 
def add_transaction():
  conn = None
  cursor = None
  try:
    while True:
        try:
            fee_id=int(input("Enter Fee ID:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    while True:
        try:
            amount=int(input("Enter Amount:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    payment_date=input("Enter date(yyyy-mm-dd):")
    mode=input("Enter mode (Cash/UPI/Card/Bank Transfer):")

    ft=fee_transaction(fee_id,amount,payment_date,mode)
    
    conn=get_connection()
    cursor=conn.cursor()
    query="insert into fee_transactions(fee_id,amount,payment_date,mode)values(%s,%s,%s,%s)"
    values=(ft.fee_id,ft.amount,ft.payment_date,ft.mode)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    print("transaction details added!")
    
    #also updating fee table
    cursor=conn.cursor()
    cursor.execute("select total_fee,paid_amount,pending_amount from fees where fee_id=%s",(fee_id,))
    rows=cursor.fetchone()
    
    if rows is None:
        print(f"Error: fee_id {fee_id} not found in fees table. Cannot update balances.")
        return
        
    paid_amount=rows[1]+amount
    pending_amount=rows[0]-paid_amount

    query="update fees set paid_amount=%s, pending_amount=%s where fee_id=%s"
    values=(paid_amount,pending_amount,fee_id)
    cursor.execute(query,values)
    conn.commit()
    
  except DBError as e:
    if conn: conn.rollback()
    print(f"Database Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    if cursor: cursor.close()
    if conn: conn.close()

# view Fees Transaction
def view_transaction():
  conn = None
  cursor = None
  try:
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from fee_transactions")
    print("==============================================================")
    print("|transaction_id  fee_id  amount  payment_date  mode|\n==============================================================")
    rows=cursor.fetchall()
    for i in rows:
        print(f" {i[0]}             |{i[1]}          |{i[2]}        |{i[3]}      |{i[4]}")
  except DBError as e:
    print(f"Database Error: {e}")
  finally:
    if cursor: cursor.close()
    if conn: conn.close()


# update Fees Transaction
def update_transaction():
  conn = None
  cursor = None
  try:
    while True:
        try:
            transaction_id=int(input("Enter Transaction ID to Update:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    while True:
        try:
            amount=int(input("Enter Amount to Update:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    payment_date=input("Enter Date(yyyy-mm-dd):")
    mode=input("Enter Mode (Cash/UPI/Card/Bank Transfer):")

    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select fee_id from fee_transactions")
    
    fetchone_res = cursor.fetchone()
    if fetchone_res is None:
        print("Error: No records found in fee_transactions.")
        return
        
    fee_id=fetchone_res[0]
    cursor.close()
    
    cursor=conn.cursor()
    cursor.execute("update fee_transactions set amount=%s,payment_date=%s,mode=%s where transaction_id=%s",(amount,payment_date,mode,transaction_id))
    conn.commit()
    cursor.close()
    
    cursor=conn.cursor()
    cursor.execute("Select paid_amount,pending_amount from fees where fee_id=%s",(fee_id,))
    rows=cursor.fetchone()
    
    if rows is None:
        print(f"Error: fee_id {fee_id} not found in fees table.")
        return
        
    paid_amount=rows[1]+amount
    pending_amount=rows[0]-paid_amount
    query="""update fees set paid_amount=%s,pending_amount=%s where fee_id=%s"""
    values=(paid_amount,pending_amount,fee_id)
    cursor.execute(query,values)
    
  except DBError as e:
    if conn: conn.rollback()
    print(f"Database Error: {e}")
  finally:
    if cursor: cursor.close()
    if conn: conn.close()

  
# search Fees Transaction
def search_transaction():
  conn = None
  cursor = None
  try:
    while True:
        try:
            transaction_id=int(input("Enter Transaction Id to Search:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from fee_transaction where transaction_id=%s",(transaction_id,))
    row=cursor.fetchone()
    t_id, student_id, amount, mode, t_date = row

    print("="*78)
    print(f"| {'Trans ID':<10} | {'Student ID':<10} | {'Amount':<10} | {'Mode':<12} | {'Date':<15} |")
    print("="*78)
    print(f"| {t_id:<10} | {student_id:<10} | {amount:<10} | {mode:<12} | {str(t_date):<15} |")
    print("="*78)
  except DBError as e:
    print(f"Database Error: {e}")
  finally:
    if cursor: cursor.close()
    if conn: conn.close()
  
# delete Fees Transaction
def delete_transaction():
  conn = None
  cursor = None
  try:
    while True:
        try:
            transaction_id=int(input("Enter Transaction Id to Delete:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select amount from fee_transactions where transaction_id=%s",(transaction_id,))
    amount=cursor.fetchone()
    if amount is None:
        print(f"Error: Transaction ID {transaction_id} not found.")
        return
        
    cursor.close()
    cursor=conn.cursor()
    cursor.execute("select fees.paid_amount,fees.pending_amount from fees join fee_transactions on fee_transactions.fee_id=fees.fee_id where fee_transactions.transaction_id=%s",(transaction_id,))
    row=cursor.fetchone()
    if row is None:
        print("Error: Linked fee balance profile details could not be found.")
        return
        
    paid_amount=row[0]-amount[0]
    pending_amount=row[1]+amount[0]
    cursor.close()
    
    cursor=conn.cursor()
    cursor.execute("delete from fee_transactions where transaction_id=%s",(transaction_id,))
    cursor.close()
    
    cursor=conn.cursor()
    cursor.execute("update fees set paid_amount=%s, pending_amount=%s",(paid_amount,pending_amount))
    cursor.close()
    conn.commit()
    print(f"Transaction Id {transaction_id} Deleted Successfully.")
  except DBError as e:
    if conn: conn.rollback()
    print(f"Database Error: {e}")
  finally:
    if cursor: cursor.close()
    if conn: conn.close()