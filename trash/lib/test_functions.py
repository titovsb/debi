import re

def num_to_str(num:float) -> str:
    dtranslate = {'1':{'сто', '', 'одиннадцать','', 'одна', ''},
                  '2':{'двести', 'двадцать', 'двенадцать','две', 'два'},
                  '3':{'триста', 'тридцать', 'тринадцать','три', 'три'},
                  '4':{'четыреста', 'сорок', 'четырнадцать','четыре', 'одна'},
                  '5':{'пятьсот', 'пятьдесят', 'пятнадцать','пять', 'пять'},
                  '6':{'шестьсот', 'шестьдесят', 'шестнадцать','шесть', 'шесть'},
                  '7':{'семьсот', 'семьдесят', 'семнадцать','семь', 'семь'},
                  '8':{'восемьсот', 'восемьдесят', 'восемнадцать','восемь', 'восемь'},
                  '9':{'девятьсот', 'девяносто', 'девятнадцать','девять', 'девять'},
                  '0':None}
    quart = {'0': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             '1': {'копейка','рубль','тысяча','миллион','миллиард'},
             '2': {'копейки', 'рубля', 'тысячи', 'миллиона', 'миллиарда'},
             '3': {'копейки', 'рубля', 'тысячи', 'миллиона', 'миллиарда'},
             '4': {'копейки', 'рубля', 'тысячи', 'миллиона', 'миллиарда'},
             '5': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             '6': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             '7': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             '8': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             '9': {'копеек', 'рублей', 'тысяч', 'миллионов', 'миллиардов'},
             }
    def translate_triade(digits) -> str:
        pass

    num = round(num,2)
    return translate_triade(num)



if __name__ == '__main__':
    # print(num_to_str())

    number = '12345678.12'
    fi = re.findall('(\d+)\.(\d{2})',str(number))
    print(fi)
    gross, small = fi[0]
    print(gross, small)
    l = list()
    for i in gross:
        print(, end='')
