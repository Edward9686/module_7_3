import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Приводим строку к нижнему регистру
                        line = line.lower()
                        # Убираем пунктуацию
                        line = line.translate(str.maketrans('', '', string.punctuation + '—'))
                        # Разбиваем строку на слова
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден")
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            try:
                index = words.index(word) + 1  # в консоли выдаёт счёт с нуля, решил это вот так:)
                results[file_name] = index  # Позиция первого вхождения
            except ValueError:
                # Если слово не найдено, пропускаем
                pass
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                results[file_name] = count  # Количество вхождений
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
