calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(word):
    count_calls()
    tuple = len(word), word.upper(), word.lower()
    return tuple


def is_contains(string, list_to_search):
    count_calls()
    if string.upper() in str(list_to_search[0:]).upper():
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)