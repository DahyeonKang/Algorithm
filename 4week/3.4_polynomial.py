'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 3.4_polynomial.py
* 작성일 : 2021.09.29.Wed
* 프로그램 설명 : 수학과 과학에서 다항식은 매우 중요하게 사용된다. 다음 추상 자료형으로
정의된 다항식 클래스를 파이썬의 리스트를 이용해 구현하여라.
참고, 계수는 리스트에 저장하여라.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Polynomial:
    def __init__(self):
        self.coef = []
        # self.deg = len(self.coef) - 1

    def read_poly(self):
        n = int(input("다항식의 최고 차수를 입력하시오: "))
        for i in range(n, -1, -1):  # or reversed(range(1, n+1))
            self.coef.append(int(input("      x^%d의 계수 : " % i)))
        self.coef.reverse()

    def degree(self): return len(self.coef) - 1  # self.n을 하면 변수 c 경우는 self.n을 입력받지 않았기 때문에 오류 발생

    def evaluate(self, scalar):
        res = 0.0
        for index, c in enumerate(self.coef):
            res += c * (scalar ** index)
        return res

    def add(self, rhs):
        p = Polynomial()
        if len(self.coef) > len(rhs.coef):
            p.coef = self.coef.copy()  # or list(self.coef)
            for i in range(len(rhs.coef)):
                p.coef[i] += rhs.coef[i]
        else:
            p.coef = rhs.coef.copy()  # or list(rhs.coef)
            for i in range(len(self.coef)):
                p.coef[i] += self.coef[i]
        return p

    def subtract(self, rhs):
        s = Polynomial()
        if len(self.coef) > len(rhs.coef):
            s.coef = self.coef.copy()  # or list(self.coef)
            for i in range(len(rhs.coef)):
                s.coef[i] -= rhs.coef[i]
        else:
            s.coef = rhs.coef.copy()  # or list(rhs.coef)
            for i in range(len(self.coef)):
                s.coef[i] -= self.coef[i]
        return s

    def multiply(self, rhs):
        m = Polynomial()
        m.coef = [0] * (len(self.coef) + len(rhs.coef) + 1)
        for i in range(len(self.coef)):
            for j in range(len(rhs.coef)):
                m.coef[i + j] += self.coef[i] * rhs.coef[j]
        return m

    def display(self, msg):
        print(msg, end='')
        deg = self.degree()
        for index, c in zip(range(deg, -1, -1), reversed(self.coef)):
            if index == 0:
                print(" %.1f" % c)
                break
            print(" %.1f x^%d " % (c, index), end='+')


a = Polynomial()
b = Polynomial()
a.read_poly()
b.read_poly()
c = a.add(b)
a.display("  A(x) = ")
b.display("  B(x) = ")
c.display("  C(x) = ")
print("  C(2) = ", c.evaluate(2))


# 두 리스트 길이 같을 때 요소끼리의 덧셈
# a = [1, 2, 3]
# b = [2, 3, 4]
# print([x+y for x,y in zip(a, b)])
# print([a[i]+b[i] for i in range(len(a))])

