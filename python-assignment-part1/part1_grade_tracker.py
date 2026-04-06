#Task 1 ###################################################### starts here
# Raw student data with unformatted names, string rolls, and comma-separated marks
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Clean each student record
cleaned_students = []
for stu in raw_students:
    cleaned_students.append({
        "name": stu["name"].strip().title(),   # Remove whitespace and convert to Title Case
        "roll": int(stu["roll"]),               # Convert roll from string to integer
        "marks": [int(mrk) for mrk in stu["marks_str"].split(", ")]  # Split marks string into list of ints
    })

# Verify name and print formatted profile card
for student in cleaned_students:
    is_valid = all(word.isalpha() for word in student["name"].split())
    status = "✓ Valid name" if is_valid else "✗ Invalid name"
    print("================================")
    print(f" Student : {student['name']} ({status})")
    print(f" Roll No : {student['roll']}")
    print(f" Marks   : {student['marks']}")
    print("================================")

# Print name in ALL CAPS and lowercase for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print(f"\nRoll 103 - ALL CAPS  : {student['name'].upper()}")
        print(f"Roll 103 - lowercase : {student['name'].lower()}")
        break
#Task 1 ###################################################### ends  here
#Task 2 ###################################################### starts  here

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Grade label based on marks
def get_grade(m):
    if m >= 90: return "A+"
    elif m >= 80: return "A"
    elif m >= 70: return "B"
    elif m >= 60: return "C"
    else: return "F"

# Print each subject with marks and grade
print(f"Student: {student_name}\n")
for i in range(len(subjects)):
    print(f"  {subjects[i]:<12} : {marks[i]:>3}  ({get_grade(marks[i])})")

# Total and average
total = sum(marks)
average = round(total / len(marks), 2)
print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")

# Highest and lowest scoring subject
max_idx = marks.index(max(marks))
min_idx = marks.index(min(marks))
print(f"Highest       : {subjects[max_idx]} ({marks[max_idx]})")
print(f"Lowest        : {subjects[min_idx]} ({marks[min_idx]})")

# While loop - simulate marks-entry system
new_count = 0
while True:
    subject = input("\nEnter subject name (or 'done' to stop): ").strip()
    if subject.lower() == "done":
        break

    marks_input = input(f"Enter marks for {subject} (0-100): ").strip()

    # Validate marks input
    try:
        m = int(marks_input)
    except ValueError:
        print(f"  ⚠ Invalid input '{marks_input}' — must be a number. Skipping.")
        continue

    if m < 0 or m > 100:
        print(f"  ⚠ Marks {m} out of range (0-100). Skipping.")
        continue

    subjects.append(subject)
    marks.append(m)
    new_count += 1
    print(f"  ✓ Added {subject} with {m} marks ({get_grade(m)})")

# Summary after adding new subjects
print(f"\nNew subjects added : {new_count}")
updated_avg = round(sum(marks) / len(marks), 2)
print(f"Updated average    : {updated_avg}")

#Task 2 ###################################################### ends  here

