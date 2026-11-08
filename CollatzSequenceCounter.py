#  Make an integer n.
n = int(input("Please give an integer:"))
#  If n is even, divide it by 2 (n / 2). If n is odd, multiply it by 3 and add 1 (3n + 1). Repeat this process until n = 1.
steps = 0
while 1 < n:
    if n % 2 == 0:
        print(n)
        n = n//2
        steps+=1
    else:
        n = 3*n + 1
        steps+=1
#  Write a program that returns the total number of steps it took to reach 1 for any given starting number.
print(f"Number of steps taken are {steps}")
