#In conditinal logic all functions that are set with variables take different actions 
#based on different purposes that the User may have.

if price >= 1.00:
    tax = .07
    print (tax)
else:
    tax = 0
    print (tax)

#Symbol and the Operation
# > - Greater than
# < - Less than
# >= - Greater than or Equal to
# <= - Less than or Equal to
# == - Is equal to
# != - Not Equal to


#When comparing strings ensure you have acknowledges the Upper and Lower case variables within the functions
#If statements are very sensitive about Upper and Lower variables hence why you should specify which you'll use

country = 'CANADA'
if country.lower == 'Canada' :
    print ('Oh look a Canadian ')
else: 
    print ('Well you are not a canadian')


print (' The new country that allows the ')

#Multiple Conditions
# If multiple values cause the same output you can combine them by listing all 
# values you want to check for with the in operator
province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
	tax = 0.05
elif province == 'Nunavut':
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)


# If I enter 2.00 I should see the message "Tax rate is: 0.07" 
# If I enter 1.00 I should see the message "Tax rate is: 0.07" 
# If I enter 0.50 I should see the message "Tax rate is: 0" 
price = input('how much did you pay? ')

tax = 0

if price > 1.00:
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
    print('Tax rate is:' str(tax))
	tax = 0

print('Tax rate is: ' + str(tax))


price = 5.0
if price >= 1.00:
	tax = .07
else:
	tax = 0

print (tax)


#Multiple Conditions #2
# If their first name starts with A or B
# tell them they go to room AB 
# If their first name starts with another letter, ask for their last name
# If their last name starts with Z, tell them to go to room Z
first_letter = name[0:1]
if first_letter.upper() in ('A','B'):
    room = 'AB'
# If their first name starts with C
# tell them to go to room C
elif first_letter.upper() == 'C':
    room = 'C'
else:
    
    last_name = input('what is your last name? ')
    last_name_first_letter = last_name[0:1]
    # if their last name starts with any other letter, tell them to go to room OTHER
    if last_name_first_letter == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room ' + room)