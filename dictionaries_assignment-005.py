Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Abrar Aslam
... # SP24-BBA-005
... # Section C
... 
... 
... 
... # Creating a dictionary with 10 students and their scores
... student_scores = {
...     "Rana": 88,
...     "Abubakr": 78,
...     "Faizan": 56,
...     "Saboor": 88,
...     "Taha": 76,
...     "Ahmed": 60,
...     "Ahad": 70,
...     "Abubakr": 86,
...     "Chattur": 42,
...     "Farhan": 82
... }
... 
... # No.1. get() - Retrieve the score of a specific student
... print("1. Rana's score is:", student_scores.get("Rana"))
... 
... # No.2. keys() - List all student names
... print("2. List of students:", list(student_scores.keys()))
... 
... # No.3. values() - List all scores
... print("3. Their scores:", list(student_scores.values()))
... 
... # No.4. items() - Display all key-value pairs
... print("4. Student and score pairs:")
... for name, score in student_scores.items():
...     print(f"   {name}: {score}")
... 
... # No.5. update() - Update a student's score
... student_scores.update({"Ali": 89})
... print("5. Chattur's updated score:", student_scores["Chattur"])

# No.6. pop() - Remove a student and return their score
removed_score = student_scores.pop("Ahmed")
print("6. Ahmed was removed. His score was:", removed_score)

# No.7. popitem() - Remove the last inserted item
last_entry = student_scores.popitem()
print("7. Last entry removed (likely Farhan):", last_entry)

# No.8. copy() - Create a backup copy of the dictionary
scores_backup = student_scores.copy()
print("8. Backup of current student scores:", scores_backup)

# No.9. setdefault() - Add a new student only if they don't exist
student_scores.setdefault("Taha", 81)
print("9. Taha was added with default score. Current list:")
print(student_scores)

# No.10. fromkeys() - Create a new dictionary with default scores
new_students = ["Jawad", "Saim", "Haider"]
default_scores = dict.fromkeys(new_students, 52)
print("10. New students with default scores:", default_scores)


# clear() - Would remove all items from the dictionary
student_scores.clear()
