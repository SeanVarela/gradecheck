# Sean Varela 6/14/2020 8:03PM (or if you're not American,
# 14/6/2020 20:04 EST)

'''
What this does is, instead of doing all the math, 
you can input your earned score and attempted score and see
how an assignment will affect your grade. This was really just a project to learn Python with.
'''
# user inputs number of assignments
print("To calculate how an assignment will affect your grade add 1 to the input")
print("Example: If you have 15 assignments not including the one you want to calculate enter 16")
assignments = int(input("How many assignments do you have? : "))

# user input quality control
while assignments < 1:
    print("Really, do you even need to calculate this?")
    assignments = int(input("How many assignments do you have? : "))

# creating variables
earned_total = 0.0
attempted_total = 0.0

# the beef of the program
for i in range(1, assignments + 1):
    earned = float(input("Assignment " + str(i) + " earned score (numerator) : "))
    earned_total += earned
    attempted = float(input("Assignment " + str(i) + " attempted score (denominator) : "))
    attempted_total += attempted

final_decimal = earned_total / attempted_total

final_percent = final_decimal * 100

final_percent = round(final_percent, 2)

print("Your grade is " + str(final_percent) + "%")

print("A+ = 97-100%")
print("A = 93-96%")
print("A- = 90-92%")
print("B+ = 87-89%")
print("B = 83-86%")
print("B- = 80-82%")
print("C+ = 77-79%")
print("C = 73-76%")
print("C- = 70-72%")
print("D+ = 67-69%")
print("D = 63-66%")
print("D- = 60-62%")
print("F = Below 60%")
