#Print numbers from 1 to 30. But:

#If divisible by 3, print "Fizz".

#If divisible by 5, print "Buzz".

#If divisible by both 3 and 5, print "FizzBuzz".

#Otherwise, print the number itself.

for i in range(1, 31):
    if (i % 3 == 0 and i % 5 == 0):
        print(f"{i} es FizzBuzz ")
    elif (i % 5 == 0):
        print(f"{i} es Buzz ")
    elif (i % 3 == 0):
        print(f"{i} es Fizz ")