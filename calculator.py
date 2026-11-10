import os

users = {
    "teacher": {"password": "teacher123", "role": "teacher", "name": "Prof. Matheus"},
    "student": {"password": "student123", "role": "student", "name": "Matheus Dias"},
}

history = [
    {"name": "Ana Silva", "grades": [8.5, 7.5, 9.0], "average": 8.33, "status": "Approved"},
    {"name": "Bruno Costa", "grades": [4.0, 5.0, 5.5], "average": 4.83, "status": "Failed"},
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    clear()
    print("Academic Portal")
    print("-" * 30)
    username = input("Username: ").strip()
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
        print(f"Student - {user['name']}")
        print("1. Calculate my grade")
        print("2. Logout")
        option = input("> ").strip()

        if option == "1":
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

            history.append({
                "name": user["name"],
                "grades": grades,
                "average": round(avg, 2),
                "status": status,
            })

            print(f"\nAverage: {avg:.2f}")
            print(f"Status: {status}")
            input("\nPress Enter to go back...")

        elif option == "2":
            break


def teacher_menu(user):
    while True:
        clear()
        print(f"Teacher - {user['name']}")
        print("1. View grade history")
        print("2. Logout")
        option = input("> ").strip()

        if option == "1":
            clear()
            print(f"{'Student':<18}{'Grades':<18}{'Avg':<8}Status")
            print("-" * 52)
            if not history:
                print("No records yet.")
            for r in history:
                grades = ", ".join(f"{g:.1f}" for g in r["grades"])
                print(f"{r['name']:<18}{grades:<18}{r['average']:<8.2f}{r['status']}")
            input("\nPress Enter to go back...")

        elif option == "2":
            break


while True:
    user = login()
    if user is None:
        continue
    if user["role"] == "teacher":
        teacher_menu(user)
    else:
        student_menu(user)