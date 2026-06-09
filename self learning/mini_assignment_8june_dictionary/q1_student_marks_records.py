'''----------------------------------------------------
Problem Statement: Student Performance Analytics System

A coaching institute wants to analyze student performance.
Store details of at least 30 students in a dictionary.

Example Structure
students = {
 "S101": {"name": "Anuj", "marks": 85},
 "S102": {"name": "Rahul", "marks": 72}
}

Requirements
1. Display all student records.
2. Search a student using Student ID.
3. Add a new student.
4. Update marks of an existing student.
5. Delete a student.
6. Find topper and lowest scorer.
7. Calculate class average.
8. Count pass and fail students.
9. Generate grades.
10. Display students scoring above average.
11. Display top 5 performers.
12. Create scholarship dictionary (marks > 85)
----------------------------------------------------'''

#----------------------------------------------------
# student records (30 students)
students = {
 "S101": {"name": "Anuj", "marks": 85},
 "S102": {"name": "Rahul", "marks": 72},
 "S103": {"name": "Priya", "marks": 91},
 "S104": {"name": "Neha", "marks": 68},
 "S105": {"name": "Amit", "marks": 78},
 "S106": {"name": "Rohan", "marks": 88},
 "S107": {"name": "Kavya", "marks": 55},
 "S108": {"name": "Ishaan", "marks": 4},
 "S109": {"name": "Meera", "marks": 92},
 "S110": {"name": "Dev", "marks": 47},
 "S111": {"name": "Sanya", "marks": 81},
 "S112": {"name": "Kabir", "marks": 73},
 "S113": {"name": "Aarav", "marks": 69},
 "S114": {"name": "Diya", "marks": 95},
 "S115": {"name": "Arjun", "marks": 58},
 "S116": {"name": "Simran", "marks": 83},
 "S117": {"name": "Yash", "marks": 77},
 "S118": {"name": "Pooja", "marks": 62},
 "S119": {"name": "Riya", "marks": 89},
 "S120": {"name": "Manav", "marks": 90},
 "S121": {"name": "Tanya", "marks": 71},
 "S122": {"name": "Harsh", "marks": 66},
 "S123": {"name": "Nikhil", "marks": 84},
 "S124": {"name": "Ira", "marks": 93},
 "S125": {"name": "Om", "marks": 52},
 "S126": {"name": "Laksh", "marks": 79},
 "S127": {"name": "Mahi", "marks": 87},
 "S128": {"name": "Vansh", "marks": 44},
 "S129": {"name": "Khushi", "marks": 76},
 "S130": {"name": "Pari", "marks": 60}
}

#----------------------------------------------------
# menu-driven system
while True:
    print("\n========== STUDENT ANALYTICS MENU ==========")
    print("1. Display all records")
    print("2. Search student")
    print("3. Add student")
    print("4. Update marks")
    print("5. Delete student")
    print("6. Topper & Lowest scorer")
    print("7. Class average")
    print("8. Pass/Fail count")
    print("9. Grades")
    print("10. Above average students")
    print("11. Top 5 performers")
    print("12. Scholarship students")
    print("13. Exit")

    choice = int(input("Enter choice: "))

    #------------------------------------------------
    if choice == 1:
        print("\n--- ALL STUDENTS ---")
        for sid in students:
            print(sid, "->", students[sid])

    #------------------------------------------------
    elif choice == 2:
        sid = input("Enter Student ID: ")
        if sid in students:
            print("Found:", students[sid])
        else:
            print("Not found")

    #------------------------------------------------
    elif choice == 3:
        sid = input("Enter new ID: ")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[sid] = {"name": name, "marks": marks}
        print("Student added")

    #------------------------------------------------
    elif choice == 4:
        sid = input("Enter ID: ")
        if sid in students:
            students[sid]["marks"] = int(input("Enter new marks: "))
            print("Updated")
        else:
            print("Not found")

    #------------------------------------------------
    elif choice == 5:
        sid = input("Enter ID to delete: ")
        if sid in students:
            del students[sid]
            print("Deleted")
        else:
            print("Not found")

    #------------------------------------------------
    elif choice == 6:
        # sample-style loop (no max/min)
        items = list(students.items())

        highest_id = items[0][0]
        lowest_id = items[0][0]

        highest_marks = items[0][1]["marks"]
        lowest_marks = items[0][1]["marks"]

        for item in items:
            sid = item[0]
            marks = item[1]["marks"]

            if marks > highest_marks:
                highest_marks = marks
                highest_id = sid

            if marks < lowest_marks:
                lowest_marks = marks
                lowest_id = sid

        print("Topper:", highest_id, students[highest_id])
        print("Lowest:", lowest_id, students[lowest_id])

    #------------------------------------------------
    elif choice == 7:
        total = 0
        count = 0

        for sid in students:
            total += students[sid]["marks"]
            count += 1

        print("Average:", total / count)

    #------------------------------------------------
    elif choice == 8:
        p = 0
        f = 0

        for sid in students:
            if students[sid]["marks"] >= 50:
                p += 1
            else:
                f += 1

        print("Pass:", p)
        print("Fail:", f)

    #------------------------------------------------
    elif choice == 9:
        print("\n--- GRADES ---")
        for sid in students:
            m = students[sid]["marks"]

            if m >= 90:
                g = "A"
            elif m >= 75:
                g = "B"
            elif m >= 50:
                g = "C"
            else:
                g = "F"

            print(sid, students[sid]["name"], "=>", g)

    #------------------------------------------------
    elif choice == 10:
        total = 0
        count = 0

        for sid in students:
            total += students[sid]["marks"]
            count += 1

        avg = total / count

        print("\n--- ABOVE AVERAGE ---")
        for sid in students:
            if students[sid]["marks"] > avg:
                print(sid, students[sid])

    #------------------------------------------------
    elif choice == 11:
        # manual top 5 (no sorting)
        temp = students.copy()

        print("\n--- TOP 5 ---")
        for _ in range(5):
            max_id = None
            max_marks = -1

            for sid in temp:
                if temp[sid]["marks"] > max_marks:
                    max_marks = temp[sid]["marks"]
                    max_id = sid

            print(max_id, temp[max_id])
            temp.pop(max_id)

    #------------------------------------------------
    elif choice == 12:
        scholarship = {}

        for sid in students:
            if students[sid]["marks"] > 85:
                scholarship[sid] = students[sid]

        print("\n--- SCHOLARSHIP STUDENTS ---")
        print(scholarship)

    #------------------------------------------------
    elif choice == 13:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

