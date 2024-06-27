class MyMath:
    def convert(radians):
        radians *= 12
        radians %= 24
        return radians
    

class degrees:
    def sin(x):
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

    def cos(x):
        x %= 360
        degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        cos_list = ['1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', 
                    '-1/2', '0', '1/2', '√2/2', '-3/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return cos_list[y]
    def tan(x):
        x %= 360
        degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        tan_list = ['0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3', '0', '√3/3', '1', 
                    '√3', 'undefined', '-√3', '-1', '-√3/3']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return tan_list[y]
    



class radians:


    def sin(x):
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
    

    def cos(x):
        x = MyMath.convert(x)
        degree_list = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        cos_list = ['1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', 
                    '-1/2', '0', '1/2', '√2/2', '-√3/2']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return cos_list[y]
    

    def tan(x):
        x = MyMath.convert(x)
        degree_list = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        tan_list = ['0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3', '0', '√3/3', '1', 
                    '√3', 'undefined', '-√3', '-1', '-√3/3']
        y = 0
        for i in range(len(degree_list)):
            if degree_list[y] == x:
                break
            y += 1
        return tan_list[y]


print(degrees.sin(30))