import os
import random

users = {
    "teacher@school.com": {
        "password": "teacher123",
        "role": "teacher",
        "name": "Prof. Matheus",
        "id": "",
    },
    "student@school.com": {
        "password": "student123",
        "role": "student",
        "name": "Matheus Dias",
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


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    clear()
    print("=" * 45)
    print("               ACADEMIC PORTAL               ")
    print("=" * 45)
    print("1. Sign In")
    print("2. Create Account / Change Password")
    print("=" * 45)
    choice = input("> ").strip()

    if choice == "2":
        clear()
        print("--- ACCOUNT MANAGEMENT ---")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()

        if not first_name or not last_name or not email or not password:
            print("\nError: All fields are required.")
            input("Press Enter to continue...")
            return None

        if password != confirm_password:
            print("\nError: Passwords do not match.")
            input("Press Enter to continue...")
            return None

        role = "student"

        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"

        existing_id = ""
        if email in users:
            existing_id = users[email].get("id", "")
        else:
            duplicate_user = next((u for u in users.values() if u["name"].lower() == full_name.lower()), None)
            if duplicate_user:
                existing_id = duplicate_user.get("id", "")

        if not existing_id:
            while True:
                existing_id = str(random.randint(100000, 999999))
                if not any(u.get("id") == existing_id for u in users.values()):
                    break

        users[email] = {
            "password": password,
            "role": role,
            "name": full_name,
            "id": existing_id,
        }

        print(f"\nAccount processed! Your PERMANENT ID (RA) is: {existing_id}")
        input("Press Enter to go to login...")
        return None

    clear()
    print("--- SIGN IN ---")
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    user = users.get(email)
    if user and user["password"] == password:
        return user

    print("\nWrong email or password.")
    input("Press Enter to try again...")
    return None


def student_menu(user):
    while True:
        clear()
        print(f"Student - {user['name']} | ID: {user['id']}")
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
                print(f"Name:    {record['name']}")
                print(f"ID (RA): {record['id']}")
                grades_str = ", ".join(f"{g:.1f}" for g in record["grades"])
                print(f"Grades:  {grades_str}")
                print(f"Average: {record['average']:.2f}")
                print(f"Status:  [{record['status'].upper()}]")
            else:
                print(f"Hello {user['name']}. Your grades have not been released by the teacher yet.")
            input("\nPress Enter to go back...")

        elif option == "2":
            break


def teacher_menu(user):
    while True:
        clear()
        print(f"Teacher - {user['name']}")
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

            student_user = next(
                (u for u in users.values() if u.get("id") == student_id), None
            )
            if not student_user:
                print("Error: Student ID not found in database.")
                input("Press Enter to go back...")
                continue

            grades = []
            for i in range(1, 4):
                while True:
                    try:
                        g = float(input(f"Grade {i}: "))
                    except ValueError:
                        print("Enter a number.")
                        continue
                    if 0 <= g <= 10:
                        grades.append(g)
                        break
                    print("Grade must be between 0 and 10.")

            avg = sum(grades) / 3
            status = (
                "Approved" if avg >= 7 else "Remedial" if avg >= 5 else "Failed"
            )

            global history
            history = [r for r in history if r["id"] != student_id]

            history.append(
                {
                    "id": student_id,
                    "name": student_user["name"],
                    "grades": grades,
                    "average": round(avg, 2),
                    "status": status,
                }
            )
            print("\nReport card updated successfully!")
            input("Press Enter to continue...")

        elif option == "2":
            clear()
            print(f"{'ID':<10}{'Student':<18}{'Avg':<8}Status")
            print("-" * 40)
            if not history:
                print("No records yet.")
            for r in history:
                print(
                    f"{r['id']:<10}{r['name']:<18}{r['average']:<8.2f}{r['status']}"
                )
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