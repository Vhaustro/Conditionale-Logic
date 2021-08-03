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


    