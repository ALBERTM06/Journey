Details = {} #Empty Dictionary that will contain student data

Details["Name"] = input("Enter Name: ") #Student name
Subject_Count = int(input("Enter Number of Subjects: "))

subjects = {}
for i in range(Subject_Count):
    Subject = input("Enter Subject: ").strip().title() #.strip() removes leading/trailing spaces, .title() makes “physics” → “Physics” for consistent keys.
    Grade = int(input("Enter Grade: "))
    subjects[Subject] = Grade

Details["Subjects"] = subjects

grades = list(subjects.values())

average = sum(grades)/len(grades)
highest = max(grades)
lowest = min(grades)

Details["Average"] = average
Details["Highest"] = highest
Details["Lowest"] = lowest


print("\n--- Student Performance ---")
print("Name:", Details["Name"])
print("Subjects and Grades:")
for subject, grade in Details["Subjects"].items():
    print(f"  {subject}: {grade}")
print("Average Grade:", Details["Average"])
print("Highest Grade:", Details["Highest"])
print("Lowest Grade:", Details["Lowest"])



