import telebot
from config import TELEGRAM_TOKEN
from PIL import Image

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def handle_start_command(message):
    bot.reply_to(message, "Para recibir los horarios ingrese la linea de BUS Ej: 6a habil, 6r6 sabado, 11a domingo")

@bot.message_handler(func=lambda message: message.text == "Horarios")
def send_horarios(message):
    horarios_html = '6A habil\n6A sabado\n6A domingo\n6R6 habil\n6R6 sabado\n6R6 domingo\n11A habil\n11A sabado\n11A domingo\n'
    bot.send_message(message.chat.id, horarios_html)

bus_horarios = {
    "6A habil": ("./img/6A-Horarios-Habiles.png", "Habiles"),
    "6A sabado": ("./img/6A-Sabado.png", "Sabado"),
    "6A domingo": ("./img/6A-Domingo.png", "Domingo"),
    "6R6 habil": ("./img/6R6-Habiles.png", "Habiles"),
    "6R6 sabado": ("./img/6R6-Sabado.png", "Sabado"),
    "6R6 domingo": ("./img/6R6-Domingo.png", "Domingo"),
    "11A habil": (["./img/11A-habil-hacia-montevideo.jpg", "./img/11A-habil-desde-montevideo.jpg"], ["Habil Desde Sauce", "Habil Desde Montevideo"]),
    "11A sabado": (["./img/11A-sabado-hacia-montevideo.jpg", "./img/11A-sabado-desde-montevideo.jpg"], ["Sabado Desde Sauce", "Sabado Desde Montevideo"]),
    "11A domingo": (["./img/11A-domingo-hacia-montevideo.jpg", "./img/11A-domingo-desde-montevideo.jpg"], ["Domingo Desde Sauce", "Domingo Desde Montevideo"]),
}

@bot.message_handler(func=lambda message: message.text in bus_horarios.keys())
def send_bus_horarios(message):
    img_paths, captions = bus_horarios[message.text]
    if isinstance(img_paths, str):
        img_path = img_paths
        photo = open(img_path, "rb")
        bot.send_photo(message.chat.id, photo, caption=captions)
    elif isinstance(img_paths, list):
        for img_path, caption in zip(img_paths, captions):
            photo = open(img_path, "rb")
            bot.send_photo(message.chat.id, photo, caption=caption)

# MAIN
if __name__ == '__main__':
    print('Bot Iniciado')
    bot.infinity_polling()
