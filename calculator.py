name = input("Student name: ").strip()
while name == "":
    name = input("Name can't be empty: ").strip()

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

print()
print(name)
for i, g in enumerate(grades, 1):
    print(f"Grade {i}: {g:.1f}")
print(f"Average: {avg:.2f}")
print(f"Status: {status}")
