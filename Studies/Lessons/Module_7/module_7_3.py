import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for name in self.file_name:
            with open(name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                text = text.split()
                all_words[name] = text
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_word[name] = words.index(word.lower()) + 1
        return find_word if find_word else {}

    def count(self, word):
        count_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_word[name] = words.count(word.lower())
        return count_word if count_word else {}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего