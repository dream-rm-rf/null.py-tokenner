from __main__ import *
import time
import sys                                                                     
import os
import subprocess 
import datetime                                                                 
import random

logging.basicConfig(filename='chats_ids.log', level=logging.INFO)
logging.basicConfig(filename='debug\debug.log', level=logging.DEBUG)
def get_time():  #Функция, необходимая для логирования времени
    return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S") #Выводит день/месяц/год/час/минута/секунда выполнения команды
def console_log(text, symbols_amount=30): #более красивая интерпретация функции print(), не поддерживает более 30 символов
    print("[" + get_time() + "] " + text) 
    print("-" * symbols_amount)
def clear(): #Очищение экрана, не всегда полезно, но незаменимо
    os.system('clear')
def print_red(text): #Цветной текст, немного багнутый, цвет может залипнуть, можно использовать с get_time(), но не с console_log()
    print("\033[31m {}" .format(text))
def print_yellow(text):
    print("\033[33m {}" .format(text))
def print_blue(text):
    print("\033[34m {}" .format(text))
def err_catch():
    print_red("Произошла ошибка, проверьте правильность ввода данных")
