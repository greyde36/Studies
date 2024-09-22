def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(a='snow', b=False, c=17)
print_params(b=25)
print_params(c=[1, 2, 3])
##############################################################
values_list = [5, True, 'snow']
values_dict = {'a': 17, 'b': 'September', 'c': False}
def print_params(*args, **kwargs):
    print(args)
    print(kwargs)
print_params(*values_list, **values_dict)
##############################################################
values_list_2 = [54.32,'Строка']
print_params(*values_list_2, 42, **values_dict)
##############################################################
list_my=[]
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)    # Значение добавляется в список и действует только внутри функции
print(list_my)
print(append_to_list(5))