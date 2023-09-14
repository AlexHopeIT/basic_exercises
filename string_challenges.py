# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
counter = 0
for i in word:
    if i in 'УЕЫАОЭЯИЮуеыаоэяию':
        counter += 1
print(f'Количество гласных букв в данном слове: {counter}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print('Количество слов в предложении "Мы приехали в гости":', len(sentence))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for i in sentence:
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
length_words = 0
for i in sentence:
    length_words += len(i)
arg_len = length_words / len(sentence)
print("Ответ:", arg_len)