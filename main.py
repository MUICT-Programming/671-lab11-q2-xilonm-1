n = int(input())
lst1 = []
for i in range(n):
    number = int(input())
    lst1.append(number)

lst2 = []
for i in range(n):
    number = int(input())
    lst2.append(number)

def summation(lst1, lst2):
     return [x + y for x, y in zip(lst1, lst2)]

def find_min_max(lst):
     return (min(lst), max(lst))

updated_list = summation(lst1, lst2)
print(updated_list)

print(find_min_max(updated_list))
