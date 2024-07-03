import trig
import random




points = 0


while points != 10:

    degree_or_radian = random.randint(1, 2)

    degree_list = trig.degree_list
    base = random.randint(0, 2)
    degree = random.choice(degree_list) + base * 360
    base_r = random.randint(0, 2)
    base_r *= 2


    radians_list = [0, 1/6, 1/4, 1/3, 1/2, 
                    2/3, 3/4, 5/6, 1, 
                    7/6, 5/4, 4/3, 3/2, 
                    5/3, 7/4, 11/6]
    

    str_randians_list = [f'{base_r}π', f'{base_r * 6 + 1}π/6', f'{base_r * 4 + 1}π/4', f'{base_r * 3 + 1}π/3', f'{base_r * 2 + 1}π/2',
                         f'{base_r * 3 + 2}π/3', f'{base_r * 4 + 3}π/4', f'{base_r * 6 + 5}π/6', f'{base_r + 1}π', 
                         f'{base_r * 6 + 7}π/6', f'{base_r * 4 + 5}π/4', f'{base_r * 3 + 4}π/3', f'{base_r * 2 + 3}π/2', 
                         f'{base_r * 3 + 5}π/3', f'{base_r * 4 + 7}π/4', f'{base_r * 6 + 11}π/6']
    
    decider = random.randint(0, 15)

    radian = radians_list[decider]
    str_randian = str_randians_list[decider]








    if degree_or_radian == 1:
        operator_list = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']
        solve_list = [trig.degrees.sin(degree), trig.degrees.cos(degree), trig.degrees.tan(degree), trig.degrees.csc(degree), trig.degrees.sec(degree), trig.degrees.cot(degree)]
        deciding_int = random.randint(0, 5)
        print('')
        print('')

        x = str(input(f'What is {operator_list[deciding_int]} {degree}º: '))

        if x == solve_list[deciding_int]:
            print('')
            print('Correct!')
            points += 1
            print('')
            print('')
        else:
            print('')
            print('Wrong!')
            print('')
            print(f'Answer is: {solve_list[deciding_int]}')
            points = 0
            print('')
            print('')

    if degree_or_radian == 2:
        operator_list = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']
        solve_list = [trig.radians.sin(radian), trig.radians.cos(radian), trig.radians.tan(radian), trig.radians.csc(radian), trig.radians.sec(radian), trig.radians.cot(radian)]
        deciding_int = random.randint(0, 5)
        print('')
        print('')

        x = str(input(f'What is {operator_list[deciding_int]} {str_randian}: '))

        if x == solve_list[deciding_int]:
            print('')
            print('Correct!')
            points += 1
            print('')
            print('')
        else:
            print('')
            print('Wrong!')
            print('')
            print(f'Answer is: {solve_list[deciding_int]}')
            points = 0
            print('')
            print('')
