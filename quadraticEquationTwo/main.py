import math

def solve(a, b, c):
    delta = b*b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2 * a)
        x2 = (-b - math.sqrt(delta))/(2 * a)
        return  x1, x2
    elif delta == 0:
        x = -(b/(2*a)) 
        return x

a = float(input('type a: '))
b = float(input('type b: '))
c = float(input('type c: '))

solution = solve(a, b, c)

if solution is not None:
    if len(solution) == 2:
        x1, x2 = solution
        print(f'x1= {x1}, x2= {x2}')
    else:
        x = solution
        print(f'x= {x}')
else:
    print('not x')