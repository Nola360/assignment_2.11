#Akinola Daramola Jr
#Programming Exercise 2.11
#Due Date: 6/16/22


#Declaring male and female students
males = 0
females = 0

#Redeclaring male and female students
males = int(input("Enter the number of male students. "))
females = int(input("Enter the number of female students. "))

#Declaring value of male and female students
male_students = males
female_students = females

#Declaring value of total students
total_students = males + females

#Computing percenttage of male and female students
percentage_of_male_students = male_students / total_students
percentage_of_female_students = female_students / total_students

#Results
print(f"Number of males: {male_students}")
print(f"Number of females: {female_students}")
print(f"Total number of students: {total_students}")
print(f"% of male students: {percentage_of_male_students:.0%}")
print(f"% of female students: {percentage_of_female_students:.0%}")

