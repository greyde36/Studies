immutable_var = (1,2.0,True,'4',[1,2,3])
print(immutable_var)
#immutable_var [1] = 5         #immutable_var [4][1] = 5
#Сам кортеж не изменяем, но внутри него могут быть изменяемые объекты
mutable_list = ['1','2','3','4','5']
mutable_list[1]='5'
mutable_list.remove('4')
mutable_list.append('6')
print(mutable_list)