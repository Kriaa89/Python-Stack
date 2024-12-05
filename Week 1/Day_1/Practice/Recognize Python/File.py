num1 = 42 #variable declaration inialize number
num2 = 2.3 #variable declaration inialaze float
boolean = True #variable declaration inialaze boolian
string = 'Hello World' #variable declaration inialaze string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration inialaze list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration inialaze dionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration inialaze tuple
print(type(fruit))
print(pizza_toppings[1]) #log value 'peperonie'
pizza_toppings.append('Mushrooms') #tuple addvalue
print(person['name']) #log value 'jhon'
person['name'] = 'George' #dictionary change value 
person['eye_color'] = 'blue' #dictionary change value 
print(fruit[2]) #log value "strawberry"

if num1 > 45: #conditional if 
    print("It's greater") #log statement "it s grater"
else: #conditional else
    print("It's lower") #log statement "its lower"

if len(string) < 5: #conditional if
    print("It's a short word!") #log statment "it s a short word!"
elif len(string) > 15: #conditional elif
    print("It's a long word!") #log statment "It's a long word!"
else: #conditional else
    print("Just right!") #log statment "Just right!"

for x in range(5): #for loop start 0 break 5 increment 1
    print(x) #log value x
for x in range(2,5): #for loop start 2 break 5 increment 1
    print(x) #log value x
for x in range(2,10,3): #for loop start 2 break 10 increment 3
    print(x) #log value x
x = 0 #variable declaration initialise number
while(x < 5): #conditional while loop start 0 break 5
    print(x) #log value x
    x += 1 #variable add 1

pizza_toppings.pop() #list delete value 'olives'
pizza_toppings.pop(1) #list delete value 'sausage'

print(person) #log dictionatry person
person.pop('eye_color') #dicionatry delete value 'eye color' : blue
print(person)

for topping in pizza_toppings: #for loop start 'peperonie' break 'cheese'
    if topping == 'Pepperoni': #conditional if 
        continue #conditional if continue
    print('After 1st if statement') #log statement "after  1st staement"
    if topping == 'Olives': #conditional if 
        break #conditional if break

def print_hello_ten_times(): #function argument no parameters no return
    for num in range(10): #for loop start 0 stop 10 increment 1
        print('Hello') #log statement "hello"

print_hello_ten_times() #function argument no params no return

def print_hello_x_times(x): #function argument 1 param no return
    for num in range(x): #for loop start 0 break x increment 1
        print('Hello') #log statement "hello"

print_hello_x_times(4) #function argument 1 param no return

def print_hello_x_or_ten_times(x = 10): #function argument 1 param default value 10 no return
    for num in range(x): #for loop start 0 break x incremant 1
        print('Hello') #log statement "hello"
 
print_hello_x_or_ten_times()  #function argument no param no return log statemnt "hello" 10 times
print_hello_x_or_ten_times(4) #function argument 1 param no return log statemnt "hello" 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)