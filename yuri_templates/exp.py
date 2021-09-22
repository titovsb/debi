from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime, timedelta
import requests
import csv
import tkinter.ttk as ttk
import time


current_date = datetime.now().date()
two_weeks_time = current_date + timedelta(days=14)
prosrochka = two_weeks_time - current_date
one = str(prosrochka)
only_days_of_prosrochka = int(one.split()[0])

def go_to_digits(one):

    res = []
    for i in one:
        if i.isdigit():
            res.append(i)
        elif i == ',':
            break
    number = float(''.join(map(str, res)))
    return number

def clicked():

    file = filedialog.askopenfilename()
    entry.insert(0, f'{file}')


def one_get():
    entry_get = entry.get()
    res = []
    with open(f'{entry_get}', encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            res.append(row)

    master = Tk()
    master.geometry('400x150')
    progress_bar = ttk.Progressbar(master, length=200, orient="horizontal", mode="determinate", maximum=100, value=0)

    label_1 = Label(master, text="Progress Bar")

    label_1.grid(row=0, column=0)
    progress_bar.grid(row=0, column=1)

    progress_bar['value'] = 0
    master.update()

    for i in range(len(res) - 1):
        progress_bar['value'] = (i + 1) / int(len(res) - 1) * 100




        res_number = go_to_digits(res[i + 1][1])

        two = {'req': res[i + 1][2], 'key': '78526161ffc0c65c7417aca4437515396f6de5c3'}
        one_one = requests.get('https://api-fns.ru/api/multinfo', params=two)
        otvet = one_one.json()['items']

        def dict_filter(one):

            res = []

            for key in list(one[0]['ЮЛ'].keys()):
                if key == 'Адрес':
                    res.append(one[0]['ЮЛ'][key])

            for key in list(res[0].keys()):
                if key == 'КодРегион':
                    del res[0][key]

            result = list(res[0].values())
            result.append(one[0]['ЮЛ']['ИНН'])
            result.append(one[0]['ЮЛ']['НаимСокрЮЛ'])

            return result

        two = dict_filter(otvet)

        d = datetime.now().date()

        text = [f'{two[3]}, \n'
                f'{two[2]}, \n'
                f'{two[1]}, \n'
                f'{two[0]}, \n'
                f'\n'
                f'{d}, \n'
                f'\n'
                f'ДОСУДЕБНАЯ ПРЕТЕНЗИЯ\n'
                f'\n'
                f'Настоящим, сообщаем Вам, о наличии за Вашей организацией задолженности перед ООО «БДА Капитал», \n'
                f'возникшей по: {res[1][0]}. Размер задолженности составляет {res_number} рублей. Согласно положениям ст. 309, 310, 314 \n'
                f'Гражданского кодекса Российской Федерации обязательства сторон договорных правоотношений \n'
                f'должны исполняться надлежащим образом в соответствии с требованиями законодательства и условиями договора. \n' \
                f'Обязательство должно исполняться точно в срок, в соответствии с договором. При этом, российским законодательством не допускается \n'
                f'односторонний отказ от исполнения обязательства, а также изменение его условий в одностороннем порядке. Предлагаем Вам в добровольном порядке \n'
                f'в срок до {two_weeks_time} года погасить возникшую задолженность в полном объеме в сумме {res[1][1]} рублей. В случае неисполнения Ваших обязательств \n'
                f'в выше обозначенный срок, при отсутствии конструктивных предложений с Вашей стороны по урегулировании ситуации, мы будем вынуждены обратиться \n'
                f'в арбитражный суд о взыскании задолженности в принудительном порядке. В этом случае сумма Вашей задолженности будет увеличена на сумму госпошлины – \n'
                f'{(res_number * 0.16 / 100 * 365) + res_number / 10} рублей, сумму процентов за пользование коммерческим кредитом согласно п. 4.9 – {res_number * 0.16 / 100 * 365} рублей. Итоговая сумма, подлежащая уплате через суд\n'
                f'на {two_weeks_time}, может составить более {(res_number * 0.16 / 100 * only_days_of_prosrochka) + res_number} рублей. Настоятельно рекомендуем принять участие в мирном урегулировании данного процесса, \n'
                f'что позволит обеим сторонам сэкономить время и деньги, а также создаст предпосылки для дальнейшего плодотворного сотрудничества наших компаний \n'
                f'\n'
                f'генеральный директор______________________________________ Ю.А.Кормилов']
        f = open(f'C:\\Users\\Валентина\\Desktop\\претензии\\{two[2]}.txt', 'w')
        f.write(text[0])
        master.update()
        time.sleep(1)
    master.destroy()
    messagebox.showinfo('Внимание!', 'обработка претензий завершена')






window = Tk()
window.title("Добро пожаловать в приложение искbit")
window.geometry('700x350')


dokkod = PhotoImage(file='C:\\Users\\Валентина\\Desktop\\проект\\icon.png')
panel = Label(window, image=dokkod)
panel.grid(column=0, row=0)
label = Label(window, text="Загрузите файл", font=("Arial Bold", 12))
label.grid(column=0, row=1)
entry = Entry(window, width=60)
entry.grid(column=1, row=1)

btn_1 = Button(window, text="обзор", width=20, command=clicked).grid(column=2, row=1)

btn_2 = Button(window, text="пуск", width=20, command=one_get).grid(column=2, row=2)


window.mainloop()