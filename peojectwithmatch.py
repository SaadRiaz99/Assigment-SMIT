stud = []

def signup():
    print("\n---- Signup ----")
    E_mail = input("Enter Your Email: ")

    for i in stud:
        if i[0] == E_mail:
            print("Username already exists. Try another.")
            return

    password = input("Create Password: ")
    name = input("Enter Full Name: ")
    roll_no = input("Enter Roll Number: ")

    print("\nEnter Marks :")
    print("\nEnter Marks:")

    while True:
        eng = int(input("English Number out of 100: "))
        math = int(input("Math Number out of 100: "))
        isl = int(input("Islamiat Number out of 75: "))
        urdu = int(input("Urdu Number out of 100: "))

        if eng > 100 and math > 100 and isl > 75 and urdu > 100:
            print("Invalid Number! Please enter again.\n")
                         
        else:
            break

    print("Successfully Entered Your Marks ")

    student_data = [E_mail, password, name, roll_no, eng, math, isl, urdu]
    stud.append(student_data)
    print("\nSignup successful! Now login to see your marksheet.")


def login():
    print("\n--- LOGIN ---")
    username = input("Enter Email: ")
    password = input("Enter Password: ")

    for i in stud:
        if i[0] == username and i[1] == password:
            print(f"\nWelcome {i[2]}!")
            show_marksheet(i)
            return
    print("Invalid username or password.")


def show_marksheet(i):
    print("\n======= MARKSHEET =======")
    print(f"Name    : {i[2]}")
    print(f"Roll No : {i[3]}")
    print("--------------------------")
    print(f"English : {i[4]}")
    print(f"Math    : {i[5]}")
    print(f"Islamiat: {i[6]}")
    print(f"Urdu    : {i[7]}")
    print("--------------------------")

    total = i[4] + i[5] + i[6] + i[7]
    percent = total / 4
    print(f"Total Marks: {total}/375")
    print(f"Percentage : {percent:.2f}%")

    
    if percent >= 80:
        grade = "A+"
    elif percent >= 70:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 50:
        grade = "C"
    else:
        grade = "Fail"

   
    if grade == "Fail":
        result = "Fail - Try Again!"
    else:
        result = "Pass - Congratulations!"

    print(f"Grade  : {grade}")
    print(f"Result : {result}")
    print("==========================")


def update_student():
    email = input("Enter Email to Update: ")
    for i in stud:
        if i[0] == email:
            print("Record Found!")
            i[2] = input("New Name: ") or i[2]
            i[3] = input("New Roll No: ") or i[3]
            i[4] = int(input("New English Marks: ") or i[4])
            i[5] = int(input("New Math Marks: ") or i[5])
            i[6] = int(input("New Islamiat Marks: ") or i[6])
            i[7] = int(input("New Urdu Marks: ") or i[7])
            print("Record Updated Successfully!")
            return
    print("Student not found!")


def delete_student():
    email = input("Enter Email to Delete: ")
    for i in stud:
        if i[0] == email:
            stud.remove(i)
            print("Student deleted successfully!")
            return
    print("No such student found.")


def show_total_students():
    print(f"\nTotal Students Registered: {len(stud)}")


def show_all_students():
    if len(stud) == 0:
        print("\nNo students registered yet.")
        return

    print("\n===== ALL STUDENTS LIST =====")
    for idx, i in enumerate(stud, start=1):
        print(f"{idx}. Name: {i[2]} | Roll No: {i[3]} | Email: {i[0]}")
    print("=============================")
def show_name_by_roll():
    roll = input("Enter Roll Number: ")

    for i in stud:
        if i[3] == roll:
            print(f"Student Name: {i[2]}")
            return
    print("No student found with this Roll Number.")



while True:
    print("\n===== STUDENT PORTAL =====")
    print("1. Sign Up")
    print("2. Login")
    print("3. Total Students")
    print("4. Show All Students")
    print("5. Update Student Data")
    print("6. Delete Student Data")
    print("7. Search By Roll-No")
    print("8. Exit")

    ch = input("Choose an option: ")

    if ch == "1":
        signup()
    elif ch == "2":
        login()
    elif ch == "3":
        show_total_students()
    elif ch == "4":
        show_all_students()
    elif ch == "5":
        update_student()
    elif ch == "6":
        delete_student()
    elif ch == "7":
        show_name_by_roll()   
    elif ch == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
