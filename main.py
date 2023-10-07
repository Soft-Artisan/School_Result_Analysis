# Import the School class to work with the collection of report cards.
from school import School

# Number of students in the school.
NUM_STUDENTS = 10

# Entry point of the program.
if __name__ == "__main__":
    #print("Program started")  # Debug print
    # Instantiate a school object with report cards for all students.
    school = School("students", NUM_STUDENTS)
    #print("School initialized")  # Debug print
    # Display various statistics.
    print("Average Student Grade:", school.average_student_grade)
    print("Hardest Subject:", school.hardest_subject)
    print("Easiest Subject:", school.easiest_subject)
    print("Best Performing Grade:", school.best_grade_level)
    print("Worst Performing Grade:", school.worst_grade_level)
    print("Best Student ID:", school.best_student)
    print("Worst Student ID:", school.worst_student)
