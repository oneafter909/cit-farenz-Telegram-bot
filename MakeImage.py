from posixpath import split
import sys
import random
from PIL import Image, ImageFont, ImageDraw 
immagini = ["templateAngolare.png", "templateAngolareDue.png", "templateAngolareTre.png"]

my_image = Image.open(random.choice(immagini)).convert("RGBA")
font_size = 105
title_font = ImageFont.truetype('ED.TTF', font_size)
title_text = sys.argv[1]
textRectangle_width = 1965
textRectangle_height = 1217
def text_wrap(text, font, max_width):
        lines = []
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            words = text.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

button_image = Image.new('RGBA', (textRectangle_width, textRectangle_height), "white") #sfondo
button_draw = ImageDraw.Draw(button_image)
# put text on image
size_width, size_height = button_draw.textsize(title_text, title_font)
#print(str(size_width) + " " + str(size_height))
testo = text_wrap(title_text, title_font, 940)
citMarco = "\n- Marco Farina"
testoFinale = "\""+"\n".join(testo)+"\""
edit_width, edit_height = button_draw.textsize(testoFinale, title_font)
if(edit_height <= 1000):
    button_draw.text((1000, textRectangle_height/2), testoFinale + citMarco, font=title_font, anchor="rm", fill="black", align='right')
else:
    #OUT OF BOX
    button_draw.text((1000, textRectangle_height/2), "Inserisci testi corti.", font=title_font, anchor="rm", fill="black", align='right')

my_image.paste(button_image, (881, 0))
my_image.save(sys.argv[2])

