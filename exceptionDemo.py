# This is a demo for error handling
try:
    age = int(input('Age: '))
    income = 10000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')