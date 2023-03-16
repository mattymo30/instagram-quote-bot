import json
from PIL import Image, ImageDraw, ImageFont
import requests
import random
import textwrap
import upload


def get_quote():
    """
    Get the quote of the day data from https://quotes.rest/qod
    :return: The string representation of the daily quote and author
    """
    # use requests.get to retrieve info from the quote url if possible
    request = requests.get("https://quotes.rest/qod")
    # if status code was 200, the request was successful
    if request.status_code == 200:
        # load all the text from requests as a dictionary
        data = json.loads(request.text)
        # get the designated first quote and its author and return it
        quote = data['contents']['quotes'][0]['quote']
        author = data['contents']['quotes'][0]['author']
        return quote, author
    # else raise an exception that the request failed and end the program
    else:
        raise Exception("Data could not be obtained for quote")


def create_quote():
    """
    create the quote image to upload to instagram
    """
    # get the quote and author using the get_quote function
    quote, author = get_quote()
    # set the rgb values to random int values from 0-255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # set the font to the downloaded Oswald-Regular, size 20
    font = ImageFont.truetype("./fonts/Oswald-Regular.ttf", size=20)
    # wrap the quote with a max of 40 characters per line
    quote_wrapped = textwrap.wrap(quote, width=40)
    formatted_quote = ""
    # format the quote with newline to end each line of quote_wrapped
    for ele in quote_wrapped:
        formatted_quote += str(ele) + "\n"
    # concatenate the author after the quote
    formatted_quote += "- " + author + "\n"
    # create a new image, size 512x512 and color set to rgb values created
    image = Image.new(mode="RGB", size=(512, 512),
                      color=(r, g, b))

    img_draw = ImageDraw.Draw(image)
    # get the width and height of the formatted_quote string
    _, _, w, h = img_draw.textbbox((0, 0), formatted_quote, font=font)
    # center the text
    x_text = (image.width - w) / 2
    y_text = (image.height - h) / 2
    # draw the text onto the image and save it
    img_draw.text((x_text, y_text), formatted_quote, align="center", font=font)
    image.save("quoteImage.png")


if __name__ == "__main__":
    create_quote()
    upload.main()
