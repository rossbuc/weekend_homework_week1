# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
from itertools import filterfalse
for number in filterfalse(lambda x : x % 2, numbers):
    even_numbers.append(number)

# 2. Print the difference between the largest and smallest value:
sorted_numbers = sorted(numbers)
difference_between = sorted_numbers[len(numbers) - 1] - numbers[0]

print(difference_between)
# 3. Print True if the list contains a 2 next to a 2 somewhere.
double_2 = False
for x in range(0, len(numbers) - 1):
    if numbers[x] == 2 and numbers[x + 1] == 2:
        double_2 = True



# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum_not_6_to_7 = 0
counter = False

for number in numbers:
    if number == 6:
        counter = True
    elif number == 7 and counter == True:
        counter = False
        continue

    if counter == True:
        continue
    else:
        sum_not_6_to_7 += number


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 






