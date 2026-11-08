#  First we make an integer n.
n = int(input("Please give an integer:"))
#  If n is even, divide it by 2 (n / 2). If n is odd, multiply it by 3 and add 1 (3n + 1). Repeat this process until n = 1.
steps = 0 #  This will print the number of steps taken in the end.
#  Now using while loop to keep the function running until n = 1.
while 1 < n:
    print(n)
#  Using if-else statement to have different functions if n is even or odd.
    if n % 2 == 0:
        n = n//2
        steps+=1
    else:
        n = 3*n + 1
        steps+=1
#  Outputting the total number of steps taken to bring any number to 1.
print(f"Number of steps taken are {steps}")
