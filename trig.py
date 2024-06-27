class MyMath:
    def convert(radians):
        radians *= 12
        radians %= 24
        return radians
    
def sin(x, type):
    if type == 'degrees' or type == 'd' or type == 'degree' or type == 'Degrees' or type == 'Degree' or type == 'D':
        x %= 360
        degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        sin_list = ['0', '1/2', '√2/2', '√3/2', '1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', 
                    '-√3/2', '-1', '-√3/2', '-√2/2', '-1/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]
    else:
        x = MyMath.convert(x)
        degree_list = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        sin_list = ['0', '1/2', '√2/2', '√3/2', '1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', 
                    '-√3/2', '-1', '-√3/2', '-√2/2', '-1/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]

def cos(x, type):
    if type == 'degrees' or type == 'd' or type == 'degree' or type == 'Degrees' or type == 'Degree' or type == 'D':
        x %= 360
        degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        sin_list = ['1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', 
                    '-1/2', '0', '1/2', '√2/2', '-3/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]
    else:
        x = MyMath.convert(x)
        degree_list = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        sin_list = ['1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', 
                    '-1/2', '0', '1/2', '√2/2', '-√3/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]
def tan(x, type):
    if type == 'degrees' or type == 'd' or type == 'degree' or type == 'Degrees' or type == 'Degree' or type == 'D':
        x %= 360
        degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        sin_list = ['0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3', '0', '√3/3', '1', 
                    '√3', 'undefined', '-√3', '-1', '-√3/3']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]
    else:
        x = MyMath.convert(x)
        degree_list = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        sin_list = ['0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3', '0', '√3/3', '1', 
                    '√3', 'undefined', '-√3', '-1', '-√3/3']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return sin_list[y]
