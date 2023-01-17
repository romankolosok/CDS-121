
num = float(input("Enter a positive whole number: "))
while(not num.is_integer()):
    print("Number is not an integer, please try again\n")
    num = float(input("Enter a positive whole number: "))

num = int(num)
for i in range(1, num+1):
    if num % i == 0:
        print(i)