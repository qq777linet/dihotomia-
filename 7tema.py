
'''вариант 17 Полотнянко'''


a = float(input('a: '))
b = float(input('b: '))     
eps = float(input('eps: ')) 

def funct(x):
    return(x**3 + 5*x + 11) 

def dihotomia(a, b, eps):    
    if funct(a) * funct(b) > 0:
        return 0, 0
    else:
        c = 0
        i = 0
        while abs(b - a) > 2 * eps:
            c = (a + b) / 2
            if funct(a) * funct(c) < 0:
                b = c
            else:
                a = c
            i += 1
        return c, i
print(dihotomia(a, b, eps))



