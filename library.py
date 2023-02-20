import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amalthomas",
    database="library"
)
cursor = mydb.cursor()
def add_book():
    title=input("Enter the Title of the book: ")
    author=input("Enter the name of the author: ")
    published_year=input("Enter the year of publication: ")
    sql = "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)"
    val = (title, author, published_year)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "book inserted")

def delete_book():
    book_id=int(input("Enter the id of the book to delete:"))
    sql = "DELETE FROM books WHERE id = %s"
    val = (book_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "book deleted")

def add_member():
    name=input("Enter the name of the member : ")
    email=input("Enter the mail id of the member: ")
    phone=input("Enter phone number: ")
    sql = "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)"
    val = (name, email, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "member inserted")

def delete_member():
    member_id=input("Enter the id of the member: ")
    sql = "DELETE FROM members WHERE id = %s"
    val = (member_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "member deleted")

def loan_book():
    book_id=input("Enter the id of the book to borrow: ")
    member_id=input("Enter the id of the member :")
    start_date=input("Enter the start date: ")
    due_date=input("Enter the due date: ") 
    sql = "INSERT INTO loans (book_id, member_id, start_date, due_date) VALUES (%s, %s, %s, %s)"
    val = (book_id, member_id, start_date, due_date)
    cursor.execute(sql, val)
    mydb.commit()
    sql="UPDATE books SET available=available-1 WHERE id=%s"
    val=(book_id,)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount, "book loaned")

def return_book():
    book_id=input("Enter the book ID")
    sql = "UPDATE loans SET returned = TRUE WHERE id = %s AND returned = FALSE"
    val = (book_id,)
    cursor.execute(sql, val)
    mydb.commit()
    sql="UPDATE books SET available=available+1 WHERE id=%s"
    val=(book_id,)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount, "book returned")

def list_books():
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def list_members():
    sql = "SELECT * FROM members"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def list_loans():
    sql = "SELECT loans.id, books.title, members.name, loans.start_date, loans.due_date, loans.returned FROM loans JOIN books ON loans.book_id = books.id JOIN members ON loans.member_id = members.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)


while True:

    print("Menu:")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Add Member")
    print("4. Delete Member")
    print("5. Borrow Book")
    print("6. Retrun Book")
    print("7. List Members")
    print("8. List Borrow")
    print("9. List Books")
    print("10. Exit")


    choice = input("Enter your choice: ")


    if choice == "1":
        print("You selected Add Book ")
        add_book()
        
    elif choice == "2":
        print("You selected Delete Book")
        delete_book()
        
    elif choice == "3":
        print("You selected Add Member")
        add_member()
        
    elif choice == "4":
        print("You selected Delete Member")
        delete_member()
        
    elif choice == "5":
        print("You selected Borrow Book")
        loan_book()
        
    elif choice == "6":
        print("You selected Return Book")
        return_book()
        
    elif choice == "7":
        print("You selected List Members")
        list_members()
        
    elif choice == "8":
        print("You Selected List Borrow")
        list_loans()
        
    elif choice == "9":
        print("You selected List Books")
        list_books()
        
    else:
        print("Exit")
        break

