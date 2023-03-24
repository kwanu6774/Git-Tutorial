def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(r):
    area=3.14*r*r
    return area
    
num=get_radius('넓이를 구하고자 하는 원의 반지름은?')
num2=get_circle_area(num)
print('반지름 ',num,'인 원의 넓이 = 3.14 ',num, 'x ',num,' = ',num2)


