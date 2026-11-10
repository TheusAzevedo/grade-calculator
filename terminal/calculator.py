import os
import random
import re
import base64
import locales

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


def t(key):
    return locales.translations[locales.current_lang][key]


def enc(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def dec(s):
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')


def status_label(st):
    if locales.current_lang != "pt":
        return st
    if st == "Approved":
        return "Aprovado"
    if st == "Remedial":
        return "Recuperação"
    return "Reprovado"


def login():
    clear()
    print("=" * 45)
    print(t("portalTitle"))
    print(f"                                   [ {t('currentLoc')} ]")
    print("=" * 45)
    print(t("menuSignIn"))
    print(t("menuRegister"))
    print(t("menuLanguage"))
    print("=" * 45)
    choice = input("> ").strip()

    if choice == "3":
        locales.location_menu()
        return None

    if choice == "2":
        clear()
        print(t("regTitle"))
        first_name = input(t("fieldFirstName")).strip()
        last_name = input(t("fieldLastName")).strip()
        email = input(t("fieldEmail")).strip().lower()
        password = input(t("fieldPassword")).strip()
        confirm = input(t("fieldConfirmPassword")).strip()

        if not first_name or not last_name or not email or not password:
            print(t("errRequired"))
            input(t("pressEnter"))
            return None

        if not re.match(NAME_REGEX, first_name) or not re.match(NAME_REGEX, last_name):
            print(t("errName"))
            input(t("pressEnter"))
            return None

        if not re.match(EMAIL_REGEX, email):
            print(t("errEmail"))
            input(t("pressEnter"))
            return None

        if len(password) < 6:
            print(t("errPassLength"))
            input(t("pressEnter"))
            return None

        if password != confirm:
            print(t("errPassMatch"))
            input(t("pressEnter"))
            return None

        if email in users:
            print(t("errEnumMitigation"))
            input(t("pressEnter"))
            return None

        full_name = first_name.capitalize() + " " + last_name.capitalize()

        existing_id = ""
        for u in users.values():
            if dec(u["name"]).lower() == full_name.lower():
                existing_id = u.get("id", "")
                break

        if not existing_id:
            while True:
                existing_id = str(random.randint(100000, 999999))
                if not any(u.get("id") == existing_id for u in users.values()):
                    break

        users[email] = {
            "password": enc(password),
            "role": "student",
            "name": enc(full_name),
            "id": existing_id,
        }

        print(t("successReg") + existing_id)
        input(t("pressEnter"))
        return None

    clear()
    print(t("signInTitle"))
    email = input(t("fieldEmail")).strip().lower()
    password = input(t("fieldPasswordLogin"))

    user = users.get(email)
    if user and dec(user["password"]) == password:
        return user

    print(t("errWrongCreds"))
    input(t("pressEnterTry"))
    return None


def student_menu(user):
    while True:
        clear()
        nome = dec(user['name'])
        print(t("studentHeader") + nome + " | ID: " + user['id'])
        print("=" * 45)
        print(t("menuViewReport"))
        print(t("menuLogout"))
        print("=" * 45)
        option = input("> ").strip()

        if option == "1":
            clear()
            print(t("reportHeader"))
            record = None
            for r in history:
                if r["id"] == user["id"]:
                    record = r
                    break

            if record:
                print(t("reportName") + record['name'])
                print("ID (RA): " + record['id'])
                grades_str = ", ".join(f"{g:.1f}" for g in record["grades"])
                print(t("reportGrades") + grades_str)
                print(t("reportAverage") + f"{record['average']:.2f}")
                print(t("reportStatus") + "[" + status_label(record["status"]).upper() + "]")
            else:
                print(t("noGradesYet"))
            input(t("pressEnterBack"))

        elif option == "2":
            break


def teacher_menu(user):
    while True:
        clear()
        nome = dec(user['name'])
        print(f"Teacher - {nome}")
        print("=" * 45)
        print(t("menuLaunchGrades"))
        print(t("menuViewHistory"))
        print(t("menuLogoutTeacher"))
        print("=" * 45)
        option = input("> ").strip()

        if option == "1":
            clear()
            print(t("launchHeader"))
            student_id = input(t("fieldStudentID")).strip()

            student_user = None
            for u in users.values():
                if u.get("id") == student_id:
                    student_user = u
                    break

            if not student_user:
                print(t("errIDNotFound"))
                input(t("pressEnter"))
                continue

            grades = []
            for i in range(1, 4):
                while True:
                    try:
                        g = float(input(t("fieldGrade") + f"{i}: "))
                    except ValueError:
                        print(t("errNumber"))
                        continue
                    if 0 <= g <= 10:
                        grades.append(g)
                        break
                    print(t("errGradeBounds"))

            avg = sum(grades) / 3
            if avg >= 7:
                status = "Approved"
            elif avg >= 5:
                status = "Remedial"
            else:
                status = "Failed"

            for i, r in enumerate(history):
                if r["id"] == student_id:
                    del history[i]
                    break

            history.append({
                "id": student_id,
                "name": dec(student_user["name"]),
                "grades": grades,
                "average": round(avg, 2),
                "status": status,
            })
            print(t("successLaunch"))
            input(t("pressEnter"))

        elif option == "2":
            clear()
            print(f"{'ID':<10}{'Student':<18}{'Avg':<8}Status")
            print("-" * 40)
            if not history:
                print(t("historyEmpty"))
            for r in history:
                print(f"{r['id']:<10}{r['name']:<18}{r['average']:<8.2f}{status_label(r['status'])}")
            input(t("pressEnterBack"))

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