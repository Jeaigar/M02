# Jermaine Bentley

# This application will assess and record the credentials and feats of the students which will include whether they have made the
# honor roll, deans list, or both. 

# File name is "Student Qualification Application GUI Version.py"

import tkinter as tk
from tkinter import messagebox

class StudentQualificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Qualification Application")

        # Initialize an empty list to store student records
        self.student_records = []

        # Create widgets
        self.last_name_label = tk.Label(root, text="Last Name:")
        self.last_name_entry = tk.Entry(root)
        self.first_name_label = tk.Label(root, text="First Name:")
        self.first_name_entry = tk.Entry(root)
        self.gpa_label = tk.Label(root, text="GPA:")
        self.gpa_entry = tk.Entry(root)
        self.submit_button = tk.Button(root, text="Submit", command=self.add_student_record)
        self.history_button = tk.Button(root, text="History", command=self.display_history)
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)

        # Grid layout
        self.last_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.last_name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.first_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.gpa_label.grid(row=2, column=0, padx=10, pady=5)
        self.gpa_entry.grid(row=2, column=1, padx=10, pady=5)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.history_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.quit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_student_record(self):
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        try:
            gpa = float(self.gpa_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid GPA. Please enter a valid numeric value.")
            return

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
        self.student_records.append(student_record)

        # Clear input fields
        self.last_name_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.gpa_entry.delete(0, tk.END)

        # Display qualification message
        messagebox.showinfo("Qualification", f"{first_name} {last_name} - {qualification_message}")

    def display_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Student Records History")
        for i, record in enumerate(self.student_records, start=1):
            record_str = f"{i}. {record['first_name']} {record['last_name']} - GPA: {record['gpa']}, Qualifications: {record['qualifications']}"
            tk.Label(history_window, text=record_str).pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentQualificationApp(root)
    app.run()
