
import streamlit as st

class Student:
    def __init__(self, name, rollno, marks, dept):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.dept = dept

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def display_details(self):
        cols = st.columns(5)  # Create 5 columns
        cols[0].write(f"**Name:** {self.name}")
        cols[1].write(f"**Roll No:** {self.rollno}")
        cols[2].write(f"**Department:** {self.dept}")
        cols[3].write(f"**Marks:** {self.marks}")
        cols[4].write(f"**Grade:** {self.calculate_grade()}")

# Create an empty list to store student objects
students = []

# Create a form to input student information
st.title("Student Information System")
with st.form("student_form"):
    name = st.text_input("Enter Student Name")
    rollno = st.number_input("Enter Roll Number")
    marks = st.number_input("Enter Marks")
    dept = st.text_input("Enter Department")
    submitted = st.form_submit_button("Add Student")

# Use a session state to store the students list
if "students" not in st.session_state:
    st.session_state.students = []

if submitted:
    # Create a new Student object and add it to the list
    student = Student(name, rollno, marks, dept)
    st.session_state.students.append(student)
    st.write("Student added successfully!")

# Display all student details
st.title("Student Details")
if st.session_state.students:
    st.write("List of Students:")
    for i, student in enumerate(st.session_state.students, start=1):
        st.write(f"**Student {i}:**")
        student.display_details()
        st.write("---")
else:
    st.write("No students added yet!")

# Add a button to clear the list
if st.button("Clear List"):
    st.session_state.students.clear()
    st.write("List cleared!")


    
