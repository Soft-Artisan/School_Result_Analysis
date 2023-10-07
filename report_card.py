# Required libraries for file manipulation and JSON reading
import json
import os

# The ReportCard class represents an individual student's report card.
class ReportCard:
    # Class variable that lists the subjects each student takes.
    SUBJECTS = ["math", "science", "history", "english", "geography"]

    # Constructor initializes the report card with data, default is empty.
    def __init__(self, data={}):
        self.data = data

    # Property to calculate the average grade for a student.
    @property
    def average(self):
        sum_of_marks = sum(self.data[subject] for subject in ReportCard.SUBJECTS)
        return sum_of_marks / len(ReportCard.SUBJECTS)

    # Property to get the grade level of a student.
    @property
    def grade(self):
        return self.data.get("grade")

    # Property to get the ID of the student.
    @property
    def student_id(self):
        return self.data.get("id")

    # Class method to load a report card from a JSON file based on student number.
    @classmethod
    def from_file(cls, directory, student_number):
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(directory, f"{student_number}.json")
        path = os.path.join(base_path, file_path)
        try:
            # Attempt to open and read the file.
            with open(path, "r") as file:
                data = json.load(file)
            return cls(data)
        except FileNotFoundError:
            # If file doesn't exist, return an empty report card.
            return cls()
        



