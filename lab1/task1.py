import re

#ЗАДАНИЕ 1.1
# Чтение файла
with open ('/root/lab1/files/first_task.txt', 'r', encoding='utf-8') as file:
    text=file.read()

# Замена знаков препинания на пробел
text_new = (
    text.replace('.', '')
    .replace('?', '')
    .replace('!', '')
    .replace('\n', '')
    .lower().strip()
)

# Разделение на слова
words = text_new.split(' ')

# Подсчет повторяемости слов
word_list = {}
for word in words:
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1
word_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)

# Сохранение в файл
with open("/root/lab1/files/results/task1_1.txt", "w") as file:
        for key, value in word_list:
            file.write(f"{key}: {value}\n")

# ЗАДАНИЕ 1.2
# Подсчет количества слов
words_count = len(words)

# Подсчет количества предложений
sentences_count = len([sentence.strip() for sentence in re.split(r'[.?!\n]', text) if sentence.strip()])

# Среднее количество слов в предложении
avg_words = words_count/sentences_count

# Сохранение в файл
with open("/root/lab1/files/results/task1_2.txt", "w") as file:
            file.write(f"Среднее количество слов без округления: {avg_words}\n\
Среднее количество слов с округлением: {avg_words:.0f}")
