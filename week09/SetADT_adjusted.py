'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : SetADT_adjusted.py
* 작성일 : 2021.11.03.Wed
* 프로그램 설명 : 3장에서 구현한 집합 자료구조 수정하기 (참고 : 집합의 원소들을 항상 
정렬된 순으로 저장되고, 삽입 연산은 더 복잡해진다.)
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

    def insert(self, elem):  ## 수정
        if elem in self.items:  # 집합에 원소를 삽입할 때는 이미 항목이 존재하면 삽입하면 안됌
            return
        for idx in range(len(self.items)):
            if elem < self.items[idx]:  # 삽입할 위치 인덱스(idx) 찾음
                self.items.insert(idx, elem)  # 찾은 위치에 항목 삽입
                return
        self.items.append(elem)  # 맨 뒤에 삽입

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):  ## 수정
        newSet = Set()  # 반환할 합집합 생성
        a = 0  # self의 원소에 대한 인덱스
        b = 0  # setB의 원소에 대한 인덱스

        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]  # self의 현재 원소
            valueB = setB.items[b]  # setB의 현재 원소
            if valueA < valueB:  # self의 원소가 더 작으면
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB:  # setB의 원소가 더 작으면
                newSet.items.append(valueB)
                b += 1
            else:  # 중복되는 원소
                newSet.items.append(valueA)
                a += 1
                b += 1
        while a < len(self.items):  # self에 남은 원소를 모두 추가
            newSet.items.append(self.items[a])
            a += 1
        while b < len(setB.items):  # setB에 남은 원소를 모두 추가
            newSet.items.append(setB.items[b])
            b += 1
        return newSet

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

    def __eq__(self, setB):  ## 수정; 두 집합이 같은지 비교하는 함수
        if self.size() != setB.size():  # 비교하려면 원소의 개수가 같아야 함
            return False
        for idx in range(len(self.items)):  # loop - n번
            if self.items[idx] != setB.items[idx]:  # 원소별로 같은지 검사해서 다르면
                return False  # 다르면 False 반환
        return True  # 같으면 True 반환
