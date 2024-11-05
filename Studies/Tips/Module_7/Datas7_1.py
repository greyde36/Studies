a='hello' # ASCII
chars=[]
for i in a:
    chars.append(ord(i))        # Переводит символы в бинарный код
print(chars)
s= ''
for i in chars:
    s+=chr(i)                   # Переводит бинарный код обратно в символы
print(s)
print(hex(ord('h')))            # Перевод символа в 16-ричный код
bb= b'\x68'
print(type(bb))
print(bb.decode())              # Перевод из 16 в символ