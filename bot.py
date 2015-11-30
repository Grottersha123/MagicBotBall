import config # модуль, в котором находятся все константы и токен

import telebot # модуль, который подключает к библиотеке телеграм https://github.com/sourcesimian/pyTelegramBotAPI
import time
import random

#https://core.telegram.org/bots/api#getupdates

def listener(messages): # принимает новые сообщения
	#for m in messages: # каждое слово 
		#if m.content_type == 'text':
        bot.send_message(messages[0].chat.id,random.choice(config.population))# отправляем 


if __name__=='__main__':
	bot = telebot.TeleBot(config.token)
	bot.set_update_listener(listener)
	bot.polling(none_stop=True) # это надо для того чтобы после 5 ошибок код останавливался
