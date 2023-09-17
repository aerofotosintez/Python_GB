#Скрабл

import re
def scrabble(text):
    return bool(re.search('[а-яА-Я]', text))
letter_en = {1: 'AEIOLNSTR', 
             2: 'DG', 
             3: 'BCMP', 
             4: 'FHVWY', 
             5: 'K', 
             8: 'JX', 
             10: 'QZ'}
letter_ru = {1: 'АВЕИНОРСТ', 
             2: 'ДКЛМПУ', 
             3: 'БГЁЬЯ', 
             4: 'ЙЫ', 
             5: 'ЖЗХЦЧ', 
             8: 'ШЭЮ',
             10: 'ФЩЪ'}
text = input().upper()
if scrabble(text):
    print(sum([k for i in text for k, v in letter_ru.items() if i in v]))
else:
    print(sum([k for i in text for k, v in letter_en.items() if i in v]))
