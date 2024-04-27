
import telebot
from telebot import types
from datetime import datetime
import csv
from time import sleep
sleep(15) # чтобы бд успела загрузиться
from db_connect import *

API_TOKEN = '7050440167:AAFV4wSya-qHZ5w3Q47DmwnfxLY8xgH9UKQ' # токен бота
evaluation = ['1','2','3','4','5','6','7','8','9','10']
answers_list = []


def survey(message):
    # Функция опросника, в список можно грузить любое количество вопросов, возвращает список ответов
    question_list = ["О каком вебинаре Вы хотите рассказать?",
                     "Что вам больше всего понравилось в теме вебинара и почему?",
                     "Были ли моменты в вебинаре, которые вызвали затруднения в понимании материала? Можете описать их?",
                     "Какие аспекты вебинара, по вашему мнению, нуждаются в улучшении и какие конкретные изменения вы бы предложили?",
                     "Есть ли темы или вопросы, которые вы бы хотели изучить более подробно в следующих занятиях?",
                     ]
    answer_list = []
    old_len = 0
    # цикл смены вопросов
    for question in question_list:
            bot.send_message(message.chat.id, question)
            old_len = len(answer_list)
            while True:
                @bot.message_handler(func=lambda message: message.text, content_types=['text'])
                def answer_message(message):
                    answer_list.append(message.text)
                if len(answer_list) != old_len:
                    break
    return answer_list

def new_csv(answers_list, answers_date):
    #функция создания csv файла
    data = [
        ['timestamp', 'question_1', 'question_2','question_3','question_4','question_5','is_relevant','object','is_positive'],
        [answers_date, answers_list[0], answers_list[1], answers_list[2], answers_list[3], answers_list[4]]
    ]

    csv_file_path = 'test.csv'

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file '{csv_file_path}' created successfully.")


#Основной функционал бота

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Здравствуйте, я бот команды Gosling_te@m, написанный на коленке\
""")
    kb = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton(text='Старт', callback_data='true')
    kb.add(start_button)

    bot.send_message(message.chat.id,"Начинаем?", reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def before_test(callback):
    if callback.data == 'true':
        bot.send_message(callback.message.chat.id, "По шкале от 1 до 10, "
                                    "насколько вы готовы поделиться вашим мнением о вебинаре?")


@bot.message_handler(func=lambda message: message.text in evaluation, content_types=['text'])
def echo_message(message):
    if int(message.text) < 5:
         bot.reply_to(message, "Очень жаль, попробуйте в другой раз")
    else:
        bot.reply_to(message, "Опрос не займет много времени, "
                              "отвечайте на вопросы в развернутом виде")

        answers_list = survey(message) #получаем список ответов
        answers_date = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') # получаем актуальную дату

        bot.send_message(message.chat.id, "Спасибо за ответы, ваше мнение очень важно для нас:)")

        new_csv(answers_list,answers_date) #создаю новый csv файл
        insert_in_db(answers_list, answers_date) # заношу данные в бд


print("Gosling_Bot is Active!")
bot.infinity_polling()

