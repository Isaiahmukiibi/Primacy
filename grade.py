students = {}

def calculate_cgp(marks):
    if marks >= 90:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 70:
        return 3.3
    elif marks >= 60:
        return 3.0
    elif marks >= 50:
        return 2.7
    elif marks >= 40:
        return 2.3
    elif marks >= 30:
        return 2.0
    elif marks >= 20:
        return 1.7
    elif marks >= 10:
        return 1.3
    else:
        return 1.0

def add_student():
    name = input("Enter student name: ")
    students[name] = {"CGPA": 0.0}
    
    for i in range(1, 6):
        unit = input("Enter course unit {}: ".format(i))
        marks = float(input("Enter coursework marks for {} (out of 100) in {}: ".format(name, unit)))
        cgp = calculate_cgp(marks)
        students[name][unit] = {"Marks": marks, "CGPA": cgp}
        students[name]["CGPA"] += cgp
    
    students[name]["CGPA"] /= 5  # Calculate the average CGPA

def print_students():
    print("Student Details:")
    for name, data in students.items():
        print("Name: {}, CGPA: {}".format(name, data["CGPA"]))
        for unit, unit_data in data.items():
            if unit not in ["CGPA"]:
                print("  {}: Marks: {}, CGPA: {}".format(unit, unit_data["Marks"], unit_data["CGPA"]))

def main():
    while True:
        print("\nMENU:")
        print("1. Add Student")
        print("2. Print Student Details")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            print_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
