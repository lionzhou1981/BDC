from PIL import Image, ImageDraw, ImageFont

word = "[ˈnæʃnəl]"
img = Image.new('1', (250, 122), 255)
font = ImageFont.truetype('pics/symbol.ttf', 20)
textsize = font.getsize(word)
draw = ImageDraw.Draw(img)
draw.text((10, 10), word, font=font, fill=0)
print(img.size)
img.save("save.gif", "gif")
img.show()