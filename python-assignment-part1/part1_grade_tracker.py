class GradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self, subject):
        if subject in self.grades:
            return sum(self.grades[subject]) / len(self.grades[subject])
        else:
            return 0

    def display_grades(self):
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

# Example usage:
if __name__ == '__main__':
    tracker = GradeTracker()
    tracker.add_grade('Math', 95)
    tracker.add_grade('Math', 85)
    tracker.add_grade('Science', 90)
    tracker.display_grades()
    print(f"Average Math grade: {tracker.calculate_average('Math')}")
