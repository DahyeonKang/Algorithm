items = []

def insert(pos, elem):
    items.insert(pos, elem)
def delete(pos): return items.pop(pos)
def getEntry(pos): return items[pos]
def isEmpty(): return len(items) == 0
def size(): return len(items)
def clear(): items=[]
def find(item): items.index(item)
def replace(pos, elem): items[pos] = elem
def sort(): items. sort()
def merge(lst): items.extend(lst)
def display(msg='ArrayList:'):
    print(msg, size(), items)

display('파이썬 리스트로 구현한 리스트 테스트')
insert(0,10); insert(0,20); insert(1,30)
insert(size(), 40); insert(2, 50)
display('파이썬 리스트로 구현한 List(삽입x5): ')
sort()
display('파이썬 리스트로 구현한 List(정렬후): ')
replace(2, 90)
display('파이썬 리스트로 구현한 List(교체x1): ')
delete(2); delete(size()-1); delete(0)
display('파이썬 리스트로 구현한 List(삭제x3): ')
lst = [1, 2, 3]
merge(lst)
display('파이썬 리스트로 구현한 List(병합): ')
clear()
display('파이썬 리스트로 구현한 List(정리후): ')