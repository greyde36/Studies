import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a/b                                                 # перехват ошибки до выполнения
        logging.info(f"Successful divide {a}/{b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error("HA 0 HE DELI!!!", exc_info=True)
        return "На ноль делить нельзя!"

def sub(a, b):
    return a - b

'''def add(a, b):
    return a**2 + b**2
'''

if __name__ == "__main__":
    # level - откуда берём лог, filemode - как открываем лог (запись, чтение...),
    # filename - название файла, format - вид по которому будет оформлен лог
    # asctime - время обращения, levelname - какого уровня сообщение, message - описание ошибки
    logging.basicConfig(level=logging.INFO, filemode="w", filename="py.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")

    print(div(3,4))
    print(div(3,0))

# Есть 5 уровней(видов) логов
# Logging.debug("комментарий")
# Logging.info("комментарий")
# Logging.warning("комментарий")
# Logging.error("комментарий")
# Logging.critical("комментарий")