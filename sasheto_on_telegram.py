import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("....и ти ли си НЕумен като Гнома?")

def help(update, context):
    update.message.reply_text("""
    Available commands:
    /start -> Welcome Message
    /help -> This Message
    /riba -> Information About Fishing
    """)

def fishing(update, context):
    update.message.reply_text("Всичко в риболова смърди!\nРибата смърди. Вашата стръв смърди – независимо дали е старо синьо сирене, лепкави червеи, рибни пелети или люти протеинови топчета.\nРиболовците вярват, че колкото по-отвратително мирише стръвта им толкова по-апетитна хапка за рибите е тя.\nА, ако имате и късмета да хванете риба – след това и кепчето ви ще се усмърди (особено ако го оставите да изсъхне на слънце).\nДрехите ви и те съвсем скоро ще започнат да смърдят, ако си бършете ръцете от крачолите на панталона.\nЗа капак и вие ще започнете леко да понамирисвате. Неизбежно е, колкото и да се стараете да поддържате чистота!")

def handle_message(update, context):
    update.message.reply_text()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("fishing", fishing))


updater.start_polling()
updater.idle()