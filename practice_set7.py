# Practice set on loops in python
'''
# Ques1. Write a program to print the multiplication table of a given number using for loop ?
num = int(input("Enter the number: "))
for i in range(1,11):
    print(num*i)

print(f"Multiplicaation table of {num} has been printed using for loop.\n")


# Ques2. Write a program to greet all the person names stored in the list "l" and which starts with S. l= ["Harry", "Sohan", "Sachin", "Rahul"]
name_list = ["Harry", "Sohan", "Sachin", "Rahul"]
print("Given list of name is -->",name_list)
i = 0
j = 0
while(i<len(name_list)):
    if(name_list[i][j] == "S"):
        print("Welcome ",name_list[i])
        i += 1
    else:
        i+=1

print(f"Greeting program has been run using while loop.\n")


# Ques3. Attempt problem 1 using while loop ?
n = int(input("Enter the number for printing table: "))
k = 1
while(k<=10):
    print(n*k)
    k += 1

print(f"Multiplicaation table of {n} has been printed using while loop.\n")


# Ques4. Write a program to find wheather a given number is prime or not ?
given_num = int(input("Enter the Number: "))
i = 2
while(i<given_num):
    if(given_num%i != 0):
        i += 1
        if(i == given_num):
            print(f"{given_num} is a Prime Nmuber.")

    else:
        print(f"{given_num} is Not a Prime number.")
        break

print("Prime number program has been run using while loop.\n")


# Ques5. Write a program to find the sum of first n natural numbers using while loop ?
natural_num = int(input("Enter the number: "))
sum = 0
i = 1
while(i<=natural_num):
    sum = sum+i
    i += 1
print(f"Sum of first {natural_num} natural number is ->",sum)

print(f"Sum of first {natural_num} number program has been run using while loop.\n")

'''

# Ques6. Write a program to calculate the factorial of a given number using for loop ?
fact_num = int(input("Enter the Number: "))
factorial = 1
for i in range(1, fact_num+1):
    factorial *= i

print(f"factorial of {fact_num} is ->{factorial}")

print("Factorial of the given entered number has been run successfuly.")