import datetime
from instabot import Bot


date = datetime.date.today()
bot = Bot()

bot.login(username="your_username", password="your_password")
bot.upload_photo("quoteImage.png", caption="QOTD: " + str(date))
