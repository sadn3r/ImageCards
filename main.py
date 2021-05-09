from PIL import Image, ImageDraw, ImageFont


def generate_card(card_text: str):

    CARD_PADDING = 50
    FONT_SIZE = 16

    image_tmp = Image.new('RGB', (0, 0), (0, 0, 0))
    drawer_tmp = ImageDraw.Draw(image_tmp)

    font = ImageFont.truetype('DiabloHeavy.ttf', size=FONT_SIZE)
    # font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=FONT_SIZE)

    card_text_size = drawer_tmp.multiline_textsize(
        card_text,
        font
    )
    card_size = (
        card_text_size[0] + CARD_PADDING * 2,
        card_text_size[1] + CARD_PADDING * 2
    )

    image = Image.new('RGB', card_size, (0, 0, 0))
    drawer = ImageDraw.Draw(image)

    for num, line in enumerate(card_text.splitlines(), start=0):
        line_text_size = drawer.textsize(
            line,
            font
        )
        line_start = (card_size[0] - line_text_size[0]) / 2
        if num == 0:
            fill = (90, 88, 58) # 908858
        else:
            fill = (55, 55, 99)

        drawer.text((line_start, CARD_PADDING + (num * (FONT_SIZE + 2))), line, fill=fill, font=font, align="center")

    return image
