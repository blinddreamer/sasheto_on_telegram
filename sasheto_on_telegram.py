import telegram.ext
import os
import requests
import re

TOKENO = os.environ['TOKEN']

def start(update, context):
    update.message.reply_text("....и ти ли си НЕумен като Гнома?")

def help(update, context):
    update.message.reply_text("""
    Available commands:
    /start -> Welcome Message
    /help -> This Message
    /fishing -> Information About.. well Fishing
    /dogo -> Dog Pics EVERYWHERE!
    """)
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def fishing(update, context):
    update.message.reply_text("Всичко в риболова смърди!\nРибата смърди. Вашата стръв смърди – независимо дали е старо синьо сирене, лепкави червеи, рибни пелети или люти протеинови топчета.\nРиболовците вярват, че колкото по-отвратително мирише стръвта им толкова по-апетитна хапка за рибите е тя.\nА, ако имате и късмета да хванете риба – след това и кепчето ви ще се усмърди (особено ако го оставите да изсъхне на слънце).\nДрехите ви и те съвсем скоро ще започнат да смърдят, ако си бършете ръцете от крачолите на панталона.\nЗа капак и вие ще започнете леко да понамирисвате. Неизбежно е, колкото и да се стараете да поддържате чистота!")

@run_async
def dogo(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

updater = telegram.ext.Updater(TOKENO, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("fishing", fishing))
disp.add_handler(telegram.ext.CommandHandler("dogo", dogo))


updater.start_polling()
updater.idle()