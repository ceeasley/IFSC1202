#A school decided to replace the desks in three classrooms. Each desk seats two students.
#Given the number of students in each class, determine the smallest possible number of desks that can be purchased.
#The program should:
#    Read three integers: the number of students in each of the three classerooms A, B and C respectively.
#    Use floor division to find the number of desk that has two students and use modulus to find the number of desks that have one student.
#    Add the number of desks needed for each classroom and print the total.

#Example:
#Classroom A has 20 students and thus needs 10 desks.
#Classroom B has 21 students, so they can get by with no fewer than 11 desks.
#Classroom C has 22 and also needs 11 desks
#32 desks in total (10 + 11 + 11)

a = int(input("How many students are in Classroom A?: "))
b = int(input("How many students are in Classroom B?: "))
c = int(input("How many students are in Classroom C?: "))

fulldesks_a = a//2
fulldesks_b = b//2
fulldesks_c = c//2

remain_a = a%2
remain_b = b%2
remain_c = c%2

totaldesks_a = fulldesks_a + remain_a
totaldesks_b = fulldesks_b + remain_b
totaldesks_c = fulldesks_c + remain_c

total = totaldesks_a + totaldesks_b + totaldesks_c

print("Classroom A needs "+str(totaldesks_a)+" desks. Classroom B needs "+str(totaldesks_b)+" desks. Classroom C needs "+str(totaldesks_c)+" desks. Overall, "+str(total)+" desks are needed.")
