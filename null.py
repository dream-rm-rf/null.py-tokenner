#subprocess.call("notepad.exe")
from prettytable import PrettyTable  
from progress.bar import IncrementalBar                                     
import time
bar = IncrementalBar('Подгрузка модулей...', max = 100)
for i in range(100):
    bar.next()
    time.sleep(0.02)
bar.finish()
from additional_func import get_time, console_log, clear, print_red, print_yellow, print_blue
from tokens import add_rows
token = 'null' 
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
    print_blue("11.Лайкнуть запись " + '(' + 'В разработке' + ')')
    add_rows()
    x  = int(input("Выберите функцию >>>"))
    from additional_func import post, friend_add, friend_remove, msg_send, vertyeplyshka, status_change, ava_change, unban, ban, comm

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
        time.sleep(1)
        menu()   
    # menu_ch()
menu()

