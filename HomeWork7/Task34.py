# Винни-Пух попросил Вас посмотреть, есть ли в его 
# стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их 
# придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из
# одного слова, если во фразе несколько слов, то они
# разделяются дефисами. Фразы отделяются друг от друга
# пробелами. Стихотворение Винни-Пух вбивает в 
# программу с клавиатуры. В ответе напишите “Парам
# пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам


def count_vowels(phrase):
    vowels_letters = 'уеыаоэяиюё'
    count = 0
    for letter in phrase:
        if letter in vowels_letters:
            count += 1
    return count


def ritm(phrases):
    count0 = count_vowels(phrases[0])
    for phrase_i in phrases[1:]:
        count_i = count_vowels(phrase_i)
        if count0 != count_i:
            return 'Пам парам'
    return 'Парам пам-пам'

song = input('введие песню: ').split()
print(ritm(song))
