#Countdown
def countdown(num):
#create an empty list to store the countdwon
    countdown_list = []
# start from the given number and go down to 0
    for i in range(num, -1, - 1):
        countdown_list.append(i)
    return countdown_list
print(countdown(5))

# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

# First Plus Length 
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1, 2, 3, 4])) 

#Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
# store the second value in the list 
    second_value = list[1]
# create a empty list for the values greater than the second 
    new_list = [] 
    for value in list:
        if value > second_value:
            new_list.append(value)
    print(len(new_list))
    return new_list

# This Length, That Value
def length_value(size, value):
    return [value] * size