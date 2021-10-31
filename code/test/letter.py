from fpdf import FPDF

txt = f'Ветер свистел, визжал, кряхтел и гудел на разные лады. То жалобным тоненьким голоском,' \
      f'то грубым басовым раскатом распевал он свою боевую песенку. Фонари чуть заметно мигали' \
      f'сквозь огромные белые хлопья снега, обильно сыпавшиеся на тротуары, на улицу, на экипажи,' \
      f'лошадей и прохожих. А я все шла и шла, все вперед и вперед. Нюрочка мне сказала:'
txt2 = f'Надо пройти сначала длинную большую улицу, на которой такие высокие дома и роскошные ' \
       f'магазины, потом повернуть направо, потом налево, потом опять направо и опять налево, ' \
       f'а там все прямо, прямо до самого конца - до нашего домика. Ты его сразу узнаешь. Он около' \
       f'самого кладбища, тут еще церковь белая и красивая такая. Я так и сделала. Шла все прямо, ' \
       f'как мне казалось, по длинной и широкой улице, но ни высоких домов, ни роскошных магазинов ' \
       f'я не видала. Все заслонила от моих глаз белая, как саван, живая рыхлая стена бесшумно ' \
       f'падающего огромными хлопьями снега. Я повернула направо, потом налево, потом опять направо, ' \
       f'исполняя все с точностью, как говорила мне Нюрочка, - и все шла, шла, шла без конца.'

fname = 'test.pdf'

ELEM_TYPES = ('Header', 'Text', 'Image', 'Box', 'Line', 'Barcode')


class PdfElements():
    def __init__(self):
        self.pdf_el = list()

    def add_element(self, el):
        mode, params, axes = el['mode'], el['params'], el.setdefault('axes', dict())
        if mode not in ELEM_TYPES:
            raise KeyError('Тип должен быть Header/Text/Image/Box/Line/Barcode')
        new_el = dict()
        new_el['mode'] = mode
        new_el['params'] = params
        new_el['axes'] = axes
        self.pdf_el.append(new_el)

def show_pdf(func):
    def wrapper(*args, **kwargs):
        pprint(kwargs[elements])
    return wrapper

@show_pdf
def make_pdf(filename=fname, elements=dict, margins={10, 20, 50}):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(*margins)
    # pdf.add_font('arial', 'Regular', 'Arial.ttf', uni=True)
    pdf.add_font('times_regular', '', 'Times New Roman Cyr Regular.ttf', uni=True)
    pdf.set_font('times_regular', size=14)
    t = 'Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований. Привет участникам соревнований.'
    pdf.multi_cell(190, 7, txt=t, align='J')
    # pdf.cell(190,6, txt=t, align='J')
    pdf.add_font('times_italic', '', 'Times New Roman Cyr Italic.ttf', uni=True)
    pdf.set_font('times_italic', size=14)
    pdf.multi_cell(190, 7, txt=t, align='J')
    pdf.set_font('times_regular', size=10)
    pdf.multi_cell(190, 5, txt=t, align='J')
    pdf.multi_cell(190, 5, txt=t, align='L')
    pdf.multi_cell(190, 5, txt=t, align='R')
    pdf.multi_cell(190, 5, txt=t, align='C')
    pdf.image(name='debipng.png', x=10, y=100, w=100)
    pdf.text(200, 100, txt=t)
    pdf.output(fname)


if __name__ == '__main__':

    elements = PdfElements()
    elements.add_element({'mode': 'Text',
                          'params': dict()})
    make_pdf(fname, elements)
