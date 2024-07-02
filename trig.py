degree_list = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
sin_list = ['0', '1/2', '√2/2', '√3/2', '1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', '-1/2']
cos_list = ['1', '√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1', '-√3/2', '-√2/2', '-1/2', '0', '1/2', '√2/2', '-√3/2']
tan_list = ['0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3', '0', '√3/3', '1', '√3', 'undefined', '-√3', '-1', '-√3/3']
csc_list = ['undefined', '2', '√2', '2√3/3', '1', '2√3/3', '√2', '2', 'undefined', '-2', '-√2', '-2√3/3', '-1', '-2√3/3', '-√2', '-2']
sec_list = ['1', '2√3/3', '√2', '2', 'undefined', '-2', '-√2', '-2√3/3', '-1', '-2√3/3', '-√2', '-2', 'undefined', '2', '√2', '-2√3/3']
cot_list = ['undefined', '√3', '1', '√3/3', '0', '-√3/3', '-1', '-√3', 'undefined', '√3', '1', '√3/3', '0', '-√3/3', '-1', '-√3']


class MyMath:
    def convert(radians):
        ##Converts radians to whole numbers
        ##Input radians always satisfies the unit circle
        ##Exclued π from input
        ##Radians are inputed in fraction form. EX: 1/6, 5/3
        radians *= 12
        radians %= 24
        return radians
    

class degrees:

    ##All trig functions have domains that satisfy the unit circle
    ##All degress are either multiples of 30 or 45 or it will not work
    ##Degrees may be greater than 360º

    def sin(x):
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)    
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the sin list
            if degree_list[i] == x:
                break #Once found, exit loop
        return sin_list[i] #Return response. If response is invalid, it will return none.

    def cos(x):  
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the cos list
            if degree_list[i] == x:
                break #Once found, exit loop
        return cos_list[i] #Return response. If response is invalid, it will return none.
    
    def tan(x):  
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)    
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the tan list
            if degree_list[i] == x:
                break #Once found, exit loop
        return tan_list[i] #Return response. If response is invalid, it will return none.
    
    def csc(x): 
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the csc list
            if degree_list[i] == x:
                break #Once found, exit loop
        return csc_list[i] #Return response. If response is invalid, it will return none.
    
    def sec(x): 
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)      
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the sec list
            if degree_list[i] == x:
                break #Once found, exit loop
        return sec_list[i] #Return response. If response is invalid, it will return none.
    
    def cot(x): 
        x %= 360 #Converts all degrees over 360º to the range of (0, 360)    
        for i in range(len(degree_list)): #For loop to check if the degree corresponds to the cot list
            if degree_list[i] == x:
                break #Once found, exit loop
        return cot_list[i] #Return response. If response is invalid, it will return none.

class radians:
    ##To convert degrees to radians use this formula: radians = degrees * π / 180
    ##Drop the π from your degrees. EX: π/4 -> 1/4
    ##Express the radians as a fraction as show above

    def sin(x): 
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the sin list
            if degree_list[i] == x:
                break #Once found, exit loop
        return sin_list[i] #Return response. If response is invalid, it will return none.
    

    def cos(x):
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the cos list
            if degree_list[i] == x:
                break #Once found, exit loop
        return cos_list[i] #Return response. If response is invalid, it will return none.
    

    def tan(x):
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the tan list
            if degree_list[i] == x:
                break #Once found, exit loop
        return tan_list[i] #Return response. If response is invalid, it will return none.
    
    def csc(x):
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the csc list
            if degree_list[i] == x:
                break #Once found, exit loop
        return csc_list[i] #Return response. If response is invalid, it will return none.

    def sec(x):
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the sec list
            if degree_list[i] == x:
                break #Once found, exit loop
        return sec_list[i] #Return response. If response is invalid, it will return none.
    
    def cot(x):
        x = MyMath.convert(x) #Convert fractions into whole numbers using common multipliers with the convert function
        for i in range(len(degree_list)): #For loop to check if the radian corresponds to the cot list
            if degree_list[i] == x:
                break #Once found, exit loop
        return cot_list[i] #Return response. If response is invalid, it will return none.

################################################################################################################################################################################


