import os
import random
import re
import base64

users = {
    "teacher@school.com": {
        "password": base64.b64encode(b"teacher123").decode('utf-8'),
        "role": "teacher",
        "name": base64.b64encode(b"Prof. Matheus").decode('utf-8'),
        "id": "",
    },
    "student@school.com": {
        "password": base64.b64encode(b"student123").decode('utf-8'),
        "role": "student",
        "name": base64.b64encode(b"Matheus Dias").decode('utf-8'),
        "id": "123456",
    },
}

history = [
    {
        "id": "123456",
        "name": "Matheus Dias",
        "grades": [8.5, 7.5, 9.0],
        "average": 8.33,
        "status": "Approved",
    }
]

EMAIL_REGEX = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
NAME_REGEX = r"^[A-Za-zÀ-ÖØ-öø-ÿ]{2,}$"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    clear()
    print("=" * 45)
    print("               ACADEMIC PORTAL               ")
    print("=" * 45)
    print("1. Sign In")
    print("2. Create Student Account")
    print("=" * 45)
    choice = input("> ").strip()

    if choice == "2":
        clear()
        print("--- STUDENT REGISTRATION ---")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip().lower()
        password = input("Password (Min 6 chars): ").strip()
        confirm_password = input("Confirm Password: ").strip()

        if not first_name or not last_name or not email or not password:
            print("\nValidation Error: All fields are required.")
            input("Press Enter to continue...")
            return None

        if not re.match(NAME_REGEX, first_name) or not re.match(NAME_REGEX, last_name):
            print("\nSecurity Error: Names must contain only letters and be at least 2 chars long.")
            input("Press Enter to continue...")
            return None

        if not re.match(EMAIL_REGEX, email):
            print("\nSecurity Error: Invalid email format. Use: user@domain.com")
            input("Press Enter to continue...")
            return None

        if len(password) < 6:
            print("\nSecurity Error: Password must be at least 6 characters long.")
            input("Press Enter to continue...")
            return None

        if password != confirm_password:
            print("\nValidation Error: Passwords do not match.")
            input("Press Enter to continue...")
            return None

        if email in users and users[email]["role"] == "teacher":
            print("\nConflict Error: This email belongs to an institutional Teacher account.")
            input("Press Enter to continue...")
            return None

        full_name = first_name.capitalize() + " " + last_name.capitalize()

        existing_id = ""
        if email in users:
            existing_id = users[email].get("id", "")
        else:
            duplicate = next((u for u in users.values() if base64.b64decode(u["name"].encode('utf-8')).decode('utf-8').lower() == full_name.lower()), None)
            if duplicate:
                existing_id = duplicate.get("id", "")

        if not existing_id:
            while True:
                existing_id = str(random.randint(100000, 999999))
                if not any(u.get("id") == existing_id for u in users.values()):
                    break

        users[email] = {
            "password": base64.b64encode(password.encode('utf-8')).decode('utf-8'),
            "role": "student",
            "name": base64.b64encode(full_name.encode('utf-8')).decode('utf-8'),
            "id": existing_id,
        }

        print("\nAccount processed! Your PERMANENT ID (RA) is: " + existing_id)
        input("Press Enter to go to login...")
        return None

    clear()
    print("--- SIGN IN ---")
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    user = users.get(email)
    if user and base64.b64decode(user["password"].encode('utf-8')).decode('utf-8') == password:
        return user

    print("\nWrong email or password.")
    input("Press Enter to try again...")
    return None


def student_menu(user):
    while True:
        clear()
        real_name = base64.b64decode(user['name'].encode('utf-8')).decode('utf-8')
        print("Student - " + real_name + " | ID: " + user['id'])
        print("=" * 45)
        print("1. View My Report Card")
        print("2. Logout")
        print("=" * 45)
        option = input("> ").strip()

        if option == "1":
            clear()
            print("--- OFFICIAL ACADEMIC REPORT ---")
            record = next((r for r in history if r["id"] == user["id"]), None)

            if record:
                print("Name:    " + record['name'])
                print("ID (RA): " + record['id'])
                grades_str = ", ".join("{:.1f}".format(g) for g in record["grades"])
                print("Grades:  " + grades_str)
                print("Average: {:.2f}".format(record['average']))
                print("Status:  [" + record['status'].upper() + "]")
            else:
                print("Hello " + real_name + ". Your grades have not been released by the teacher yet.")
            input("\nPress Enter to go back...")

        elif option == "2":
            break


def teacher_menu(user):
    while True:
        clear()
        real_name = base64.b64decode(user['name'].encode('utf-8')).decode('utf-8')
        print("Teacher - " + real_name)
        print("=" * 45)
        print("1. Enter Student Grades (By ID)")
        print("2. View Grade History")
        print("3. Logout")
        print("=" * 45)
        option = input("> ").strip()

        if option == "1":
            clear()
            print("--- LAUNCH STUDENT GRADES ---")
            student_id = input("Enter Student ID (RA): ").strip()

            student_user = next((u for u in users.values() if u.get("id") == student_id), None)
            if not student_user:
                print("\nError: Student ID not found in database.")
                input("Press Enter to go back...")
                continue

            grades = []
            for i in range(1, 4):
                while True:
                    try:
                        g = float(input("Grade " + str(i) + ": "))
                    except ValueError:
                        print("Enter a valid number.")
                        continue
                    if 0 <= g <= 10:
                        grades.append(g)
                        break
                    print("Grade must be between 0 and 10.")

            avg = sum(grades) / 3
            status = "Approved" if avg >= 7 else "Remedial" if avg >= 5 else "Failed"

            global history
            history = [r for r in history if r["id"] != student_id]

            student_real_name = base64.b64decode(student_user["name"].encode('utf-8')).decode('utf-8')
            history.append({
                "id": student_id,
                "name": student_real_name,
                "grades": grades,
                "average": round(avg, 2),
                "status": status,
            })
            print("\nReport card updated successfully!")
            input("Press Enter to continue...")

        elif option == "2":
            clear()
            print("{:<10}{:<18}{:<8}Status".format("ID", "Student", "Avg"))
            print("-" * 40)
            if not history:
                print("No records yet.")
            for r in history:
                print("{:<10}{:<18}{:<8.2f}{}".format(r['id'], r['name'], r['average'], r['status']))
            input("\nPress Enter to go back...")

        elif option == "3":
            break


while True:
    user = login()
    if user is None:
        continue
    if user["role"] == "teacher":
        teacher_menu(user)
    else:
        student_menu(user)