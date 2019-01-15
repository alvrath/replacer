# -*- coding: utf-8 -*-
import re
#набор символов для замены
symb_dict = {
        'Ё':'Ә',
        'ё':'ә',
        'Ї':'Ө',
        'ї':'ө',
        'Є':'Ү',
        'є':'ү',
        '>>':'Ӊ',
        '»':'ӊ',
        '‰':'Җ',
        'ў':'җ',
        'і':'h',
        'І':'h',
        #убираем неадекватное деление на абзацы
        '-\n':'',
        '\.\n':'.КОНЕЦ_АБЗАЦА.',
        '\n':' ',
        '.КОНЕЦ_АБЗАЦА.':'.\n',     
        }

#превращаем словарь с набором символов в два списка символов
orig_sym = list(symb_dict.keys())
repl_sym = list(symb_dict.values())

#вычисляем количество элементов в словаре символов (для цикла замены)
number_of_symbols = len(symb_dict)

#открываем файл, считываем и делаем преобразования
with open ('text.txt',  encoding='utf-8') as f:
        the_text = f.read ()        
        #цикл замены символов через регулярные выражения
        for i in range (number_of_symbols):
                the_text = re.sub(orig_sym[i], repl_sym[i], the_text)
                

#the_text = re.sub('\n', ' ', the_text)
#the_text = re.sub('.КОНЕЦ_АБЗАЦА.', '.\n', the_text)

#открываем файл снова, теперь уже для записи нашего преобразованного текста
with open ('text.txt', 'w', encoding='utf-8') as f:
		f.write(the_text)
print ('ВСЁ ОК. ВАШ ФАЙЛ ПРЕОБРАЗОВАН.')
