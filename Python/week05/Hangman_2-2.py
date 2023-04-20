#A program that takes an int and multiplies it from 1 to 10

num = int(input("Display multiplication table of : "))

#prints the table
for i in range ( 1 , 11):
    multi = num * i
    print(num, "X" , i, "=", multi)
