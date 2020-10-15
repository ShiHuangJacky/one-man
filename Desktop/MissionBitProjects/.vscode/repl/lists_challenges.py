subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("Computer Science")
grades.append(100)

gradebook = zip(subjects,grades)

gradebook.append(("visual arts", 93))
last_semester_gradebook = [("politics", 90), ("latin", 96), ("dance", 97), ("architecture", 65)]
full_gradebook = (last_semester_gradebook, gradebook)
print(full_gradebook)