import json
from PIL import Image, ImageDraw, ImageFont
import requests
import random
import textwrap


def get_quote():
    request = requests.get("https://quotes.rest/qod")
    if request.status_code == 200:
        data = json.loads(request.text)
        quote = data['contents']['quotes'][0]['quote']
        author = data['contents']['quotes'][0]['author']
        return quote, author


def create_quote():
    quote, author = get_quote()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    font = ImageFont.truetype("./fonts/Oswald-Regular.ttf", size=20)

    quote_wrapped = textwrap.wrap(quote, width=40)
    formatted_quote = ""
    for ele in quote_wrapped:
        formatted_quote += str(ele) + "\n"
    formatted_quote += "- " + author + "\n"
    image = Image.new(mode="RGB", size=(512, 512),
                      color=(r, g, b))

    img_draw = ImageDraw.Draw(image)
    _, _, w, h = img_draw.textbbox((0,0), formatted_quote, font=font)
    x_text = (image.width - w) / 2
    y_text = (image.height - h) / 2
    img_draw.text((x_text, y_text), formatted_quote, align="center", font=font)
    image.save("quoteImage.png")


create_quote()
