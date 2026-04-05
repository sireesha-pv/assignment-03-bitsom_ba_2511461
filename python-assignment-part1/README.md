# Grade Tracker Assignment - Part 1

## Overview
This is a Python-based grade tracking application that allows users to manage and track grades for different subjects.

## Features
- **Add Grades**: Add grades for different subjects
- **Calculate Averages**: Compute the average grade for each subject
- **Display Grades**: View all stored grades organized by subject

## File Structure
```
python-assignment-part1/
├── part1_grade_tracker.py
└── README.md
```

## Usage

### Running the Application
```bash
python part1_grade_tracker.py
```

### Example Code
```python	racker = GradeTracker()
tracker.add_grade('Math', 95)
tracker.add_grade('Math', 85)
tracker.add_grade('Science', 90)
tracker.display_grades()
print(f"Average Math grade: {tracker.calculate_average('Math')}")
```

## Class: GradeTracker

### Methods
- `__init__()`: Initialize the grade tracker with an empty grades dictionary
- `add_grade(subject, grade)`: Add a grade for a given subject
- `calculate_average(subject)`: Calculate and return the average grade for a subject
- `display_grades()`: Display all grades organized by subject

## Requirements
- Python 3.6 or higher

## Author
Assignment submission for BITSOM_BA_2511461