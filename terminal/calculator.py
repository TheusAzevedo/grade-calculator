import os
import random

users = {
    "teacher": {"password": "teacher123", "role": "teacher", "name": "Prof. Matheus", "id": ""},
    "student": {"password": "student123", "role": "student", "name": "Matheus Dias", "id": "123456"},
}

history = [
    {"id": "123456", "name": "Matheus Dias", "grades": [8.5, 7.5, 9.0], "average": 8.33, "status": "Approved"},
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    clear()
    print("Academic Portal")
    print("-" * 30)
    print("1. Sign in")
    print("2. Register")
    choice = input("> ").strip()

    if choice == "2":
        clear()
        username = input("Username: ").strip().lower()
        if username in users:
            print("That username is taken.")
            input("Press Enter to continue...")
            return None
        password = input("Password: ").strip()
        name = input("Full name: ").strip()

        student_id = str(random.randint(100000, 999999))
        while any(u["id"] == student_id for u in users.values()):
            student_id = str(random.randint(100000, 999999))

        users[username] = {"password": password, "role": "student", "name": name, "id": student_id}
        print(f"\nSaved. Your student ID is {student_id}. Write it down.")
        input("Press Enter to continue...")
        return None

    clear()
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    user = users.get(username)
    if user and user["password"] == password:
        return user

    print("Wrong username or password.")
    input("Press Enter to try again...")
    return None


def student_menu(user):
    while True:
        clear()
        print(f"Student - {user['name']} ({user['id']})")
        print("1. My grades")
        print("2. Logout")
        option = input("> ").strip()

        if option == "1":
            clear()
            record = next((r for r in history if r["id"] == user["id"]), None)

            if record:
                grades = ", ".join(f"{g:.1f}" for g in record["grades"])
                print(f"Name: {record['name']}")
                print(f"Grades: {grades}")
                print(f"Average: {record['average']:.2f}")
                print(f"Status: {record['status']}")
            else:
                print("No grades yet.")
            input("\nPress Enter to go back...")

        elif option == "2":
            break


def teacher_menu(user):
    while True:
        clear()
        print(f"Teacher - {user['name']}")
        print("1. Enter grades")
        print("2. View history")
        print("3. Logout")
        option = input("> ").strip()

        if option == "1":
            clear()
            student_id = input("Student ID: ").strip()
            student = next((u for u in users.values() if u["id"] == student_id), None)

            if not student or student["role"] != "student":
                print("Student ID not found.")
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
            if avg >= 7:
                status = "Approved"
            elif avg >= 5:
                status = "Remedial"
            else:
                status = "Failed"

            history[:] = [r for r in history if r["id"] != student_id]
            history.append({
                "id": student_id,
                "name": student["name"],
                "grades": grades,
                "average": round(avg, 2),
                "status": status,
            })
            input("\nSaved. Press Enter to continue...")

        elif option == "2":
            clear()
            print(f"{'ID':<10}{'Student':<18}{'Avg':<8}Status")
            print("-" * 44)
            if not history:
                print("No records yet.")
            for r in history:
                print(f"{r['id']:<10}{r['name']:<18}{r['average']:<8.2f}{r['status']}")
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