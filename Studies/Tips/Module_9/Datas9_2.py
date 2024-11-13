# пример 1 - как выглядит объединение функций map и filter
def by_3(x):
    return x*3
def is_odd(x):
    return x%2
my_numbers=[3,1,4,1,5,9,2,6]
result=map(by_3,filter(is_odd,my_numbers))
print(list(result))
print('#####################пример 2############################')
list_comp_1=[x*2 for x in range(1,6)]
print(list_comp_1)
print('#################################################')
# пример 2 - списковая сборка (аналог map)
my_numbers=[3,1,4,1,5,9,2,6]
result1=[x*3 for x in my_numbers]
print(result1)
print('#####################пример 3############################')
list_comp_2=[x*2 for x in range(1,11) if x>5]
print(list_comp_2)
print('#################################################')
# пример 3 - списковая сборка с if (аналог filter)
my_numbers=[3,1,4,1,5,9,2,6]
result2=[x*3 for x in my_numbers if x>5]
print(result2)
print('#####################пример 4############################')
list_comp_3=[x*2 if x>2 else x*10 for x in range(1,11)]
print(list_comp_3)
print('#################################################')
# пример 4 - условия перед циклом (для того чтобы не отфильтровывать данные, а поменять операцию над ними)
my_numbers=["A",1,4,"B",5,"C",2,6]
result3=[x if type(x)==str else x*5 for x in my_numbers]
print(result3)
print('#####################пример 5############################')
list_comp_4=[x*y for x in range(1,11) for y in range(1,5)]
print(list_comp_4)
print('#################################################')
# пример 5 - можно делать вложенные циклы
my_numbers=[3,1,4,1,5,9,2,6]
they_numbers=[2,7,1,8,2,8,1,8]
result4=[x*y for x in my_numbers for y in they_numbers]
print(result4)
result4=[x*y for x in my_numbers for y in they_numbers if x%2]
print(result4)
result4=[x*y for x in my_numbers for y in they_numbers if x%2 and y//2]
print(result4)
print('#################################################')
# пример 6 - можно создавать на лету множества и словари
my_numbers=[3,1,4,1,5,9,2,6]
result5= {x for x in my_numbers}
print(result5)

they_numbers=[2,7,1,8,2,8,1,8]
result6= {x: x**2 for x in my_numbers}
print(result6)