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

# Problem 3 — The Number Analyser
# Write a program that has a list of 10 numbers (mix of positive and negative, you choose them). Then:
#
# Print all numbers greater than zero
# Print all numbers less than or equal to zero
# Print whether the list contains more positive numbers or more negative numbers (or if it's equal)
# Replace the last item in the list with the number 99 and print the updated list

Nums = [-83, 17, -31, -100, 56, 94, 67, -75, -75, -11]
list1 = [n for n in Nums if n > 0]
print(list1)
list2 = [n for n in Nums if n<0]
print(list2)

if len(list1) > len(list2):
    print("Nums contains more positive numbers than negative numbers")
else:
    print("Nums contains more negative numbers than positive numbers")

Nums[9] = 99
print(Nums)