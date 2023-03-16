import datetime
from instabot import Bot


def main():
    # get today's date
    date = datetime.date.today()
    # create a new bot
    bot = Bot()
    # login with the user's credentials
    bot.login(username="your_username", password="your_password")
    # upload the quote image with a set caption
    bot.upload_photo("quoteImage.png", caption="QOTD: " + str(date))
