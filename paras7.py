# Program to use a dictionary to store student details with marks for different subjects

# Initialize an empty dictionary to store student details
student_details = {}

# Get the number of students and number of subjects
num_students = int(input("Enter the number of students you want to enter details for: "))
num_subjects = int(input("Enter the number of subjects: "))

# Iterate over each student
for i in range(num_students):
    # Get the name of the student
    student_name = input("Enter the name of the student: ")
    
    # Initialize an empty dictionary to store marks for each subject
    marks = {}
    
    # Iterate over each subject
    for j in range(num_subjects):
        # Get the name of the subject and marks
        subject_name = input("Enter the name of the subject: ")
        subject_marks = int(input("Enter the marks of the student for {}: ".format(subject_name)))
        
        # Add subject marks to the dictionary
        marks[subject_name] = subject_marks
    
    # Add student details (name and marks) to the main dictionary
    student_details[student_name] = marks

# Print the dictionary containing student details
print("Student details:", student_details)
