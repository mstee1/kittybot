import requests

from telegram import Bot

bot = Bot(token='5388647272:AAG7e4GsviOSW3flKOpEi6FkZ8lIpSIgx1A')

URL = 'https://api.thecatapi.com/v1/images/search'
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python


# # Рассмотрим структуру и содержимое переменной response
# print(response)

# # Посмотрим, какого типа переменная response
# print(type(response))

# # response - это список. А какой длины?
# print(len(response))

# # Посмотрим, какого типа первый элемент
# print(type(response[0])) 

chat_id = 1100876368
response = requests.get(URL).json()
random_cat_url = response[0].get('url')
# text = 'Вам телеграмма!'
# # Отправка сообщения
bot.send_message(chat_id, random_cat_url)
# # Отправка изображения
# bot.send_photo(chat_id, URL) 