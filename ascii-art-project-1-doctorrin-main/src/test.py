from symbols_list import symbols_datas

# def get_symbol_datas(filename):


stop = 10
start = 1
line_start = 2
for symbol, symbol_datas in symbols_datas.items():
    # print(symbol, symbol_datas)
    symbol_datas['start'] = line_start
    print(symbol, symbol_datas)
    start +=1
    line_start += 9
    # if start == stop:
    #     break

# Записываем словарь в файл
with open('symbols.py', 'w', encoding='utf-8') as file:
    file.write("symbols_datas = " + repr(symbols_datas))


files = {'standart.txt', 'shadow,txt', 'thinkertoy.txt'}


# Порядок действий
# функция для каждого файла - передаем в нее название файла и наш дикшинари

# Передаем наш объект данных и файл
# Есть словарь с названиями файлов и соответствием поля в символах
# Читаем файл (есть ли файл)
# Символы в файле разделены пустой строкой
# Начиная с первой строки - перенос(пустая строка)
# далее следующие 8 строк - это символ. 
# В этих восьми строках берем их длину и записываем в соответствующее поле
# В поле start пишем номер строки, с которой начинается символ

# Если поле start заполнено, мы сразу обращаемся к нужной строке и далее проверяем длину и ширину символа

# После всего надо сохранить объект в файл


# Для того, чтобы распечатать на экране
# Вводим строку
# каждый символ обрабатываем отдельно
# создаем объект:
# В принципе, ширина и не нужна же
# Нужна только высота и старт строки
# как будем печатать:
# передавать номер строки - вывод ее на экран и сразу следующую строку
# переход на новую 