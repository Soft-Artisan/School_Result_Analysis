# Import the ReportCard class to work with individual report cards.
from report_card import ReportCard

# The School class represents the entire collection of student report cards.
class School:
    # Constructor loads all the report cards from the directory.
    def __init__(self, directory, num_students):
        self.report_cards = self._load_report_cards(directory, num_students)
        #print(f"Loaded {len(self.report_cards)} report cards")  # Debug print

    # Method to load report cards for all students.
    def _load_report_cards(self, directory, num_students):
        return [ReportCard.from_file(directory, i) for i in range(num_students)]

    # Property to compute the average grade for all students.
    @property
    def average_student_grade(self):
        return round(sum(rc.average for rc in self.report_cards) / len(self.report_cards), 2)

    # Method to compute the average grade per subject.
    def subject_averages(self):
        subjects = ReportCard.SUBJECTS
        subject_averages = {subject: 0 for subject in subjects}
        for rc in self.report_cards:
            for subject in subjects:
                subject_averages[subject] += rc.data[subject]
        for subject in subjects:
            subject_averages[subject] /= len(self.report_cards)
        return subject_averages

    # Method to compute the average grade per grade level.
    def grade_level_averages(self):
        grade_level_averages = {grade: [] for grade in range(1, 9)}
        for rc in self.report_cards:
            grade_level_averages[rc.grade].append(rc.average)
    
        for grade, averages in list(grade_level_averages.items()):  # Using list to avoid dictionary size change during iteration
            if averages:  # If there are students in this grade level
                grade_level_averages[grade] = sum(averages) / len(averages)
            else:  # If no students in this grade
                del grade_level_averages[grade]  # Remove this grade level from the dictionary

        return grade_level_averages
        

    # Properties for extracting various statistics.
    @property
    def hardest_subject(self):
        return min(self.subject_averages().items(), key=lambda x: x[1])[0]

    @property
    def easiest_subject(self):
        return max(self.subject_averages().items(), key=lambda x: x[1])[0]

    @property
    def best_grade_level(self):
        return max(self.grade_level_averages().items(), key=lambda x: x[1])[0]

    @property
    def worst_grade_level(self):
        return min(self.grade_level_averages().items(), key=lambda x: x[1])[0]

    @property
    def best_student(self):
        return max(self.report_cards, key=lambda x: x.average).student_id

    @property
    def worst_student(self):
        return min(self.report_cards, key=lambda x: x.average).student_id
