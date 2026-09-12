marks:str = str(input('Enter your marks: '))
print(type(marks))
marks = float(marks)
print(type(marks))
if marks > 100:
    print('outstanding')
elif marks >= 75:
    print('excellent')
elif marks>=50:
     print('pass')
else :
    print('fail')
