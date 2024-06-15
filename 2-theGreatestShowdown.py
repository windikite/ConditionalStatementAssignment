# variables for all tasks
first_number = int(input('Input 1st number: '))
second_number = int(input('Input 2nd number: '))
third_number = int(input('Input 3rd number: '))
largest_number = "none"
smallest_number = "none"
all_equal = "none"
two_equal = "none"

#Task 1 - first version

# if (first_number >= second_number and first_number >= third_number):
#     largest_number = first_number
# elif (second_number >= first_number and second_number >= third_number):
#     largest_number = second_number
# elif (third_number >= first_number and third_number >= second_number):
#     largest_number = third_number

#Task 2 - second version-----------------------------------

# if (first_number >= second_number and first_number >= third_number):
#     largest_number = first_number
# elif (second_number >= first_number and second_number >= third_number):
#     largest_number = second_number
# elif (third_number >= first_number and third_number >= second_number):
#     largest_number = third_number

# if (first_number <= second_number and first_number <= third_number):
#     smallest_number = first_number
# elif (second_number <= first_number and second_number <= third_number):
#     smallest_number = second_number
# elif (third_number <= first_number and third_number <= second_number):
#     smallest_number = third_number

#Task 3 - third version-------------------------------
# equality checks
if (first_number == second_number and first_number == third_number):
    all_equal = "true"
elif (first_number == second_number and first_number != third_number):
    two_equal = first_number
elif (first_number == third_number and first_number != second_number):
    two_equal = first_number
elif (second_number == first_number and second_number != third_number):
    two_equal = second_number
elif (second_number == third_number and second_number != first_number):
    two_equal = second_number
elif (third_number == first_number and third_number != second_number):
    two_equal = third_number
elif (third_number == second_number and third_number != first_number):
    two_equal = third_number

# greatest number checks
if (first_number >= second_number and first_number >= third_number):
    largest_number = first_number
elif (second_number >= first_number and second_number >= third_number):
    largest_number = second_number
elif (third_number >= first_number and third_number >= second_number):
    largest_number = third_number

# smallest number checks
if (first_number <= second_number and first_number <= third_number):
    smallest_number = first_number
elif (second_number <= first_number and second_number <= third_number):
    smallest_number = second_number
elif (third_number <= first_number and third_number <= second_number):
    smallest_number = third_number

#Checker for all tasks --------------------------------------------------------
if (all_equal is "true"):
    print('All numbers are equal!')
elif (two_equal is not "none"):
    print('The largest number is', largest_number, 'and the smallest number is', smallest_number, ', and there are two', two_equal, 's!')
else:
    print('The largest number is', largest_number, 'and the smallest number is', smallest_number, '.')