#Task 3 ###################################################### starts  here

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Compute averages and statuses
results = []
for name, mrks in class_data:
    avg = round(sum(mrks) / len(mrks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    results.append((name, avg, status))

# Print formatted class report
print(f"\n{'Name':<18}| {'Average':>7} | Status")
print("-" * 40)
for name, avg, status in results:
    print(f"{name:<18}| {avg:>7.2f} | {status}")

# Pass/Fail counts
passed = sum(1 for _, _, s in results if s == "Pass")
failed = len(results) - passed
print(f"\nPassed : {passed}")
print(f"Failed : {failed}")

# Class topper
topper = max(results, key=lambda r: r[1])
print(f"Topper : {topper[0]} ({topper[1]})")

# Class average
class_avg = round(sum(avg for _, avg, _ in results) / len(results), 2)
print(f"Class Average : {class_avg}")

#Task 3 ###################################################### ends  here

#Task 4 ###################################################### starts  here

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"Step 1 - Stripped   : '{clean_essay}'")

# Step 2: Convert to Title Case
print(f"Step 2 - Title Case : {clean_essay.title()}")

# Step 3: Count no of occurrences of "python" (case-insensitive)
python_count = clean_essay.count("python")
print(f"Step 3 - 'python' count : {python_count}")

# Step 4: Replace "python" with "Python 🐍"
replaced = clean_essay.replace("python", "Python 🐍")
print(f"Step 4 - Replaced   : {replaced}")

# Step 5: Split into sentences by ". "
sentences = clean_essay.split(". ")
print(f"Step 5 - Sentences  : {sentences}")

# Step 6: Print number to each sentence, ensuring it ends with "."
print("Step 6 - Numbered sentences:")
for idx, sentence in enumerate(sentences, 1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"  {idx}. {sentence}")

#Task 4 ###################################################### ends  here


####Output#######
# PS C:\Users\spochimcherla\OneDrive - Infor\Infor\CHW\ERP_Stage2\ANADocuments> & "C:/Program Files/Python312/python.exe" "c:/Users/spochimcherla/OneDrive - Infor/Infor/CHW/ERP_Stage2/ANADocuments/part1_grade_tracker.py"
# ================================
#  Student : Ayesha Sharma (✓ Valid name)
#  Roll No : 101
#  Marks   : [88, 72, 95, 60, 78]
# ================================
# ================================
#  Student : Rohit Verma (✓ Valid name)
#  Roll No : 102
#  Marks   : [55, 68, 49, 72, 61]
# ================================
# ================================
#  Student : Priya Nair (✓ Valid name)
#  Roll No : 103
#  Marks   : [91, 85, 88, 94, 79]
# ================================
# ================================
#  Student : Karan Mehta (✓ Valid name)
#  Roll No : 104
#  Marks   : [40, 55, 38, 62, 50]
# ================================
# ================================
#  Student : Sneha Pillai (✓ Valid name)
#  Roll No : 105
#  Marks   : [75, 80, 70, 68, 85]
# ================================
#
# Roll 103 - ALL CAPS  : PRIYA NAIR
# Roll 103 - lowercase : priya nair
# Student: Ayesha Sharma
#
#   Math         :  88  (A)
#   Physics      :  72  (B)
#   CS           :  95  (A+)
#   English      :  60  (C)
#   Chemistry    :  78  (B)
#
# Total Marks   : 393
# Average Marks : 78.6
# Highest       : CS (95)
# Lowest        : English (60)
#
# Enter subject name (or 'done' to stop): DataScience
# Enter marks for DataScience (0-100): 98
#   ✓ Added DataScience with 98 marks (A+)
#
# Enter subject name (or 'done' to stop): Statistics
# Enter marks for Statistics (0-100): 100
#   ✓ Added Statistics with 100 marks (A+)
#
# Enter subject name (or 'done' to stop): probability
# Enter marks for probability (0-100): 100
#   ✓ Added probability with 100 marks (A+)
#
# Enter subject name (or 'done' to stop): MachineLearning
# Enter marks for MachineLearning (0-100): 98
#   ✓ Added MachineLearning with 98 marks (A+)
#
# Enter subject name (or 'done' to stop): done
#
# New subjects added : 4
# Updated average    : 87.67
#
# Name              | Average | Status
# ----------------------------------------
# Ayesha Sharma     |   78.60 | Pass
# Rohit Verma       |   61.00 | Pass
# Priya Nair        |   87.40 | Pass
# Karan Mehta       |   49.00 | Fail
# Sneha Pillai      |   75.60 | Pass
#
# Passed : 4
# Failed : 1
# Topper : Priya Nair (87.4)
# Class Average : 70.32
# Step 1 - Stripped   : 'python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.'
# Step 2 - Title Case : Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.
# Step 3 - 'python' count : 2
# Step 4 - Replaced   : Python 🐍 is a versatile language. it supports object oriented, functional, and procedural programming. Python 🐍 is widely used in data science and machine learning.
# Step 5 - Sentences  : ['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']
# Step 6 - Numbered sentences:
#   1. python is a versatile language.
#   2. it supports object oriented, functional, and procedural programming.
#   3. python is widely used in data science and machine learning.
