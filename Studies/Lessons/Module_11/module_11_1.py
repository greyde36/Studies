import requests
response = requests.get('https://www.google.com')
print(response.text)
# возвращает HTML код страницы
print('#############################################################')
import numpy as np
a = np.array([1, 2, 3])
b = a + 1
print(b)
# создание массива (аналог for?)
print('#############################################################')
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()
# рисует и показывает графики