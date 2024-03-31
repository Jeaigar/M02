# Jermaine Bentley

# This application will assess and record the credentials and feats of the students which will include whether they have made the
# honor roll, deans list, or both. 

# File name is "Student qualification app.py"

def main():
    print("Student Qualification Application")
    print("Enter 'ZZZ' for the last name to quit processing student records.")

    # Initialize an empty list to store student records
    student_records = []

    while True:
        last_name = input("\nEnter student's last name: ")
        if last_name.upper() == 'ZZZ':
            break  # Exit loop if 'ZZZ' is entered

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        # Check if student qualifies for Dean's List or Honor Roll
        qualifications = []
        if gpa >= 3.5:
            qualifications.append("Dean's List")
        if gpa >= 3.25:
            qualifications.append("Honor Roll")

        # Determine qualification message
        if qualifications:
            qualification_message = ", ".join(qualifications)
        else:
            qualification_message = "Unqualified"

        # Store student record in a dictionary
        student_record = {
            'last_name': last_name,
            'first_name': first_name,
            'gpa': gpa,
            'qualifications': qualification_message
        }
        student_records.append(student_record)

    # Print student records
    print("\nStudent Records:")
    for student in student_records:
        print(f"{student['last_name']}, {student['first_name']} - GPA: {student['gpa']} ({student['qualifications']})")

if __name__ == "__main__":
    main()
