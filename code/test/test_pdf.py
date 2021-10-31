from fpdf import Template

#this will define the ELEMENTS that will compose the template.
elements = [
    { 'name': 'company_logo', 'type': 'I', 'x1': 20.0, 'y1': 17.0, 'x2': 78.0, 'y2': 30.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },
    { 'name': 'company_name', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
    { 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 2, },
    { 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '200000000001000159053338016581200810081', 'priority': 3, },
]

#here we instantiate the template and define the HEADER
f = Template(format="A4", elements=elements,
             title="Demo")
f.add_page()
f.pdf.add_font('arial', '', 'Arial.ttf', uni=True)
f.pdf.set_font('arial', size=14)
#we FILL some of the fields of the template with the information we want
#note we access the elements treating the template instance as a "dict"
f["company_name"] = "Компания"
f["company_logo"] = "debipng.png"

#and now we render the page
f.render("template.pdf") # from fpdf import FPDF

#
# fname = 'test.pdf'
#
# pdf = FPDF()
# pdf.add_page()
# pdf.add_font('arial', '', 'Arial.ttf', uni=True)
# pdf.set_font('arial', size=14)
# pdf.cell(200,10, txt='Привет участникам соревнований', ln=1, align='J')
# pdf.output(fname)

# change_fonts.py

# from fpdf import FPDF
#
# def change_fonts():
#     pdf = FPDF()
#     pdf.add_page()
#     font_size = 8
#     for font in pdf.core_fonts:
#         if any([letter for letter in font if letter.isupper()]):
#             # пропускаем данный шрифт.
#             continue
#         pdf.set_font(font, size=font_size)
#         txt = "Font name: {} - {} pts".format(font, font_size)
#         pdf.cell(0, 10, txt=txt, ln=1, align="C")
#         font_size += 2
#
#     pdf.output("change_fonts.pdf")
#
# if __name__ == '__main__':
#     change_fonts()
