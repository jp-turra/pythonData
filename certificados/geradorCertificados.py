import pandas as pd
# Pillow = biblioteca para lidar com o uso de imagens
# Precisou instala biblioteca xlrd para ler dados do excel
from PIL import Image, ImageDraw, ImageFont

# Lendo o arquivo excel
path = r'C:\Users\Cliente\Desktop\Engenharia Elétrica\PET\Cursos Técnicos\Curso Python 03.07.2020\Chamada_Relatorio\Lista_Presenca_Python.xlsx'
data = pd.read_excel(path)
#print(data)

# Importa a lista de nomes de um arquivo excel (Model Unico de lista de presença que o lolis enviou)
listName = data['Nome Completo do Participante '].tolist()
# Diminuindo o tamanho da lista pra testes
listAux = listName[0:3]
#tipoCurso = input("Qual o tipo de curso? ")
#nomeCurso = input("Qual curso você deseja certificar? ")

for i in listAux:
    image = Image.open(r'C:\Users\Cliente\Desktop\Engenharia Elétrica\PET\Cursos Técnicos\Curso Python 03.07.2020\certificado.jpeg')
    d = ImageDraw.Draw(image)
    #baseText = "Certificamos que\n"+i.upper()+"\nparticipou do curso "+tipoCurso+" intitulado(a) "+nomeCurso+" com duração de 6 horas.\nO programa detalhado se encotra no verso"
    baseText = i.upper()+"\n                                                                                                                                                                "
    # Posição na imagem, para achar pode-se usar o paint
    location = (0, 530)
    # Cor do texto
    text_color = (0, 0, 0)
    # Fonte e tamanho do texto
    font = ImageFont.truetype("Montserrat-Medium.ttf", 30)

    # Aplicando as alterações (posição, text, fill= cor do texto, font = fonte/tamanho)
    d.text(
        location,
        baseText,
        fill=text_color,
        font=font,
        align="center",
        stroke_width=1
    )

    # Salva as alterações como pdf
    # Os arquivos ficam salvos na mesma pasta em que o código está
    image.save("certificado_"+i+".pdf")
