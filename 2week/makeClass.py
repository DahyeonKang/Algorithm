'''
* 프로그램명 : makeClass.py
* 작성자 : 2019015031 강다현
* 작성일 : 2021.09.15
*프로그램 설명 : Car 또는 SuperCar 클래스 작성하기
'''

class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed
    def speedUp(self): self.speed += 10
    def speedDown(self): self.speed -= 10
    def isEqual(self, carB):
        if self.color == carB.color:
            return True
        else:
            return False
    def __eq__(self, carB):
        return self.color == carB.color
    def __str__(self):
        return "color=%s, speed=%d" %(self.color, self.speed)

car1 = Car('black', 0)
car2 = Car('red', 120)
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')
car6 = Car('yellow', 30)

car2.speedDown()
car4.speedUp()

print('car2 == car6', car2.isEqual(car6))
print('car5 == car6', car5.isEqual(car6))

print('car2 == car6', car2 == car6)
print('car3 == car6', car3 == car6)

print('[car3]', car3)

class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo=True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo
    def setTurbo(self, bTurbo=True):
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
    def __str__(self):
        if self.bTurbo:
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)

s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)
