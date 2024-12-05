# Basic - Print all integers from 0 to 150
for i in range (0, 150):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range (5, 1000, 5):
    print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range(1, 101):
    if i % 10 == 0: 
        print("coding")
    elif i % 5 == 0: 
        print("Coding Dojo")
    else:
        print(i)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
for i in range(2018, 0, -4):
    print(i)
#Flexible Counter
lowNum = 2 #starting number
heighNum = 9 #Ending number
mult = 3 # multiple to check
# loop through numbers from lowNum to heighNum 
for i in range(lowNum, heighNum, mult):
    if i % mult == 0:
        print(i)
