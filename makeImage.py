import sys
from PIL import Image, ImageFont, ImageDraw 


my_image = Image.open("template.png").convert("RGBA")
title_font = ImageFont.truetype('ED.TTF', 105)
title_text = sys.argv[1]



button_image = Image.new('RGBA', (1024,382), "white")
button_draw = ImageDraw.Draw(button_image)
button_draw = ImageDraw.Draw(button_image)
button_draw.text((1000, 382/2), "\"" + title_text + "\"", font=title_font, anchor="rm", fill="black")

my_image.paste(button_image, (881, 289))



my_image.save(sys.argv[2])
