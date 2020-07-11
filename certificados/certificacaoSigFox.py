import pandas as pd
from PIL import Image, ImageFont, ImageDraw

path = r'C:\Users\Cliente\Desktop\Engenharia Elétrica\PET\Cursos Técnicos\Palestra SigFox\nomes_sigfox.csv'
data = pd.read_csv(path)
# print(data)

names_list = data['NOMES'].tolist()
# print(names_list)
espaco10 = '          '
bugCenter = "\n"
bugCenter += 13*espaco10
for i in names_list:
    im = Image.open(r'C:\Users\Cliente\Desktop\Engenharia Elétrica\PET\Cursos Técnicos\Palestra SigFox\sigfox.png')
    d = ImageDraw.Draw(im)

    baseText = i.upper() + bugCenter

    location = (0, 1500) # 1754X1540
    text_color = (0, 0, 0)
    font = ImageFont.truetype("Montserrat-Medium.ttf", 100)

    d.text(
        location,
        baseText,
        fill=text_color,
        font=font,
        align="center",
        stroke_width=1
    )
    im.save("certificado_" + i + ".pdf")
