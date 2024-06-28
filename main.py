import pyperclip
from need_text import keys_themes
from need_text import search_words

def infoCommand2():
    n = 1
    for i in search_words.keys():
        print(n, i)
        n += 1

    '''1 информатика, 2 комп
       3 кодирование, 4 сети
       5 схд, 6 информационная безопасность
       7 ворд, 8 графика
       9 моделирование, 10 алгоритм
       11 бд, 12 матплотлиб
       13 ии, 14 маш обучение
       15 регрессия, 16 классификация
       17 деревья, 18 кластеризация'''

def toDo():
    while True:
        input1 = input("Выберите действие: ")
        if input1 == '1':
            find_num = input('Введите номер темы: ') #1, 2, 3, 5, 7, 8, 9, 10, 12, 14, 15, 16, 24, 25, 27, 28, 29, 30 - infoCommand1
            output1 = keys_themes[find_num.strip().lower()]
            pyperclip.copy(output1)
            print(output1)
        elif input1 == '2':
            find_word = input('Введите слово поиска: ')
            output1 = search_words[find_word.strip().lower()]
            pyperclip.copy(output1)
            print(output1)
        else:
            infoCommand2()


if __name__ == '__main__':
    while True:
        toDo()