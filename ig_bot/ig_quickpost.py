"""
ESTE PROGRAMA ES SOLO PARA SUBIR RAPIDAMENTE UNA FOTO
UNO DANDO EL DIA Y EL NUMERO DE LA FOTO

pip install -U instabot
git clone https://github.com/instagrambot/instabot --recursive
cd instabot/examples

el user id de notivan es 24994235608
"""

from instabot import Bot

bot = Bot()
bot.login(username="notivannordan", password="Falcon_12_45")


txt = "las pruebas como deben de ser"

hashtags = ".\n" + ".\n" + ".\n" + ".\n" + ".\n" + ".\n" + \
    "#pruebas #pruebas2 #pruebas3 #pruebas4"

cap = txt + hashtags

img = "/Users/dsalzedo/Documents/Python/instabot/pic/1.jpg"


user_id_1 = 24994235608

tags = [{'user_id': user_id_1, 'x': 0.1, 'y': 0.9}]

bot.upload_photo(img, user_tags=tags, caption=cap)
