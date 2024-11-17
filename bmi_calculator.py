# BMI calculator

weight = float(input('What is your weight (kg): '))
height = float(input('What is your height (m): '))

BMI = weight / (height ** 2)

print('Your BMI is', str(BMI))


if BMI >= 35:
    print('Heavily Overweight')
elif 30 <= BMI < 35:
    print('Middle Overweight')
elif 27 <= BMI < 30:
    print('Slightly Overweight')
elif 24 <= BMI < 27:
    print('Overweight')
elif 18.5 <= BMI < 24:
    print('Normal')
elif BMI < 18.5:
    print('Underweight')

print('Exit BMI calculator')


