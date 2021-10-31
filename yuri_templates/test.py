STRING = '123,456,789'

def go_to_digits(one):

    res = []
    for i in one:
        if i.isdigit():
            res.append(i)
        elif i == ',':
            break
    number = float(''.join(map(str, res)))
    return number

def split_to_digits(s:str):
    return float(s.split(',',1)[0])

print(go_to_digits(STRING))
print(split_to_digits(STRING))
