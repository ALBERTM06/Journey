# Problem 1 — The Grade Classifier
# Write a program that stores a list of 5 student scores (numbers you choose). Then:
#
# Calculate and print the average score
# Print whether the average is a "Pass" (50 and above) or "Fail" (below 50)
# Print the highest and lowest score in the list
# Print the scores sorted from highest to lowest

#Solution1:
# NumberStudents = int(input("Enter number of students: "))
# g=0
# Grades = []
# while g < NumberStudents:
#     grade = int((input("Enter grade: ")))
#     Grades.append(grade)
#     g+=1
# print(Grades)
#
# average = sum(Grades)/len(Grades)
# print(average)
#
# if average >= 50:
#     print("Pass")
# else:
#     print("Fail")
#
# print("Maximum Grade: " , max(Grades))
# print("Minimum Grade: " , min(Grades))
#
# Grades.sort(reverse = True)
# print(Grades)

# Problem 2 — The Shopping Filter
# You have this list:
# shopping = ["apple", "Banana", "carrot", "Dragonfruit", "eggplant"]
#
# Print the first and last item in the list
# Create a new list that only contains items whose names are longer than 6 characters
# Sort that new list alphabetically and print it
# Print how many items are in the new list

#Solution2
# shopping = ["apple", "Banana", "carrot", "Dragonfruit", "eggplant"]
# print(shopping[0], shopping[4])
#
# shopping2=[item for item in shopping if len(item)>6]
# shopping2.sort()
# print(shopping2)
# print(len(shopping2))