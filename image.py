from PIL import Image, ImageDraw, ImageFont

font_file = 'simhei.ttf'


def ps(text, name, high_size=700, font_size=80, color=(255, 255, 255)):
    img = Image.open('jpg/{}.jpg'.format(name))  # type: Image.Image
    if name == '1':
        font_size = 24
        high_size = 120
        color = (0, 0, 0)
    elif name == '2':
        font_size = 45
        high_size = 350
        color = (0, 0, 0)
    img_width = img.width  # 194
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_file, size=font_size)
    left = max((img_width - len(text) * font_size) // 2, 0)
    draw.text((left, high_size), text, color, font=font)
    img.save('jpg/002.jpg')


if __name__ == '__main__':
    ps('我我我我我我我我', '2')

