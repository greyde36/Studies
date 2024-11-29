# Параллельные вычисления

# Процессор в каждый момент времени выполняет только одну задачу (процесс) среди нескольких
# Это многозадачность - см. https://goo.gl/5sHFcM (не путать с многопоточностью!)
# Для пользователя все выглядит так, как будто все задачи выполняются одновременно - параллельно.
# Все достигается за счет гигантского быстродействия процессоров. Если уменьшить скорость в миллион раз,
# то станет видно, например, как поочередно отрисовываются окна приложений и мышка двигается рывками...
#
# Процессы с точки зрения ОС имеют разную память и разный стек (места вызова функций).
# Когда процессор переключается на другую задачу, то старая задача "замораживается" на время
# - сохраняется её область памяти и стек. Когда процессор решает вернуться к ней, то он восстанавливает
# память и стек процесса и начинает с того места, где остановился в прошлый раз.
# Процессы в операционной системе доступа к памяти друг друга не имеют, иначе все бы знали наши пароли.
#
# А что есть многопоточность? Потоки - это части одного ПРОЦЕССА (см. https://goo.gl/aDq4lc).
# Сам процесс изнутри организовал себя так, что может переключать контексты выполнения СВОЕГО кода.
# Процесс хранит информацию о потоках: место и контекст выполнения потока, какие объекты создал поток, и т.п.
# То есть процесс выступает в роли небольшой операционной системы для потоков.
# И когда процессор начинает выполнять ПРОЦЕСС, то этот процесс внутри себя приступает к переключению ПОТОКОВ.
# За счет того что процесс у потоков один, они все имеют доступ к памяти процесса.
#
# И начнем мы с потоков, они проще. Но это неточно...