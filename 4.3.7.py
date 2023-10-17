#Your task is to write a function checking whether a number is prime or not.

#The function:

#is called is_prime;
#takes one argument (the value to check)
#returns True if the argument is a prime number, and False otherwise.
#Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder ‒ if it's zero, your number cannot be a prime; think carefully about when you should stop the process.

#If you need to know the square root of any value, you can utilize the ** operator. Remember: the square root of x is the same as x0.5

#Complete the code in the editor.

#Run your code and check whether your output is the same as ours.



def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#################################################

def is_prime(num):
    if num <= 1:
        return False  # 1 and any negative number are not prime

    if num <= 3:
        return True  # 2 and 3 are prime

    if num % 2 == 0 or num % 3 == 0:
        return False  # Divisible by 2 or 3, not prime

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False  # Divisible by i or i+2, not prime
        i += 6

    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
