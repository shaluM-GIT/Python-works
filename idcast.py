age = input('Enter your age: ')
print(type(age))
age=int(age)
print(type(age))
retirement_age=60
years_to_work = retirement_age-age
if years_to_work > 0 :
    print(f'you will retire in {years_to_work}years')
else:
    print('you are eligible for retirement')
