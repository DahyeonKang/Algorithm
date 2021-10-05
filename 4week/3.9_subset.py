'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 3.9_subset.py
* 작성일 : 2021.09.29.Wed
* 프로그램 설명 : 두 집합 A와 B가 있을 때, A=B인 경우A는 B의 부분집합이 된다. A가 B의 부분
집합인 경우A가 같지 않은 경우, A는 B의 진 부분집합이다. 어떤 집합이 다른 집합의 
진부분집합인지 검사하는 메소를 3.6절 Set절에 추가하라. 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        return item in self.items

    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)

    def insertAll(self, elems):
        self.items.extend(elems)
        # set(self.items)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC

    def subset1(self, lst):
        sA = set(self.items)
        sB = set(lst.items)
        if sA != sB:
            if sA == sA.intersection(sB):
                print("첫번째가 두번째의 부분집합입니다.")
            elif sB == sB.intersection(sA):
                print("두번째는 첫번째의 부분집합입니다.")
            else:
                print("서로 부분집합이 아닙니다.")
        else:
            print("부분집합은 맞으나, 진부분집합이 아닙니다.")

    def subset2(self, lst):
        sA = set(self.items)
        sB = set(lst.items)
        if sA != sB:
            if sA.issubset(sB):
                print("첫번째가 두번째의 진부분집합입니다.")
            elif sA.issuperset(sB):
                print("두번째는 첫번째의 진부분집합입니다.")
            else:
                print("서로 부분집합이 아닙니다.")
        else:
            print("부분집합은 맞으나, 진부분집합이 아닙니다.")

    def subset3(self, lst):
        sA = set(self.items)
        sB = set(lst.items)
        if sB > sA:
            print("첫번째가 두번째의 진부분집합입니다.")
        elif sA > sB:
            print("두번째는 첫번째의 진부분집합입니다.")
        elif sA == sB:
            print("부분집합은 맞으나, 진부분집합이 아닙니다.")
        else:
            print("서로 진부분집합이 아닙니다.")


A = Set(); B = Set(); C = Set(); D = Set(); E = Set()
A.insertAll([1, 2, 3, 4, 5, 6, 7]); B.insertAll([2, 5, 10]); C.insertAll([1, 3, 6])
D.insertAll([1, 2, 3, 4, 5, 6, 7, 8, 9]); E.insertAll([1, 2, 3, 4, 5, 6, 7])

A.subset1(B)
A.subset1(C)
A.subset1(D)
A.subset1(E)
print("\n")
A.subset2(B)
A.subset2(C)
A.subset2(D)
A.subset2(E)
print("\n")
A.subset3(B)
A.subset3(C)
A.subset3(D)
A.subset3(E)